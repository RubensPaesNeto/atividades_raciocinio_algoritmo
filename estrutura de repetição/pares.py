numero_limite = int(input("Insira um valor inteiro: "))
soma = 0
i = 0
while i <= numero_limite:
    if i % 2 == 0:
        soma += i
    i += 1
print(f"A soma dos pares até {numero_limite}, é igual à {soma}")