numero = int(input("Insira seu número: "))
numero += 1
multiplicacao = 1
for i in range(1,numero):
    multiplicacao *= i
print(f"O fatorial é: {multiplicacao}")
