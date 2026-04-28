numeros = []
par = []
impar = []
somatorio = 0
media = 0
while True:
    if len(numeros) == 5:
        break
    else:
        temp = int(input(f"Digite uma nota para adicionar a lista(maximo permitido: 5): "))
        numeros.append(temp)

for i in numeros:
    if (i % 2) == 0:
        par.append(i)
    else:
        impar.append(i)   

if len(par) == 0:
    print("Nenhum valor par encontrado")
else:
    print(f"Valor maximo par encontrado: {max(par)}")

if len(impar) == 0:
    print("Nenhum valor impar encontrado")
else:
    print(f"Valor minimo impar encontrado: {min(impar)}")

for i in numeros:
    somatorio += i

media = somatorio / 5

print(f"Soma dos numeros: {somatorio}, media dos numeros: {media}")
