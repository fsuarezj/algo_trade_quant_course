from nomics import Nomics

from configparser import ConfigParser
api_keys = ConfigParser()
api_keys.read("api_keys_config.ini")

nomics = Nomics(api_keys["API_KEYS"]["nomics"])

markets = nomics.Markets.get_markets()

candles = nomics.Candles.get_candles(interval = "1d", exchange = "binance", currency = "ETH")

candles
