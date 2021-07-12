from pathlib import Path
import json
from pprint import pprint
import os
import base64
from time import sleep
from datetime import datetime, timedelta

# Pip installed Modules
from loopgrpc import LoopClient
from protobuf_to_dict import protobuf_to_dict

credential_path = Path("/home/skorn/Documents/creds/kungmeow/loop")

mac = str(credential_path.joinpath("loop.macaroon").absolute())
tls = str(credential_path.joinpath("tls.cert").absolute())

loop = LoopClient(
	"192.168.1.58:11010",
	macaroon_filepath=mac,
	cert_filepath=tls
)




from pathlib import Path
import json
from pprint import pprint
import os
import base64
from time import sleep
from datetime import datetime, timedelta

# Pip installed Modules
from loopgrpc import LoopClient
from protobuf_to_dict import protobuf_to_dict

credential_path = Path("/home/skorn/.loop/mainnet")

mac = str(credential_path.joinpath("loop.macaroon").absolute())
tls = str(credential_path.joinpath("tls.cert").absolute())


loop = LoopClient(
	"127.0.0.1:11010",
	macaroon_filepath=mac,
	cert_filepath=tls
)