# Arquivo principal
#Type Hint é um mecanismo do Python 3 através do qual podemos dar uma dica sobre o tipo de uma variável.
print('***********Inputs do usuário************')

largura: float = float(input('Qual a largura do cômodo? '))
altura: float = float(input('Qual a profundidade do cômodo? '))
profundidade: float = 2.9
area_paredes:float = (2*(largura + profundidade)*altura)
area_teto:float = largura * profundidade
litragem:float = (area_paredes + area_teto) / 10

print("A área das paredes é: ",area_paredes)
print("A área do teto é: ",area_teto)
print("A litragem de tinta necessária é: ",area_teto)



