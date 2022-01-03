from abc import ABC, abstractmethod

class AbstractCounter(ABC):

    speed_of_sound_limit=0   #speed of soud value
    speed_of_sound=False     #if value is greater than speed of soud value
    result=0                 #result of couting

    def count(self,value):
        self.on_count(value)          #abstract method on count
        self.if_speed_of_soud(value)  #chceck if value is greater than speed of soud value
        return self

    @abstractmethod
    def on_count(self,value):
        pass

    def if_speed_of_soud(self,value):
        if int(value)>self.speed_of_sound_limit:
            self.speed_of_sound=True #if value is greater than speed of soud value set true

    def return_reslut(self):
        return str(self.result)

class KilometresPerHourCounter(AbstractCounter):

    speed_of_sound_limit=float(1234.8) #speed of soud value

    def on_count(self,value):
        self.result=float(value) * float(3280.840) #counting Foot Per Hour to Kilometres Per Hour

class FootPerHourCounter(AbstractCounter):

    speed_of_sound_limit=float(4051181) #speed of soud value

    def on_count(self,value):
        self.result=float(value) / float(3280.840) #counting Kilometres Per Hour to Foot Per Hour
