from . import connection

print(connection.con.eth.get_block('latest'))
print(connection.con.eth.accounts)
print(f"{connection.con.eth.block_number}")
# balance=con.eth.get_balance(wallet_address)
# print(balance)
# print(f"{con.fromWei(balance,'ether')}")
# print(f"{con.eth.getTransaction('0xda62e5b3b65b662ccd78fc21959d1e568d84362972f288d591e13f21b5151a5c')}")