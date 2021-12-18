from brownie import accounts, SimpleStorage
from brownie.network import account


def test_deploy():
    # Arrange, Act, Assert

    # Arrange
    account = accounts[0]
    # Act
    simpleStorage = SimpleStorage.deploy({"from": account})
    startinValue = simpleStorage.retrieve()
    expected = 0
    # Assert
    assert startinValue == expected


def test_updating_storage():
    # Arrange
    account = accounts[0]
    simpleStorage = SimpleStorage.deploy({"from": account})
    # Act
    expected = 15
    simpleStorage.store(expected, {"from": account})
    # Assert
    assert simpleStorage.retrieve() == expected
