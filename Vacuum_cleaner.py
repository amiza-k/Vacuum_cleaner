import time


def is_clean(a):
    Sensor=str(input("Is it clean? Y or N? "))
    while Sensor!= "Y" and Sensor!= "N":
        print("Please enter Y or N")
        Sensor=str(input("Is it clean? Y or N? "))
    if Sensor=="Y":
        if a=="A":
            A_room.append("Clean")
        else:
            B_room.append("Clean")
        print(f"Room {a} was clean")
    elif Sensor=="N":
        print("Cleaning. 7 seconds")
        if a=="A":
            A_room.append("Dirty")
        else:
            B_room.append("Dirty")
        time.sleep(7)
        print("Cleaning done")


def change_Room(a):
    if a=="A":
        print("Moving to room B")
        a="B"
    elif a=="B":
        print("Moving to room A")
        a="A"
    print("Moving. 3 seconds. ")
    time.sleep(3)
    return a

print("start")
a=str(input("Where am I? A or B? "))

while a!= "A" and a!= "B":
    print("Please enter A or B")
    a=str(input("Where am I? A or B? "))

A_room=[]
B_room=[]
RL=0
while RL<2:
    is_clean(a)
    a= change_Room(a)
    RL+=1
    print(f"I'm in room {a}")
print(f"finished cleaning. Room A: {A_room}, Room B: {B_room}")