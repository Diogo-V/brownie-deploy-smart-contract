import json
from web3 import Web3, HTTPProvider

w3 = Web3(HTTPProvider('http://127.0.0.1:8545'))

f = open('/usercode/deploy/build/contracts/SampleContract.json')
data = json.load(f)

abi = data['abi']

address = '0x257c9E9027E4D8E66898f11127Ce392c886D0A3C'

contract = w3.eth.contract(address=address, abi=abi)

isConnected = w3.isConnected()
blocknumber = w3.eth.blockNumber

account = w3.eth.accounts[0]
balance = w3.eth.get_balance(account)

print('Connected:', isConnected, 'BlockNumber:', blocknumber, 'Account Balance:', w3.fromWei(balance, 'Ether'))

buffer = contract.functions.get().call()
print('Old value of num:', buffer)

tx = contract.functions.set(40).transact({'from': account})
print(w3.eth.wait_for_transaction_receipt(tx))

buffer = contract.functions.get().call()
print('New value of num:', buffer)