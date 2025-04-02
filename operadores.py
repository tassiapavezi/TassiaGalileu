#vamos criar 2 variaveis, a variavel numero 1 e variavel numero 2.
#elas irao receber o numero informado pelo usuario do sistema, logo, devemos utilizar "imput"

variavel_numero_1 = input ("digite o primeiro numero:")
variavel_numero_2 = input ("digite o segundo numero:")

#vamos realizar a operacao de soma.

print(variavel_numero_1 + variavel_numero_2)
#isso da errado pq ele concatenou (juntou a 1 com a 2 ao invez de somar)
# + e igual juntar pq ele esta entendendo como texto por causa das "
# como concertar

variavel_numero_1 = int(input ("digite o primeiro numero:"))
variavel_numero_2 = int(input ("digite o segundo numero:"))

#int para poder rodar numeros e tem que colocar sempre entre parenteses 
# e 2 parenteses no final.

print (variavel_numero_1 + variavel_numero_2)

#nao precisa colocar int qdo solicitar a soma.

print(f'a soma dos dois numeros e d: {variavel_numero_1 + variavel_numero_2}')