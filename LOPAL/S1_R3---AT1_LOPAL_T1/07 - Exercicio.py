numero = int(input("Digite um número: "))
fatorial = 1
print(f"{numero}! = ", end="")
for i in range(numero, 0, -1):
    fatorial = fatorial * i
    print(i, end="")
    if i > 1:
        print(" x ", end="")
print(f" = {fatorial}")
