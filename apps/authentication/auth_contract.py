from web3 import Web3
import time
import sys
from .auth_contract_connection import contract_address,abi
sys.path.append('../')
from connection import connection


auth_contract = connection.con.eth.contract(address = contract_address, abi = abi)
print(auth_contract.address)
def execTxn(txName, txVar1, txVar2,txVar3,txVar4):
    print('executing ... ',txName, txVar1,txVar2,txVar3)
    nonce =connection.con.eth.getTransactionCount(connection.wallet_address)
    print(nonce)
    buildData = {
        'chainId': 4,
        'gas': 400000,
        'gasPrice': connection.con.toWei('40', 'gwei'),
        'nonce': nonce,
    }
    try:
        if (txName == 'registerUser'):
            txn_dict = auth_contract.functions.registerUser(txVar1, txVar2,txVar3).buildTransaction(buildData)
            print(txn_dict)
        
        if (txName == 'loginUser'):
            txn_dict = auth_contract.functions.loginUser(txVar1, txVar2).buildTransaction(buildData)
            print(txn_dict)
            
        if (txName == 'checkIsUserLogged'):
            txn_dict = auth_contract.functions.checkIsUserLogged(txVar1).buildTransaction(buildData)
            
        if (txName == 'logoutUser'):
            txn_dict = auth_contract.functions.logoutUser().buildTransaction(buildData)
            
        if(txName=='getUserData'):
            txn_dict = auth_contract.functions.getUserData().buildTransaction(buildData)
        
        if(txName=='changeUserData'):
            txn_dict = auth_contract.functions.changeUserData(txVar1,txVar2,txVar3,txVar4).buildTransaction(buildData)
        signed_txn = connection.con.eth.account.signTransaction(txn_dict, private_key=connection.wallet_private_key)
        result = connection.con.eth.sendRawTransaction(signed_txn.rawTransaction)
        print(result)
    except Exception as e:
        print(e)
        

    # Loop = 0
    # while (Loop < 10):
    #     try:
    #         tx_receipt = connection.con.eth.getTransactionReceipt(result)
    #         print(tx_receipt)
    #         if (txName == 'registerUser'):
    #             processed_receipt = auth_contract.events.RegNewUser().processReceipt(tx_receipt)
    #         if (txName == 'loginUser'):
    #               processed_receipt = auth_contract.events.LogInUser().processReceipt(tx_receipt)
    #         # if (txName == 'isUserLogin'):
    #         #      processed_receipt = auth_contract.events.IsUserLogin().processReceipt(tx_receipt)
    #         # print(processed_receipt)
    #         break
    #     except:
    #         print('Waiting ...')
    #         time.sleep(10)
    #         Loop += 1


