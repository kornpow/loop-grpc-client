from pathlib import Path
import shutil
import sh
import sys
import re
import os

app_dir = Path(os.getenv("APP_DIR"))
grpc_client_dir = Path(os.getenv("CLIENT_DIR"))

os.chdir(grpc_client_dir)

if not all([app_dir.exists(), grpc_client_dir.exists()]):
    print("Error: Double check that the paths exist!")
    sys.exit(1)

for proto in list(app_dir.rglob("**/*.proto")):
    print(proto)
    shutil.copy(proto, grpc_client_dir.joinpath("loopgrpc/compiled/"))
    print(f"Copied: {proto.name}")

# Modify auctioneer.proto from auctioneerrpc/auctioneer.proto --> poolgrpc/compiled/auctioneer.proto
for proto in list(grpc_client_dir.joinpath("loopgrpc/compiled/").rglob("*.proto")):
    with open(proto, 'r+') as f:
        text = f.read()
        text = re.sub('"swapserverrpc/common.proto"', '"loopgrpc/compiled/common.proto"', text)
        text = re.sub('"common.proto"', '"loopgrpc/compiled/common.proto"', text)
        # text = re.sub('signrpc/signer.proto', 'loopgrpc/compiled/signer.proto', text)
        f.seek(0)
        f.write(text)
        f.truncate()

protos = list(Path(".").joinpath("loopgrpc/compiled/").glob("*.proto"))

args = [
    "-m",
    "grpc_tools.protoc",
    "--proto_path=loopgrpc/googleapis:.",
    "--python_out=.",
    "--grpc_python_out=.",
]

for protofile in protos:
    args.append(str(protofile) )

# Generate the compiled protofiles
sh.python(args)