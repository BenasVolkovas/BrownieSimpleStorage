from brownie import accounts, config, network, SimpleStorage


def deploy_simple_storage():
    account = get_account()
    simpleStorage = SimpleStorage.deploy({"from": account})

    # Get number
    storedValue = simpleStorage.retrieve()
    print(storedValue)

    # Store new number
    storeTransaction = simpleStorage.store(15, {"from": account})
    storeTransaction.wait(1)
    updatedStoredValue = simpleStorage.retrieve()
    print(updatedStoredValue)


def get_account():
    # account = accounts[0]
    # account = accounts.load("main-account")
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # account = accounts.add(config["wallets"]["from_key"])

    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
