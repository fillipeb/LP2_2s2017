from classe_pessoa import Pessoa
from classe_usuario import Usuario

class Professor (Pessoa, Usuario):
    def __init__(self):
        self.apelido = ''
        self.disciplinas = []


    def adiciona_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)


    def remove_disciplina(self, disciplina):
        for d in self.disciplinas:
            if d.retorna_nome() == disciplina.retorna_nome():
                self.disciplinas.remove(d)
                break
        


    def disciplinas_professor(self):
        return self.disciplinas    