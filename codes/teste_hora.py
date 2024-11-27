import os
import time
s = str(input("ja e noite "))
while s == 's' :
    if s == "s" :
        print("boa noite")
    time.sleep(3)
    os.system('cls')
    s = str(input("ja e noite "))
print(time)