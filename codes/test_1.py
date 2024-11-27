palavra = input("digite uma palavra :")
print(palavra)
taman = len(palavra)
print(taman)
secret = ("_ "* taman)
print(str(secret))
src = list()
for i in secret :
    src.append(i)
print(src)
src[0] = "t" 
print (src)