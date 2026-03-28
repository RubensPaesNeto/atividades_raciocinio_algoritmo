"""Faça um Programa que pergunte quanto você ganha 
por hora e o número de horas trabalhadas no mês. Calcule e
mostre o total do seu salário no referido mês."""
horas = float(input("numero de horas trabalhados no mes: "))
valor_hora = float(input("Valor por Hora"))
print(f"Seu salrio é de: {horas * valor_hora}")