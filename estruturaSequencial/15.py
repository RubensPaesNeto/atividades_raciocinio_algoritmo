horas_trabalhadas = int(input("Informe as horas trabalhadas: "))
valor_hora = float(input("Valor por Hora: "))
salario_bruto = horas_trabalhadas * valor_hora
inss = salario_bruto * 0.08
imposto = salario_bruto * 0.11
sindicado = salario_bruto * 0.05
salario_liquido = salario_bruto - (inss + imposto + sindicado)

print(f"""Salário Bruto : R$ {salario_bruto}
IR (11%) : R$ {imposto}
INSS (8%) : R$ {inss}
Sindicato ( 5%) : R$ {sindicado}
Salário Liquido : R$ {salario_liquido}""")