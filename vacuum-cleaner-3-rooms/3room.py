import time


def is_clean(a):
    Sensor=str(input("Is it clean? Y or N? ").upper())
    while Sensor!= "Y" and Sensor!= "N":
        print("Please enter Y or N")
        Sensor=str(input("Is it clean? Y or N? ").upper())        
    if Sensor=="N":
        print("Cleaning. 7 seconds")
        time.sleep(7)
        print("Cleaning done")
    if a=="A":
        A_room.append("Clean")
    elif a=="B":
        B_room.append("Clean")
    elif a=="C":
        C_room.append("Clean")
    

def change_Room(a,RL,lm):
    if RL==0:
        if a=="A":
            print("Moving to room B. Right")
            lm="Right"
            a="B"
        elif a=="B":
            print("Moving to room C. Right")
            a="C"
        elif a=="C":
            print("Moving to room B. Left")
            lm="Left"
            a="B"
    elif RL==1:
        if a=="B":
            if lm=="Right":
                print("Moving to room C. Right")
                a="C"
            elif lm=="Left":
                print("Moving to room A. Left")
                a="A"
        elif a=="C":
            print("Moving to room B. Left")
            a="B"
    elif RL==2:
        if a=="B":
            print("Moving to room A. Left")
            a="A"
    print("Moving. 3 seconds. ")
    time.sleep(3)
    return a , lm


print("start")
a=str(input("Where am I? A or B or C? ").upper())

while a!= "A" and a!= "B" and a!="C":
    print("Please enter A or B or C")
    a=str(input("Where am I? A or B or C? ").upper())

A_room=[]
B_room=[]
C_room=[]
RL=0
lm=str()

while not (A_room and B_room and C_room):
    is_clean(a)
    print(f"Room {a} was clean")
    a , lm = change_Room(a,RL,lm)
    RL+=1
    print(f"I'm in room {a}")
print(f"finished cleaning. Room A: {A_room}, Room B: {B_room}, Room C: {C_room}.")