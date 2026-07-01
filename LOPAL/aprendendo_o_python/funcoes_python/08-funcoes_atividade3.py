def lista():
    n = [
         float(input("digite a primeira nota: ")), 
         float(input("digite a primeira nota: ")), 
         float(input("digite a primeira nota: ")),
    ]
    for i, lista in enumerate(n):
        print(f"indice{i}: {lista}")

    soma = sum(n)
    media = soma / len(n)

    print(f"Soma das notas: {soma}")
    print(f"Media das notas: {media}")
    
lista()