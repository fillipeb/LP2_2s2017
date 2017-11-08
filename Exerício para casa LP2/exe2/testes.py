#Gabriel George - 1700824
#Alisson Ferrari - 1700784
#Lucca Marques- 1700726
#Fillipe Borges - 1700135

from funcionarios import Funcionario

harry = Funcionario('Harry',  25000)

def test_ex02():
  print ('Teste da classe Funcionario')
  assert harry.aumentarSalario(10) == (27500.0)
