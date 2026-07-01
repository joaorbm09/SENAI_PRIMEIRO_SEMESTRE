#3) Imprima o maior valor da segunda linha
matriz = [[0, 0, 0,], [0, 0, 0], [0, 0, 0]]

for linhas in range(3):
    for colunas in range(3):
        matriz[linhas][colunas] = int(input(f"Digite o valor que voce deseja colocar nas linha {linhas}, coluna {colunas}: "))

print("-=" * 30)


maior_valor = max(matriz[1])

print(f"o maior valor da segunda coluna é: {maior_valor}")
print()