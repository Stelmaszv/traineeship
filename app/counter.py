from abc import ABC, abstractmethod


class AbstractCounter(ABC):

    @abstractmethod
    def count(self):
        pass

class KilometresPerHourCounter(AbstractCounter):

    speed_of_sound=False
    result=0
    speed_of_sound_limit=1234.8

    def count(self,value):
        self.result=value * 3280.840
        if value>self.speed_of_sound_limit:
            self.speed_of_sound=True
        return self