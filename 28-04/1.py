#1
a = []
while True:
    temp = int(input("Digite um numero para adicionar a lista: "))
    if len(a) == 10:
        break
    else:
        a.append(temp)

#2
for i in a:
    print(i)
