#2) A soma dos valores da terceira coluna

matriz = [[0, 0, 0,], [0, 0, 0], [0, 0, 0]]

soma_coluna = 0

for linhas in range(3):
    for colunas in range(3):
        matriz[linhas][colunas] = int(input(f"Digite o valor que voce deseja colocar nas linha {linhas}, coluna {colunas}: "))

print("-=" * 30)


for L in range(3):
    soma_coluna += matriz[L][2]  

print(f"A soma da terceira coluna é: {soma_coluna}")
print()
