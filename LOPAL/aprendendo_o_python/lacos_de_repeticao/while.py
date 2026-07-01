#uso do continue
count = 0
while count <= 5:
  print(f"Valor do contador é: {count}")
  # count += 1
  count = count + 1

  # print("O contador ainda é menor que 10. Incrmentando... ")
  # continue#ele serve para caso a linha de cima não funcione ele lera a parte de baixo para isso mas quando a linha de cima estiver funcionando ele apenas ira ignorar a linha abaixo e continuara o codigo que esta acima



#uso do break
count = 0
while count < 10:
  print(f"O valor do contador é: {count}")
  count += 1
  break
  print("o contador ainda é menor que 10")
print(f"o valor do count terminou em {count}")
print(f"o loop terminou por causa do break ")