#estou criando um variavel chamada nome e elea recebera um dado do tipo texto 
# utilizando o metodo "Input".

variavel_nome= input("digite o seu nome: ")
#pedimos para o ususario, informar o nome dele e logo em seguida esse nome sera 
# arazenado na variavel nome.
print(f"o nome armazenado na variavel_nome e {variavel_nome}")
#colocar para rodar e ver o que da.
#Coloquei meu nome na parte de baixo porque o codigo e executado  na parte de baixo e criado 
#na parte de cima.
#Mudamos o codigo e colocamos um f" na frente e ao inves de print(variavel nome) ficou:
#print(f"o nome armazenado na variavel_nome e {variavel_nome}")
#f" ajuda a formatar o texto impresso na funcao "print"
# { = chave. Qdo coloco chaves dentro de um print eu estou chamando o valor que tem dentro 
# da variavel "nome"

variavel_sobrenome= input("digite o seu sobrenome: ")
print(f"o nome armazenado na variavel_sobrenome e {variavel_sobrenome}")
#logo a variavel completa sera Nome + sobrenome e o codigo sera.

print(f"o nome completo e: {variavel_nome} {variavel_sobrenome}")