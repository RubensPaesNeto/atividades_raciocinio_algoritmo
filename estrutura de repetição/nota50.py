import random
media_geral = 0 
contador = 0
while contador <= 50:
    nota1 = random.randint(1,10)
    nota2 = random.randint(1,10)
    nota3 = random.randint(1,10)
    nota4 = random.randint(1,10)
    media_aluno = (nota1 + nota2 + nota3 + nota4) / 4
    media_geral += media_aluno
    if media_aluno >= 7.0:
        print(f"Parabens aluno aprovado com média de: {media_aluno}")
    else:
        print(f"Aluno Reprovado com media de {media_aluno}")
    contador += 1
print(f"media geral da turma: {media_geral/50}")

