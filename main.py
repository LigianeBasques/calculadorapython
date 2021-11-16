# Arquivo principal
#Type Hint é um mecanismo do Python 3 através do qual podemos dar uma dica sobre o tipo de uma variável.
print('***********Inputs do usuário************')

from calculadora import Calculadora
calc = Calculadora()

largura: float = float(input('Qual a largura do cômodo? '))
altura: float = float(input('Qual a profundidade do cômodo? '))
profundidade: float = 2.9


print("A área das paredes é: ",calc.calcular_area_paredes(largura,profundidade,altura))
calc.area_teto:float = largura * profundidade
print("A área do teto é: ",calcular_area_teto())
print("A litragem de tinta necessária é: ",(calc.area_paredes + calc.area_teto)/10)





