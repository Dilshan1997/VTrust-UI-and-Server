from web3 import Web3
from web3.auto import w3
import os
from dotenv import load_dotenv
load_dotenv()

connected = w3.isConnected()
print(connected)

node_provider=os.environ['NODE_PROVIDER_LOCAL']
print(node_provider)
con=Web3(Web3.HTTPProvider(node_provider))


wallet_address='0xA6acec1607fF4046252d158ca00000009737BFEC'
wallet_private_key ='56f239e8a9ca4ac985cf7f96f3f1d1658af2ab35e2a1e0804c9ecdc6b44d50c8'

