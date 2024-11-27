print("gibs")
quant = 0
print("se quiser que o programa pare digite >>x<<")
while quant != "x" :
    quant = int(input("são quantas revitas "))
    if quant == "x" :
        print("obrigado pela preferencia")
    if quant < 8 : 
        total = quant * 5.00
    elif (quant > 8) or (quant < 15) :
        total = quant * 4.50
    elif quant > 15 :
        total = quant * 2.50 
    print(f"o valo da sua compra é {total}")
    