# pool-grpc-client
A python grpc client for Lightning Pool (Lightning Network Daemon) ⚡⚡⚡

This is a wrapper around the default grpc interface that handles setting up credentials (including macaroons.

## Dependencies
- Python 3.6+
- Working LND lightning node, take note of its ip address.
- Copy your pool.macaroon and tls.cert files from `~/.pool/mainnet` to a directoy on your machine. 


## Installation
```bash
# NOT ON PYPI YET
pip install pool-grpc-client
```




## Basic Usage
The api mirrors the underlying lnd grpc api (http://api.lightning.community/) but methods will be in pep8 style. ie. `.GetInfo()` becomes `.get_info()`.

```python
from pathlib import Path
import json
from poolgrpc.client import PoolClient

credential_path = Path("/home/skorn/.pool/mainnet/")

mac = str(credential_path.joinpath("pool.macaroon").absolute())
tls = str(credential_path.joinpath("tls.cert").absolute())

pool = PoolClient(
	macaroon_filepath=mac,
	cert_filepath=tls
)

pool.get_info()

pool.get_lsat_tokens()
```

### Specifying Macaroon/Cert files
By default the client will attempt to lookup the `readonly.macaron` and `tls.cert` files in the mainnet directory. 
However if you want to specify a different macaroon or different path you can pass in the filepath explicitly.

```python
lnd = LNDClient(
    macaroon_filepath='~/.lnd/invoice.macaroon', 
    cert_filepath='path/to/tls.cert'
)
```

## Generating LND Proto Files
```bash
virtualenv lnd
source lnd/bin/activate
pip install grpcio grpcio-tools googleapis-common-protos sh
git clone https://github.com/lightningnetwork/lnd.git
mkdir genprotos
git clone https://github.com/googleapis/googleapis.git

# python -m grpc_tools.protoc --proto_path=googleapis:. --python_out=. --grpc_python_out=. rpc.proto
```

```python
from pathlib import Path
import shutil
import sh
import sys
import re
import os

loop_dir = Path.home().joinpath("Documents/lightning/loop")
grpc_client_dir = Path.home().joinpath("Documents/lightning/loop-grpc-client")

os.chdir(grpc_client_dir)

if not all([loop_dir.exists(), grpc_client_dir.exists()]):
    print("Error: Double check that the paths exist!")
    sys.exit(1)

for proto in list(loop_dir.rglob("**/*.proto")):
    shutil.copy(proto, grpc_client_dir.joinpath("loopgrpc/compiled/"))
    print(f"Copied: {proto.name}")

# Modify auctioneer.proto from auctioneerrpc/auctioneer.proto --> poolgrpc/compiled/auctioneer.proto
for proto in list(grpc_client_dir.joinpath("loopgrpc/compiled/").rglob("*.proto")):
    with open(proto, 'r+') as f:
        text = f.read()
        text = re.sub('import "swapserverrpc/common.proto";', 'import "loopgrpc/compiled/common.proto";', text)
        text = re.sub('import "common.proto";', 'import "loopgrpc/compiled/common.proto";', text)
        f.seek(0)
        f.write(text)
        f.truncate()

protos = list(Path(".").joinpath("loopgrpc/compiled/").glob("*.proto"))

args = [
    "-m",
    "grpc_tools.protoc",
    "--proto_path=loopgrpc/compiled/googleapis:.",
    "--python_out=.",
    "--grpc_python_out=.",
]

for protofile in protos:
    args.append(str(protofile) )

# Generate the compiled protofiles
sh.python(args)
```

## Deploy to Test-PyPi
```bash
poetry build
twine check dist/*
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```