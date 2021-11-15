# Arquivo principal
#Type Hint é um mecanismo do Python 3 através do qual podemos dar uma dica sobre o tipo de uma variável.
print('***********Inputs do usuário************')

from calculadora import Calculadora
calc = Calculadora()

largura: float = float(input('Qual a largura do cômodo? '))
altura: float = float(input('Qual a profundidade do cômodo? '))
profundidade: float = 2.9

calc.area_paredes:float = (2*(largura + profundidade)*altura)
calc.area_teto:float = largura * profundidade
litragem:float = (area_paredes + area_teto) / 10

print("A área das paredes é: ",calc.area_paredes)
print("A área do teto é: ",calc.area_teto)
print("A litragem de tinta necessária é: ",area_teto)



