a = []
while True:
    temp = int(input("Digite um numero para adicionar a lista(maximo permitido 10): "))
    if len(a) == 10:
        break
    else:
        a.append(temp)

print(f"Valor minimo {min(a)}")
print(f"Valor maximo {max(a)}")