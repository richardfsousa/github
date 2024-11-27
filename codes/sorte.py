import time
import os
import random
load = 0
while load <= 99 :
    car = "|"
    car = car*load
    load +=1
    print(f"{load}%\n")
    print(car)
    s = random.randint(1 ,3)
    time.sleep(s)
    os.system("cls")
print(f"{load}%")    
print(car)