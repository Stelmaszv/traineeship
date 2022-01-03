from abc import ABC, abstractmethod


class AbstractCounter(ABC):

    @abstractmethod
    def count(self):
        pass

class KilometresPerHourCounter(AbstractCounter):

    speed_of_sound=False
    result=0

    def count(self,value):
        self.result=value
        if self.result>121:
            self.speed_of_sound=True
        return self