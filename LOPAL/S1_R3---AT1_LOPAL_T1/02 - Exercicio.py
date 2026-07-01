num1 = int(input("Escreva o sue primeiro número: "))
num2 = int(input("Escreva o seu saegundo número: "))
num3 = int(input("Agora escreva o seu terceiro e ultimo número: "))
listagem = [num1, num2, num3]
listagem.sort()
print(listagem)
maior = listagem[2]
menor = listagem[0]
print(f"O seu maior número é: {maior}")
print(f"O seu menor número é: {menor}")

