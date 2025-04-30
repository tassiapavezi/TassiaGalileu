"""Objetivo: Trabalhar com múltiplas variáveis, entrada do usuário, soma, divisão e concatenação de texto com print().

Descrição:
O aluno deve criar um programa que receba 3 notas de um aluno, calcule a média e mostre se ele foi aprovado ou reprovado 
(média mínima 7)."""

prova1 = int(input("digite a nota 1: "))
prova2 = int(input("digite a nota 2: "))
prova3 = int(input("digite a nota 3: "))

soma_das_notas =(prova1 + prova2 + prova3)

media=soma_das_notas/3

print(f'a media das notas e {media}')

#if or else para saber se ele foi aprovado ou nao

if media > 7: 
    print("Aprovado")
else:
    print("Reprovado")