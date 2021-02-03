from pycoingecko import CoinGeckoAPI

class TradeReader():
    coin_id = {
        'btc': 'bitcoin',
        'eth': 'ethereum'
    }

    def __init__(self, fiat = 'eur', source = "coingecko"):
        self.source = source
        self.fiat = 'eur'
        if self.source == "coingecko":
            self.api = CoinGeckoAPI()

    def get_price(self, id, fiat = ""):
        if fiat == "":
            fiat = self.fiat
        return self.api.get_price(self.coin_id[id], fiat)

    def get_coin_ohlc_by_id(self, id, fiat ="", days = 1):
        if fiat == "":
            fiat = self.fiat
        return self.api.get_coin_ohlc_by_id(self.coin_id[id], fiat, days)
