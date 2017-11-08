#Gabriel George - 1700824
#Alisson Ferrari - 1700784
#Lucca Marques- 1700726
#Fillipe Borges - 1700135

class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario


    def aumentarSalario(self, porcentagem):
        aumento = ((porcentagem/100)*self.salario) + self.salario
        return aumento

