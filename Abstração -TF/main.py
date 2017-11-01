from classe_alunos import Aluno
from classe_pessoa import Pessoa
from classe_usuario import Usuario
from classe_professor import Professor
from classe_disciplina import Disciplina

aluno1 = Aluno()
aluno1.altera_celular('948715583')

aluno1.altera_senha("123456")

aluno1.altera_email("gabriel_op@hotmail.com")

email_aluno = aluno1.retorna_email()

senha_aluno = aluno1.retorna_senha()

celular_aluno = aluno1.retorna_celular()

print(email_aluno)
print(senha_aluno)
print(celular_aluno)

professor1 = Professor()
professor1.nome = 'Gabriel'

LP2 = Disciplina()
LP2.altera_nome('Linguagem de programação 2')
professor1.adiciona_disciplina(LP2)

LP1 = Disciplina()
LP1.altera_nome('Linguagem de programação 1')
professor1.adiciona_disciplina(LP1)

lista_disciplinas = professor1.disciplinas_professor()


for disciplina in lista_disciplinas:
    print(disciplina.retorna_nome())

disciplina = Disciplina()
disciplina.altera_nome('Linguagem de programação 1')
professor1.remove_disciplina(disciplina)

print(disciplina == LP1)
