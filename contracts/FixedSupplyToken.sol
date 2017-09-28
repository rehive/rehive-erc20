pragma solidity ^0.4.10;
import "./StandardToken.sol";
import "./SafeMath.sol";

contract FixedSupplyToken is StandardToken, SafeMath {

    // Token metadata
    string public constant name = "Fixed Supply Token";
    string public constant symbol = "FIX";
    uint256 public constant decimals = 18;
    string public version = "1.0";
    uint256 public totalSupply = 1000000;

    function FixedSupplyToken() {
        // Give the total supply to sender on contract creation
        balances[msg.sender] = totalSupply;
    }
}