print("conversão binario para decimal")
bin =list(map(str,input("digite o numero para conversão\n").split(" ")))
print(bin)
tam = len(bin)
e = 0
t =0
while tam >= 1 :
    for i in bin:
        d = int(i*2**tam)
        t = t + d
        tam -= 1
        print(e)
        print(tam)
        print(t)