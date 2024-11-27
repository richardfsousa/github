resposta = input ("Deseja calcular o fatorial de um número? (S/N) ")
while (resposta == "s") or (resposta == "S"):
    numero = int(input("digite o seu número: "))
    if numero < 0:
        print("Impossivel calcular! Número tem que ser >= 0 ")
    else:
        resultado = 1
        for i in range (2, numero + 1):
            resultado = resultado * i
        print(f"O fatorial de {numero} é {resultado}. ")
    resposta = input ("deseja calcular o fatorial de um número (S/N) ")