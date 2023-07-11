from brownie import SampleContract, accounts

id = 'metamask wallets private key'

def main():
    wallet = accounts.load(id)
    SampleContract.deploy({'from': wallet})