from tradeReader import TradeReader

reader = TradeReader()

reader.get_price('btc')

print(reader.get_coin_ohlc_by_id('btc', days = 1))
