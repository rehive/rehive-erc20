pragma solidity ^0.4.10;
import "./FixedSupplyToken.sol";

contract EchargeToken is FixedSupplyToken {

    // Token metadata
    string public constant name = "eCharge";
    string public constant symbol = "ECH";
    uint256 public constant decimals = 18;
    string public version = "1.0";
    uint256 public totalSupply = 1000000;
}
