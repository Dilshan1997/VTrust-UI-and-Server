
from traceback import print_tb
from web3 import Web3
import time
import sys
from .ballot_contract_connection import contract_address,abi
sys.path.append('../')
from connection import connection
ballot_contract = connection.con.eth.contract(address = contract_address, abi = abi)

def execTxn(txName,*args,**kwargs):
    print(args)
    
    return_value=None
    error_message=None
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
        if (txName == 'createBallot'):
            buildData['gas']=6721974
            txn_dict = ballot_contract.functions.createBallot(*args).buildTransaction(buildData)
            return_value=ballot_contract.functions.createBallot(*args).call()
            print(txn_dict)
    
        
        if (txName == 'createProposal'):
            buildData['gas']=6721974
            # buildData['gas']=100000000
            txn_dict = ballot_contract.functions.createProposal(*args).buildTransaction(buildData)
            # return_value=ballot_contract.functions.createProposal(*args).call()
            print(txn_dict)
            # address=ballot_contract.functions.get_address().buildTransaction(buildData)
            # address=ballot_contract.functions.get_address().call()
            # print("address:",address) 
              
        if (txName == 'voting'):
            txn_dict = ballot_contract.functions.voting(*args).buildTransaction(buildData)
            return_value=(ballot_contract.functions.voting(*args).call())
            print("return value",return_value)
            # print("print*****************",connection.con.eth.get_block("latest"))
        if (txName == 'getBallotId'):
            return_value = ballot_contract.functions.getBallotId().call()
            
        if(txName=='getBallotDetails'):
            return_value = ballot_contract.functions.getBallotDetails(*args).call()
        
        if(txName=='getProposalDetails'):
            return_value = ballot_contract.functions.getProposalDetails(*args).call()
            
        if(txName=='getProposalResult'):
            return_value = ballot_contract.functions.getProposalResult(*args).call()   
            
        if(txName=='winningProposal'):
            return_value = ballot_contract.functions.winningProposal(*args).call()  
            
        if(txName=='dashboardData'):
            return_value = ballot_contract.functions.getDashboardData(*args).call()      

        if(txName=='savePrivateBallotIds'):
            txn_dict=ballot_contract.functions.savePrivateBallotIds(*args).buildTransaction(buildData)  
            return_value = ballot_contract.functions.savePrivateBallotIds(*args).call() 
        
        if(txName=='getPrivateBallotIds'): 
            return_value = ballot_contract.functions.getPrivateIds(*args).call()    
            
        if(txName=='savePrivateVotersData'):
            txn_dict=ballot_contract.functions.savePrivateVotersData(*args).buildTransaction(buildData)
        
        if(txName=='getPrivateVotersData'): 
           return_value = ballot_contract.functions.getPrivateVotersData(*args).call()
        
        if(txName=='privateBallotVoting'):
            buildData['gas']=6721974
            txn_dict=ballot_contract.functions.privateBallotVoting(*args).buildTransaction(buildData)
            return_value=ballot_contract.functions.privateBallotVoting(*args).call()
        
        if(txName=='setFollowers'): 
            txn_dict=ballot_contract.functions.setFollwers(*args).buildTransaction(buildData)
        
        if(txName=='getFollowingBallots'): 
            return_value=ballot_contract.functions.getFollowingBallots(*args).call()
        
        signed_txn = connection.con.eth.account.signTransaction(txn_dict, private_key=connection.wallet_private_key)
        transcation_hash = connection.con.eth.sendRawTransaction(signed_txn.rawTransaction)
        # print(txn_dict)
        # print(transcation_hash)
    except Exception as e:
        error_message=e
        
    if return_value!=None:
        return return_value
    else:
        return error_message

# print(ballot_contract.functions.getBallotDetatils(1).call())
# print(ballot_contract.functions.getProposaldetails('1-0').call())
# print(ballot_contract.functions.getBallotId().call())