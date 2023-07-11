pragma solidity ^0.8.0;

contract SampleContract {
    uint num = 5;

    function set(uint x) public {
        num = x;
    }

    function get() public view returns (uint) {
        return num;
    }
}