L = [5, 7, 2, 9, 4, 1, 3]
print(L)

tamanho = len(L)
print(f"O tamanho da sua lista é: {tamanho}")

maior = max(L)
menor = min(L)
print(f"O seu maior número é: {maior}")
print(f"O seu menor número é: {menor}")

soma = sum(L)
print(f"A soma da sua lista é: {soma}")

L.sort()
print(f"Sua lista fica de forma crescente: {L}")

L.reverse()
print(f"Sua lista fica de forma decrescente: {L}")


