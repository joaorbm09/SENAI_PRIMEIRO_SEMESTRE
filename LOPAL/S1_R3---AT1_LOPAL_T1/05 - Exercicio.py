nome = input("Escreva seu nome: ")
while len(nome) <= 3:
    nome = input("Seu nome é curto, escreva denovo: ")
idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:
    idade = int(input("Sua idade está acima ou abaixo do esperado, digite novamente a sua idade: "))
salario = float(input("Escreva seu salário: "))
while salario <= 0:
    salario = float(input("Seu salário não será validado, tente novamente: "))
sexo = input("Escreva seu sexo, (por ex: 'f' para feminino, 'm' para masculino): ").lower()
while sexo != "f" and sexo != "m":
    sexo = input("Escreva seu sexo novamente, (por ex: 'f' para feminino, 'm' para masculino): ").lower()
estado_civil = input("Escreva seu estado civil(por ex: 's' de solteiro, 'c' de casado, 'v' de viuvo, 'd' de divorciado):").lower()
while estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d":
    estado_civil = input("Escreva seu estado civil novamente(por ex: 's' de solteiro, 'c' de casado, 'v' de viuvo, 'd' de divorciado").lower()
print("Seu cadastro ficou completo segue as informações abaixo para você verificalos (caso não esteja certo as suas informações, refaça o seu cadastro):")
print(f"Seu nome foi validado: {nome}")
print(f"Sua idade foi validada: {idade}")
print(f"Seu salário foi validado: {salario}")
print(f"Seu sexo foi validado: {sexo}")
print(f"Seu estado civil foi validado: {estado_civil}")


