from brownie import SimpleStorage, accounts, config


def read_contract():
    # Get latest deployment
    simpleStorage = SimpleStorage[-1]
    print(simpleStorage.retrieve())

def main():
    read_contract()
