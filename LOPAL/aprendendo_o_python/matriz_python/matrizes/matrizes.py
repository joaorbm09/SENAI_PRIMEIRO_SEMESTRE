import os
os.system('cls')

matriz = [[0, 0, 0,], [0, 0, 0], [0, 0, 0]]

for linhas in range(3):
    for colunas in range(3):
        matriz[linhas][colunas] = int(input(f"Digite o valor que voce deseja colocar nas linha {linhas}, coluna {colunas}: "))

print("-=" * 30)

for l in range(3):
    for c in range(3):
        print(f"[{matriz[l][c]: ^5}]", end='')
    print()










