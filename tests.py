import unittest
from app.counter import KilometresPerHourCounter, FootPerHourCounter

#tests For Test_KilometresPerHourCounter
class Test_KilometresPerHourCounter(unittest.TestCase):

    # tests For Test_KilometresPerHourCounter count
    def test_for_kilometres_per_hour_counter(self):
        Obj=KilometresPerHourCounter()
        Obj.count('123')
        self.assertEqual(Obj.result,403543.32)

    # tests For speed for sound for KilometresPerHourCounter
    def test_for_kilometres_per_speedof_soud(self):
        Obj=KilometresPerHourCounter()
        Obj.count('13145')
        self.assertEqual(Obj.speed_of_sound,True)


#tests For Test_FootPerHourCounter
class Test_KilometresPerHourSpeedofsoud(unittest.TestCase):

    # tests For Test_FootPerHourCounter count
    def test_for_kilometres_per_hour_counter(self):
        Obj=FootPerHourCounter()
        Obj.count('13145')
        self.assertEqual(Obj.result,4.006595871788932)

    # tests For speed for sound for FootPerHourCounter
    def test_for_kilometres_per_speedof_soud(self):
        Obj=KilometresPerHourCounter()
        Obj.count('4141415')
        self.assertEqual(Obj.speed_of_sound,True)

if __name__ == '__main__':
    unittest.main()