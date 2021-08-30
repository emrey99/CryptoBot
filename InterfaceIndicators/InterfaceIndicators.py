from abc import ABC,abstractmethod



class SarIndicator(ABC):

    @abstractmethod
    def calculate_sar(self):
        raise NotImplementedError


class MaIndicators(ABC):

    @abstractmethod
    def calculate_first_ma(self):
        raise NotImplementedError

    @abstractmethod
    def calculate_second_ma(self):
        raise NotImplementedError
