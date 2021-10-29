from binance.client import Client
import config_spot as config
 
class Executer:
    def __init__(self):
        self.client = Client(config.API, config.API_secret, testnet=True)


    def order(self, symbol, side, quantity):
        response = self.client.create_test_order(symbol = symbol,
                                                 side = side,
                                                 type = 'MARKET',
                                                 quantity = quantity)
        print(f'{side} --> {symbol} = {quantity}')
        print(response)

    def balance(self, symbol):
        return float(self.client.get_asset_balance(symbol)['free'])


if __name__ == '__main__':
    executer = Executer()
    #print(executer.client.get_account())
    #executer.order('BTCUSDT', 'SELL', 0.1)
    #print(executer.balance('BTC'))