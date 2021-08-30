from Information.info import Info
from Indicators.MA import MA
from Indicators.SAR import SAR


class Bot:

    def __init__(self):
        self.ma = MA()
        self.sar = SAR()
        self.info = Info()
        self.target = 0
        self.stop_loss = 0
        self.in_position = False
        self.order_list = []
        self.position = "sell"

    def check_short_position(self):
        if float(self.info.current_price) < float(self.info.current_ma_first):
            self.ma.below_first_ma = True
            self.order_list.append('first')
            self.verify_short_position()

        if float(self.info.current_price) > float(self.info.current_ma_first):
            self.ma.correction_sell = True
            self.order_list.append('second')

        if self.ma.below_first_ma == True and self.ma.correction_sell == True:
            self.verify_short_position()

    def check_long_position(self):
        if float(self.info.current_price) > float(self.info.current_ma_first):
            self.ma.above_first_ma = True
            self.order_list.append('first')
            self.verify_long_position()

        if float(self.info.current_price) < float(self.info.current_ma_first):
            self.ma.correction_buy = True
            self.order_list.append('second')

        if self.ma.above_first_ma == True and self.ma.correction_buy == True:
            self.verify_long_position()

    def verify_long_position(self):
        if self.order_list[0] == 'first' and self.order_list[1] == 'second':
            if float(self.info.current_price) > float(self.sar.current_sar):
                self.sar.sar_buy = True
                self.order_list.append('third')
                print("BUYYYYYYYYYYYYYYYYYYY")
                stop_loss = float(self.sar.current_sar) - 10
                print(f"Stop loss : {stop_loss}")
                target_pip = float(self.info.current_price) - stop_loss
                target = float(self.info.current_price) + target_pip
                self.in_position = True
                print(f"Your target pips are {target_pip}")
                print(f"Your target is at the price {target}")
        else:
            self.order_list.clear()

    def verify_short_position(self):
        if self.order_list[0] == 'first' and self.order_list[1] == 'second':
            if float(self.info.current_price) < float(self.sar.current_sar):
                self.sar.sar_sell = True
                self.order_list.append('third')
                print("SELLLLLLLLL")
                stop_loss = float(self.sar.current_sar) + 10
                print(f"Stop loss : {stop_loss}")
                target_pip = float(self.info.current_price) + stop_loss
                target = float(self.info.current_price) - target_pip
                self.in_position = True
                print(f"Your target pips are {target_pip}")
                print(f"Your target is at the price {target}")
        else:
            self.order_list.clear()

    def check_buy(self):
        if self.position == "sell":
            self.position = "buy"
            self.ma.above_first_ma = False
            self.ma.correction_buy = False
            self.sar.sar_buy = False
            self.order_list.clear()
            self.check_long_position()
        else:
            self.check_long_position()

    def check_sell(self):
        if self.position == "buy":
            self.position = "sell"
            self.ma.below_first_ma = False
            self.ma.correction_sell = False
            self.sar.sar_sell = False
            self.order_list.clear()
            self.check_short_position()
        else:
            self.check_short_position()

    def is_first_ma_above_second(self):
        if self.ma.second_ma != None:
            if self.ma.first_ma > self.ma.second_ma:
                if self.in_position:
                    if float(self.info.current_price) < self.stop_loss:
                        print("You hit the stop loss")

                    if float(self.info.current_price) >= self.target:
                        print("You've reached the target")
                else:
                    self.check_buy()

    def is_first_ma_below_second(self):
        if self.ma.second_ma != None:
            if self.ma.first_ma < self.ma.second_ma:
                if self.in_position:
                    if float(self.info.current_price) > self.stop_loss:
                        print("You hit the stop loss")

                    if float(self.info.current_price) <= self.target:
                        print("You've reached the target")
                else:
                    self.check_sell()