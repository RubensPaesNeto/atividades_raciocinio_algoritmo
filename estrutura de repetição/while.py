media_turma = 0
soma_das_notas = 0
quantidade_alunos = 0
nota = 0.0

while nota >= 0:
    nota = float(input(f"Digite a nota de aluno: {quantidade_alunos}, digite valor negativo para encerrar"))
    if nota == -1:
        break
    else:
        soma_das_notas += nota
        quantidade_alunos += 1
media_turma = soma_das_notas/quantidade_alunos
print(f"a media da turma é: {media_turma}")