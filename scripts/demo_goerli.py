import json
from web3 import Web3, HTTPProvider

# Add the infura project id here
w3 = Web3(HTTPProvider('https://goerli.infura.io/v3/<your infura project id>'))

f = open('/usercode/deploy/build/contracts/SampleContract.json')
data = json.load(f)

abi = data['abi']
# Add the contract address here
address = '<address>'

contract = w3.eth.contract(address=address, abi=abi)

isConnected = w3.isConnected()
blocknumber = w3.eth.blockNumber

print('Connected:', isConnected, 'BlockNumber:', blocknumber)

# Add Metamask wallet address here
nonce = w3.eth.getTransactionCount('<Metamask wallet address>')

tx_dict = contract.functions.set(25).buildTransaction({
    'chainId' : 5,
    'gas' : 2100000,
    'gasPrice' : w3.toWei('5', 'gwei'),
    'nonce' : nonce,
})

# Add Metamask wallet private key here
signed_tx = w3.eth.account.sign_transaction(tx_dict, '< Metamask wallet private key >')
tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash, timeout=240)

print(tx_receipt)