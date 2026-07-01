import os 
os.system('cls')
##Exercícios:
    #1) A soma de todos os valores pares da matriz
    


matriz = [[0, 0, 0,], [0, 0, 0], [0, 0, 0]]

for linhas in range(3):
    for colunas in range(3):
        matriz[linhas][colunas] = int(input(f"Digite o valor que voce deseja colocar nas linha {linhas}, coluna {colunas}: "))

soma_pares = 0

for L in range(3):
    for c in range(3):
        print(f"[{matriz[L][c]: ^5}]", end='')
        if matriz[L][c] % 2 == 0:
            soma_pares = soma_pares + matriz[L][c]
            print(f"O número ({matriz[L][c]}) é Par")
        else:
            print(f"O número ({matriz[L][c]}) é impar")
        
    print()
print(soma_pares)







