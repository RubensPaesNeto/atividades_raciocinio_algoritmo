alunos = int(input("Informe um numero inteiro de alunos na sala"))
notas = []
abaixo_media = 0
acima_media = 0
while True:
    if len(notas) == alunos:
        break
    else:
        temp = int(input(f"Digite uma nota para adicionar a lista(maximo permitido {alunos}): "))
        notas.append(temp)

for i in notas:
    if i >= 60:
        acima_media += 1
    else:
        abaixo_media += 1

print(f"Alunos acima ou na média: {acima_media}")
print(f"Alunos abaixo da media {abaixo_media}")