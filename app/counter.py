from abc import ABC, abstractmethod

class AbstractCounter(ABC):

    speed_of_sound_limit=0
    speed_of_sound=False
    result=0

    def count(self,value):
        self.on_count(value)
        self.if_speed_of_soud(value)
        return self

    @abstractmethod
    def on_count(self,value):
        pass

    def if_speed_of_soud(self,value):
        if value>self.speed_of_sound_limit:
            self.speed_of_sound=True

class KilometresPerHourCounter(AbstractCounter):

    speed_of_sound=False
    result=0
    speed_of_sound_limit=1234.8

    def on_count(self,value):
        self.result=value * 3280.840

class FootPerHourCounter(AbstractCounter):

    speed_of_sound=False
    result=0
    speed_of_sound_limit=4051181

    def on_count(self,value):
        self.result=value / 3280.840
