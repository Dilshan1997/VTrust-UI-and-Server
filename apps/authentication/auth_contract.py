from eth_utils import address
from toolz.functoolz import return_none
from web3 import Web3
import time
import sys
from .auth_contract_connection import contract_address,abi
sys.path.append('../')
from connection import connection


auth_contract = connection.con.eth.contract(address = contract_address, abi = abi)
# addr=auth_contract.functions.get_address().call()
# print("address:",addr)
print(connection.con.eth.accounts[0])
# print(connection.con.eth.accounts[0])
def execTxn(txName,*args,**kwargs):
    print(args)
    return_value=None
    nonce =connection.con.eth.getTransactionCount(connection.wallet_address)
    print(nonce)
    buildData = {
        # 'from':args[0],
        # 'to':connection.wallet_address,
        'chainId': 4,
        'gas': 400000,
        'gasPrice': connection.con.toWei('40', 'gwei'),
        'nonce': nonce,
    }
    
    

    try:
        if (txName == 'registerUser'):
            txn_dict = auth_contract.functions.registerUser(*args).buildTransaction(buildData)
            return_value=auth_contract.functions.registerUser(*args).call()
            print(txn_dict)
    
        
        if (txName == 'loginUser'):
            txn_dict = auth_contract.functions.loginUser(*args).buildTransaction(buildData)
            return_value=auth_contract.functions.loginUser(*args).call()
            print(txn_dict)
            # address=auth_contract.functions.get_address().buildTransaction(buildData)
            # address=auth_contract.functions.get_address().call()
            # print("address:",address)
            
            
        if (txName == 'checkIsUserLogged'):
            return_value=auth_contract.functions.checkIsUserLogged(*args).call()
            
            
        if (txName == 'logoutUser'):
            txn_dict = auth_contract.functions.logoutUser().buildTransaction(buildData)
            print(txn_dict)
            
        if(txName=='getUserData'):
            return_value=auth_contract.functions.getUserData().call()
        
        if(txName=='changeUserData'):
            txn_dict = auth_contract.functions.changeUserData(*args).buildTransaction(buildData)
            return_value=auth_contract.functions.changeUserData(*args).call()
        signed_txn = connection.con.eth.account.signTransaction(txn_dict, private_key=connection.wallet_private_key)
        transcation_hash = connection.con.eth.sendRawTransaction(signed_txn.rawTransaction)
        print(txn_dict)
        print(transcation_hash)
    except Exception as e:
        print(e)
    if return_value!=None:
        return return_value

    
    
    # Loop = 0
    # while (Loop < 10):
    #     try:
    #         tx_receipt = connection.con.eth.getTransactionReceipt(transaction_hash)
    #         print(tx_receipt)
    #         if (txName == 'registerUser'):
    #             processed_receipt = auth_contract.events.RegNewUser().processReceipt(tx_receipt)
    #         if (txName == 'loginUser'):
    #               processed_receipt = auth_contract.events.LogInUser().processReceipt(tx_receipt)
    #         if (txName == 'isUserLogin'):
    #              processed_receipt = auth_contract.events.checkIsUserLogged().processReceipt(tx_receipt)
    #         print(processed_receipt)
    #         break
    #     except:
    #         print('Waiting ...')
    #         time.sleep(10)
    #         Loop += 1


# print(auth_contract.functions.getUserData().call())
# print(auth_contract.functions.checkIsUserLogged('0x72c29fcbfF1153A4E05d45E724b4B1Be2DED302e').call())
# print(auth_contract.functions. loginUser("dd","").call())
# print(auth_contract.functions.getUserBalance().call())


# print(connection.con.eth.get_block_number())
# print(connection.con.eth.get_balance('0x902b3443aD7DBb594534b10cf09307374c17a3Bd'))
# print(connection.con.isConnected())
# x=auth_contract.functions.logoutUser().call()
# print(x)
