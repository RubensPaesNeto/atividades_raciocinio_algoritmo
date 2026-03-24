rendimento_mensal = float(input("Insira sua renda mensal: "))
numero_dependentes = float(input("Insira seu numero de dependentes: "))
valor_pensao_alimenticia = float(input("Insira o valor de sua pensao: "))
outras_deducoes = float(input("Insira o valor de outras deduções: "))
imposto_pagar = ""

valor_base = rendimento_mensal - ((numero_dependentes * 189.59) + valor_pensao_alimenticia + outras_deducoes)
print(valor_base)

if valor_base <= 1903.98:
    imposto_pagar = "0%"
    print(f"Valor de imposto a pagar: {imposto_pagar};\nFaixa em que se enquadra: Faixa 1;\nTaxa aplicada: 00.00")

elif valor_base <= 2826.65:
    imposto_pagar = "7.5%"
    rendimento_mensal = rendimento_mensal * 0.075
    print(f"Valor de imposto a pagar: {imposto_pagar};\nFaixa em que se enquadra: Faixa 2;\nTaxa aplicada: {round(rendimento_mensal,2)}")

elif valor_base <= 3751.05:
    imposto_pagar = "15%"
    rendimento_mensal = rendimento_mensal * 0.15
    print(f"Valor de imposto a pagar: {imposto_pagar};\nFaixa em que se enquadra: Faixa 3;\nTaxa aplicada: {round(rendimento_mensal,2)}")

elif valor_base <= 4664.68:
    imposto_pagar = "22.5%"
    rendimento_mensal = rendimento_mensal * 0.225
    print(f"Valor de imposto a pagar: {imposto_pagar};\nFaixa em que se enquadra: Faixa 4;\nTaxa aplicada: {round(rendimento_mensal,2)}")

else:
    imposto_pagar = "27.5%"
    rendimento_mensal = rendimento_mensal * 0.275
    print(f"Valor de imposto a pagar: {imposto_pagar};\nFaixa em que se enquadra: Faixa 5;\nTaxa aplicada: {round(rendimento_mensal, 2)}")