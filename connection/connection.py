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


wallet_address='0xBD2Bd0f58a63De29436da0E285E1d4A6C6d6BF7f'
wallet_private_key ='983113e1658a401741dafeb70b59feb90d9a8191cb3ce171df9ff719726a3198'

