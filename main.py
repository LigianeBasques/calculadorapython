# Arquivo principal
#Type Hint é um mecanismo do Python 3 através do qual podemos dar uma dica sobre o tipo de uma variável.
print('***********Calculo da área das paredes de um cômodo************')

largura: float = float(input('Qual a largura do cômodo? '))
altura: float = float(input('Qual a profundidade do cômodo? '))
profundidade: float = 2.9

print((2*(largura + profundidade)*altura))


