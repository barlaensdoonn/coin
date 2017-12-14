#!/usr/local/bin/python3
# coins - interact with APIs to get current balances and prices
# 12/13/17
# updated 12/13/17

import requests


class Prices(object):
    '''get current prices from coinmarketcap.com API'''

    coins = {
        'BTC': 'bitcoin',
        'ETH': 'ethereum',
        'LTC': 'litecoin',
        'ZEC': 'zcash',
        'DCRD': 'decred',
        'SIA': 'siacoin',
        'XEM': 'nem',
        'XLM': 'stellar',
        'MIOTA': 'iota',
        'DATA': 'streamr-datacoin',
        'GNT': 'golem'
    }

    def __init__(self):
        self.prices = {key: self.request_price(self.coins[key]) for key in self.coins.keys()}

    def _construct_url(self, coin):
        return 'https://api.coinmarketcap.com/v1/ticker/{id}/'.format(id=coin)

    def request_price(self, coin):
        r = requests.get(self._construct_url(coin))

        if r.status_code == 200:
            r_parsed = r.json()[0]
            return float(r_parsed['price_usd'])
        else:
            return None
