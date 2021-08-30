import talib
import numpy
from Information.info import Info
from InterfaceIndicators.InterfaceIndicators import SarIndicator

class SAR(SarIndicator):

    def __init__(self):
        self.sar_buy = False
        self.sar_sell = False
        self.current_sar = 0
        self.info = Info()

    def calculate_sar(self):
        sar_closes = numpy.array(self.info.closes)
        sar = talib.SAR(sar_closes, sar_closes, acceleration=0.02, maximum=0.2)
        self.current_sar = sar[-1]
        self.info.current_sar = self.current_sar
        print("the sar is:")
        print(sar[-1])