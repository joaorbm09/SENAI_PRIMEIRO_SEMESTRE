def soma(x,y):
    total = x + y
    print(total)

total = 10

soma(6,7)

print(f"Total do codigo principal {total}")

'''
nestes escopos mostra dois tipos o global e o local, quando a variavel fica dentro de uma função é global, ja quando esta fora ela é global
'''

def soma(x,y):
    global total 
    total = x + y
    print(total)

soma(6,7)

total = 10

print(f"Total do codigo principal {total}")

'''
neste caso aqui estamos permitindo que tenha um escopo global dentro da função, com o comando "global"
'''

def soma(x,y):
    global total 
    total = x + y
    print(total)

soma(6,7)

print(f"Total do codigo principal {total}")
'''
aqui fazemos a mesma coisa só que estamos permitindo que as variaveis se conversem, e como as variaveis são globais podemos atualiza-las
'''
