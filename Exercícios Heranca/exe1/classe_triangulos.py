#Gabriel George - 1700824
#Alisson Ferrari - 1700784
#Lucca Marques- 1700726
#Fillipe Borges - 1700135

class Triangulo:

    def __init__(self, ladoa, ladob, ladoc):
            self.ladoa = ladoa
            self.ladob = ladob
            self.ladoc = ladoc

    def calcular_perimetro(self):
        perimetro = self.ladoa + self.ladob + self.ladoc
        return perimetro

    def getMaior(self):
        maior = self.ladoa
        if (self.ladob > maior):
            maior = self.ladob
        if(self.ladoc > maior):
            maior = self.ladoc
        return maior


    
