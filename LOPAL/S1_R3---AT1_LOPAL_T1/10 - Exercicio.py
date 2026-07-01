senha = int(input("Digite a senha: "))
while senha != 676767:
    print("Senha incorreta, tente novamente.")
    senha = int(input("Digite a senha: "))
if senha == 676767:
    print("Acesso liberado")
else:
    print("Limite de tentativas atingido. Tente novamente mais tarde")