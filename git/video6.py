resposta = input("Deseja calcular o fatorial de um número? (s/n) ")

while (resposta == "s") or (resposta == "S"):

    numero = int(input("Digite o seu número: "))

    if numero < 0 :
        print("Impossível calcular! Número tem que ser >= 0.")
    else:
        resultado = 1

        for i in range(2, numero + 1):

            resultado = resultado * 1
        print(f"O fatorial de {numero} é {resultado}.")
    resposta = input("Deseja calcular o fatorial de um número? (s/n) ")