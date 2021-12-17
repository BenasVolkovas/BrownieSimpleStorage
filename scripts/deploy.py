from brownie import accounts, config


def deploy_simple_storage():
    account = accounts[0]
    # account = accounts.load("main-account")
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # account = accounts.add(config["wallets"]["from_key"])
    print(account)


def main():
    deploy_simple_storage()
