#verifica se eu posso dirigir.
#caso a minha idade seja maior do que 18 printa eu "posso dirigir" 
#se for menos eu "nao posso dirigir"

#Dicas
# critar variavel idade
# O usuario informa a idade
#aplique condicional para verificar a idade.
#caso a minha idade seja maior do que 18 printa eu "posso dirigir" 
#se for menos eu "nao posso dirigir"

Informe_a_idade = int(input ("digite a sua idade: "))
print(Informe_a_idade > 18)
if Informe_a_idade > 18: 
    print("posso_dirigir")


else: 
    print("nao posso dirigir")