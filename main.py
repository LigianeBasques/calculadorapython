# Arquivo principal
#Type Hint é um mecanismo do Python 3 através do qual podemos dar uma dica sobre o tipo de uma variável.
print('***********Inputs do usuário************')
from calculadora import Calculadora
from comodo import Comodo
calc = Calculadora()

#largura: float = float(input('Qual a largura do cômodo? '))
#profundidade: float = float(input('Qual a profundidade do cômodo? '))


comodo = Comodo(input('Qual a largura do comodo? '),input('Qual a profundidade do comodo? '))


print("A área das paredes é: ",calc.calcular_area_paredes(comodo.largura, comodo.profundidade, comodo.altura))
print("A área do teto é: ",calc.calcular_area_teto(comodo.largura,comodo.profundidade))
print("A litragem de tinta necessária é: ",calc.calcular_litragem_necessaria())





