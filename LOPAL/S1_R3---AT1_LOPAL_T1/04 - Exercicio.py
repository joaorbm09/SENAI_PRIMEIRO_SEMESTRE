n = int(input("Até qual termo você quer gerar a série de Fibonacci? "))
a, b = 1, 1
sequencia = []
if n <= 0:
    print("0 não da...")
elif n == 1:
    print("Série de Fibonacci até o 1º termo: [1]")
else:
    count = 0
    while count < n:
        sequencia.append(a)
        a, b = b, a + b
        count += 1
    print(f"Série de Fibonacci até o {n}º termo:")
    print(sequencia)