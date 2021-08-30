import talib
import numpy
from Information.info import Info
from InterfaceIndicators.InterfaceIndicators import MaIndicators

class MA(MaIndicators):

    FIRST_MA = 20
    SECOND_MA = 50


    def __init__(self):
        self.above_first_ma = False
        self.below_first_ma = False
        self.correction_buy = False
        self.correction_sell = False
        self.first_ma = None
        self.second_ma = None
        self.info = Info()

    def calculate_first_ma(self):
            ma_closes = numpy.array(self.info.closes)
            ma = talib.MA(ma_closes,timeperiod = MA.FIRST_MA,matype = 0)
            self.first_ma = float(ma[-1])
            self.info.current_ma_first = self.first_ma
            print("20 ma is:")
            print(self.first_ma)

    def calculate_second_ma(self):
            ma_closes = numpy.array(self.info.closes)
            ma = talib.MA(ma_closes, timeperiod=MA.SECOND_MA, matype=0)
            self.second_ma = float(ma[-1])
            self.info.current_ma_second = self.second_ma
            print("50 ma is:")
            print(self.second_ma)