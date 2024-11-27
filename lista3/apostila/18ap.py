S = 0
x = float(input("Informe o valor do primeiro número: "))
y = float(input("Informe o valor do segundo número: "))
op = input("Qual o símbolo da operação básica? ")
if op == "+":
    S = x + y
elif op == "-":
    S = x - y
elif op == "*":
    S = x * y
elif op == "/":
    S = x / y
print("O valor de S = {}".format(S))
