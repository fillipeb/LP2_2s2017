from classe_alunos import Aluno
from classe_disciplina import Disciplina

class Matricula:
    def __init__(self):
        self.aluno = ''
        self.disciplina = ''
        self.data_matricula = ''
        self.data_cancelamento = ''
        self.data_confirmacao = ''

    def altera_aluno(self, aluno):
        if type(aluno = Aluno):
            self.aluno = aluno
            return True
        return False

    def altera_disciplina(self, disciplina):
        if type (disciplina) == Disciplina:
            self.disciplina = disciplina
            return True
        return False


