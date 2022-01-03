run = False
from app.counter import KilometresPerHourCounter, FootPerHourCounter

while run ==False:
    print("1 For counting Foot Per Hour to Kilometres Per Hour:")
    print("2 For counting Kilometres Per Hour to Foot Per Hour")
    value=input("Please set Type of couting :")
    if int(value)  == 1 or int(value) == 2:
        objets={
            1:KilometresPerHourCounter,
            2:FootPerHourCounter
        }
        object=objets.get(int(value))
        value_for_counting = input("Please enter value:")
        data=object().count(int(value_for_counting))
        print(data.result)
        if data.speed_of_sound:
            print('Warning speed of sound !')