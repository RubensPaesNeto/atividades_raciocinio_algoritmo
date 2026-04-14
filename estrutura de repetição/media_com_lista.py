lista = list(input("insira numero para a lista: ").split())
soma = 0
for i in lista:
    soma += float(i)
print(f"Sua media é: {soma/4}")