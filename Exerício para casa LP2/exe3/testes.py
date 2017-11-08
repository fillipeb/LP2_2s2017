#Gabriel George - 1700824
#Alisson Ferrari - 1700784
#Lucca Marques- 1700726
#Fillipe Borges - 1700135

from livros import Livro


instancia = Livro('Vidas Secas', 300, 'Graciliano Ramos')

def test_ex02():
  print ('Teste da classe Livro')
  assert instancia.getPreco('50') == ('50')
  assert instancia.setPreco('90') == ('90')
