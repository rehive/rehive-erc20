var EchargeToken = artifacts.require("./EchargeToken.sol");

module.exports = function(deployer) {
    deployer.deploy(EchargeToken)
};
