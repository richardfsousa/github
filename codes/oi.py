import time 
import os
import random
import sys
comodos = ["[1]sala","[2]quarto","[3]corredor"]
for i in comodos :
        print(i)
ir = input("escolha um comodo para olhar : ")
os.system("cls")
if ir != 1 and 2 and 3 :
        print("você digitou algo errado\ntente novamente!! ")
        while ir != 1 and 2 and 3 :
            for i in comodos :
                print(i)
            ir = input("escolha um comodo para olhar : ")
            if ir == 1 :
                for o in range(9):
                    print(f"carregando{"."*o}")
                    if o == 3%0 :
                        sys.stdout.write("033[F")

    
