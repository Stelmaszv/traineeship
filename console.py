run = False
from app.counter import KilometresPerHourCounter, FootPerHourCounter

while run ==False:
    print("1 For counting Foot Per Hour to Kilometres Per Hour:")
    print("2 For counting Kilometres Per Hour to Foot Per Hour")
    value=input("Please set Type of couting :")
    if int(value)  == 1 or int(value) == 2:
        #seting type of couting
        objets={
            1:KilometresPerHourCounter,
            2:FootPerHourCounter
        }
        # set counter
        object=objets.get(int(value))
        # enter value
        value_for_counting = input("Please enter value:")
        # counting
        data=object().count(int(value_for_counting))
        print(data.result)
        # show if speed of sound
        if data.speed_of_sound:
            print('Warning speed of sound !')