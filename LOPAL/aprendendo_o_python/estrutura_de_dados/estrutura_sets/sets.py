x = set()
x.add(1)
x.add(2)
x.add(4)
x.add(3)
x.add(7)
x.add(8)
x.add(9)
l = [1, 2, 3, 4 , 4, 4, 5 , 5, 5, 5]
l1 = set(l)
print(x)#neste caso ele listara em ordem crescente
print(l1)#aqui o set mostrara apenas o padrao que não se repetirá
print(x.union(l1))#aqui faz a uniao das listas
print(x.intersection(l1))#ele só vai deixar apenas o que as lsita tem
