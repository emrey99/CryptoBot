from Indicators.SAR import SAR
from Indicators.MA import MA
from Bot.bot import Bot

class MethodCaller:


    def __init__(self):
        self.sar = SAR()
        self.ma = MA()
        self.bot = Bot()

    def call_sar_calculation(self):
        self.sar.calculate_sar()

    def call_first_ma_calculation(self):
        self.ma.calculate_first_ma()

    def call_second_ma_calculation(self):
        self.ma.calculate_second_ma()
        self.bot.is_first_ma_above_second()
        self.bot.is_first_ma_below_second()