palavra = input("digite uma palavra :")
print(palavra)
taman = len(palavra)
print(taman)
secret = ("_ "* taman)
print(str(secret))
for i in palavra :
    x = str(input())
letras = list()
for letra in palavra :
    letras.append(letra)

print(letras)
secrit = input()
for i in letras :
    if i == letras :
        print("boa")
     
