idade = int(input("Qual é a sua idade: "))
if (idade < 12):
    print("Criança")
elif (idade >= 12) and (idade <= 18):
    print("Adolescente")
else:
    print("Adulto")
