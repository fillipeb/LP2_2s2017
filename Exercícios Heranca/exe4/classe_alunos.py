#Gabriel George - 1700824
#Alisson Ferrari - 1700784
#Lucca Marques- 1700726
#Fillipe Borges - 1700135


class Aluno:

    def __init__(self, nome, curso, temposemdormir):
        self.nome = nome
        self.curso = curso
        self.temposemdormir = temposemdormir


    def estudar(self, horas_de_estudos):
        resultado = horas_de_estudos + self.temposemdormir
        return resultado

    def dormir(self, qtd_horas_sono):
        resultado = qtd_horas_sono - self.temposemdormir
        return resultado
    
