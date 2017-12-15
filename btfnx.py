#!/usr/local/bin/python3
# coins - get wallet balances from bitfinex
# 12/15/17
# updated 12/15/17

# code modified from the bitfinex examples

import requests
import json
import base64
import hashlib
import hmac
import time  # for nonce
import kys


class BitfinexClient(object):
    key = kys.btfnx_ky
    scrt = kys.btfnx_scrt

    def _nonce(self):
        '''returns a nonce. used in authentication'''

        return str(int(round(time.time() * 1000)))

    def _headers(self, path, nonce, body):
        sig = "/api/" + path + nonce + body
        print("signing: {}".format(sig))
        h = hmac.new(self.scrt, sig, hashlib.sha384)
        sig = h.hexdigest()

        return {
            "bfx-nonce": nonce,
            "bfx-apikey": self.key,
            "bfx-signature": sig,
            "content-type": "application/json"
        }

    def _construct_url(self):
        # TODO
        pass

    def active_orders(self):
        '''fetch active orders'''

        nonce = self._nonce()
        body = {}
        rawBody = json.dumps(body)
        path = "v2/auth/r/orders"
        print(self.base_url + path)
        print(nonce)

        headers = self._headers(path, nonce, rawBody)
        print(headers)
        print(rawBody)

        # print("requests.post("+self.BASE_URL + path + ", headers=" + str(headers) + ", data=" + rawBody + ", verify=True)")
        r = requests.post(self.BASE_URL + path, headers=headers, data=rawBody, verify=True)

        return r.json() if r.status_code == 200 else None

    def get_balances
