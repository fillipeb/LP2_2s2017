class Disciplina:
    def __init__(self):
        self.nome = ''
        self.carga_horaria = 0
        self.teoria = 0
        self.pratica = 0
        self.ementa = ''
        self. competencias = ''
        self. habilidades = ''
        self.conteudo = ''
        self. bibliografia_basica = ''
        self. bibliografia_complementar = ''


    def altera_nome(self, nome):
        if type(nome) == str:
            self.nome = nome
            return True
        return False


    def retorna_nome(self):
        return self.nome