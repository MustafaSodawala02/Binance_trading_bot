
import time, hmac, hashlib, requests, logging, os
BASE_URL = "https://testnet.binancefuture.com"

class BinanceClient:
    def __init__(self, key, secret):
        self.key = key
        self.secret = secret

    def sign(self, params):
        query = "&".join([f"{k}={v}" for k,v in params.items()])
        return hmac.new(self.secret.encode(), query.encode(), hashlib.sha256).hexdigest()

    def place_order(self, symbol, side, order_type, qty, price=None, stopPrice=None):
        endpoint = "/fapi/v1/order"
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": qty,
            "timestamp": int(time.time()*1000)
        }
        if price:
            params["price"] = price
            params["timeInForce"] = "GTC"
        if stopPrice:
            params["stopPrice"] = stopPrice

        params["signature"] = self.sign(params)

        headers = {"X-MBX-APIKEY": self.key}
        logging.info(f"Request: {params}")
        r = requests.post(BASE_URL+endpoint, headers=headers, params=params)
        logging.info(f"Response: {r.text}")
        return r.json()
