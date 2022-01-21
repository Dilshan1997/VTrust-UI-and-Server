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
wallet_address='0x72c29fcbfF1153A4E05d45E724b4B1Be2DED302e'
wallet_private_key =os.environ['PRIVATE_KEY']