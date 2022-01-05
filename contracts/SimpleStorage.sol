// SPDX-License-Identifier: MIT
pragma solidity 0.8.10;

contract SimpleStorage {
    uint256 favoriteNumber;

    // Update favorite number value
    function store(uint256 _favoriteNumber) public returns (uint256) {
        favoriteNumber = _favoriteNumber;
        return favoriteNumber;
    }

    // Get favorite numver
    function retrieve() public view returns (uint256) {
        return favoriteNumber;
    }

    struct Person {
        uint256 favoriteNumber;
        string name;
    }

    Person[] public people;
    mapping(string => uint256) public nameToFavoriteNumber;

    // Add Person to people's list with its name and favorite number
    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(Person(_favoriteNumber, _name));
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }
}
