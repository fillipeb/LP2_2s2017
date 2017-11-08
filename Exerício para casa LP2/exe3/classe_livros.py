#Gabriel George - 1700824
#Alisson Ferrari - 1700784
#Lucca Marques- 1700726
#Fillipe Borges - 1700135

class Livro:

    def __init__(self, nome, qtdpaginas, autor):
        self.nome = nome
        self.qtdpaginas = qtdpaginas
        self.autor = autor
        self.preco = 0

    
    def  getPreco(self,preco):
        self.preco = preco
        return self.preco

    
    def setPreco(self, novo_valor):
        self.preco = novo_valor
        return self.preco



