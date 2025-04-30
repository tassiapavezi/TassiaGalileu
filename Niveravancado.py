"""Objetivo: Consolidar os conceitos anteriores em um cenário mais voltado para negócios. Usar operadores matemáticos para calcular porcentagens.

Descrição:
Criar um programa que peça ao usuário:

o valor de compra de um produto,

o valor de venda,

e a quantidade vendida.

Depois, calcular:

o lucro por unidade,

o lucro total,

e a porcentagem de lucro sobre o valor de compra."""


valor_de_compra = float(input("digite o valor da compra"))
valor_da_venda = float(input("digite o valor da venda"))
quantidade_vendida = int(input("digitar a quantidade vendida"))

lucro_unitario = valor_da_venda - valor_de_compra
print(f'Lucro unitario: {lucro_unitario}')

Lucro_total = lucro_unitario * quantidade_vendida
print(f'Lucro total {Lucro_total}')

porcenta_lucro_sobre_compra = (valor_da_venda / valor_de_compra)-1
print(F' porcentagem do valor de compra {porcenta_lucro_sobre_compra}')