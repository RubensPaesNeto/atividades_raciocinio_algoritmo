avaliacao_1 = float(input("Coloque sua nota 1: "))
avaliacao_2 = float(input("Coloque a nota2: "))
media = 6.0
avaliacao_final = 0.0
if (avaliacao_1 + avaliacao_2) >= media:
    print("Voce esta aprovado, parabens!")
elif avaliacao_1 < 1 and avaliacao_2 < 1:
    print("Beee voce esta reprovado!")
else:
    print("Valores informasrdos insuficientes para passar, favor informarmar-me o valor da sua AF")
    avaliacao_final = float(input("Informe a AF: "))
    if avaliacao_1 <= avaliacao_2 and (avaliacao_2 + avaliacao_final) >= media:
        print("Parabens voce esta aprovado")
    elif avaliacao_2 <= avaliacao_1 and (avaliacao_1 + avaliacao_final) >= media:
        print("Parabens voce esta aprovado")
    else:
        print("Voce esta reprovado!")