#dicionario

from pprint import pprint
meu_dicionario = {"nome":"joao", "sobrenome":"santos", "idade":30, "peso": 80.5, "filhos":["maria", "josefina"]}

meu_dicionario['sobrenome'] = 'souza'#fazedo deste forma voce consegue recriar algo que ja foi criado neste caso mudamos o sobrenome mas se aplica aos outros também.
meu_dicionario['cidade']= "Santa Bábara d' Oeste" #aqui nós adicionamos mais um item a lista podendo apenas chamar o dicionario ou criar um print desejado
meu_dicionario['dado_aleatório'] = {'a':1, 'b':2, 'c':3}

#pprint(meu_dicionario)#aqui chamamos todo o dicionario
#pprint(meu_dicionario.keys())#aqui chamamos apenas as chaves
#pprint(meu_dicionario.values())#ja aqui chamamos apenas os valores
# pprint(meu_dicionario.items())#aqui vamos imprimir o conjunto chave e valor dentro do parenteses (dupla)
print(meu_dicionario["nome"])
print(meu_dicionario["sobrenome"])
print(meu_dicionario["idade"])
print(meu_dicionario["peso"])
print(meu_dicionario["filhos"])
print(meu_dicionario["cidade"])