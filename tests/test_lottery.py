from brownie import Lottery, accounts, config, network
from web3 import Web3

# 0.013
# 13000000000000000
# 13315353095235598


def test_get_entrance_fee():
    account = accounts[0]
    lottery = Lottery.deploy(
        config["networks"][network.show_active()]["eth_usd_price_feed"],
        {"from": account},
    )
    assert lottery.getEntranceFee() > 12000000000000000
    assert lottery.getEntranceFee() > Web3.toWei(0.012, "ether")
    assert lottery.getEntranceFee() < Web3.toWei(0.015, "ether")
