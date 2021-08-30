import websocket,json,pprint
from Information.info import Info
from MethodCaller.methodcaller import MethodCaller
from Indicators.MA import MA


SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"


class Main:

    pricing = 0

    def __init__(self):

        self.candle_closed = False
        self.close_price = 0

    def on_open(self):
        print('opened connection')

    def on_close(self):
        print('closed connection')

    def on_message(self, message):
        print('received message')
        json_message = json.loads(message)
        pprint.pprint(json_message)
        candle = json_message['k']
        is_candle_closed = candle['x']
        self.candle_closed = is_candle_closed
        self.close_price = candle['c']
        if self.candle_closed == True:
            print(self.close_price)
            Main.pricing = self.close_price
            Info.closes.append(float(self.close_price))
            if len(Info.closes) > 1:
                MethodCaller().call_sar_calculation()
            if len(Info.closes) > MA().FIRST_MA:
                MethodCaller().call_first_ma_calculation()
            if len(Info.closes) > MA().SECOND_MA:
                MethodCaller().call_second_ma_calculation()


ws = websocket.WebSocketApp(SOCKET, on_open= Main.on_open , on_close=Main.on_close,on_message= Main.on_message)
ws.run_forever()