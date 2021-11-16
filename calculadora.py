#Arquivo calculadora

print('*****Orientação a objetos*******')

class Calculadora:
    area_paredes: float
    area_teto: float

    def calcular_area_paredes(self,largura,profundidade,altura):
        self.area_paredes = 2 * (largura + profundidade) * altura
        return self.area_paredes
    def calcular_area_teto(self,largura,profundidade):
        self.area_teto = largura * profundidade
        return self.area_teto




