print("-------Digite 'sair' para encerrar o programa--------")

nome =input('Digite o seu nome completo : ')
if nome=='sair':
    exit()
mail =input('Digite o seu email : ')
if mail=='sair':
    exit()
tlm = input('Digite o seu número telefone : ')
if tlm=='sair':
    exit()
bnc = input('Digite seu endereço :')
if bnc=='sair':
    exit()
print("----------------------------------------")
d1={'Nome':nome,}
d2={'Email':mail,}
d3={'Telefone':tlm,}
d4={'Endereço':bnc}
print(d1,d2,d3,d4)
print("----------------------------------------")
pesquisa=input("Pesquise pelo nome para saber os dados:")
if pesquisa=='sair':
    exit()
if (pesquisa==nome):
  valor1=d1.values()
  valor2=d2.values()
  valor3=d3.values()
  valor4=d4.values()
 print(valor1,valor2,valor3,valor4)
else:
  print("Nome não encontrado")
print("----------------------------------------")
delete=input("Deseja remover ?insira o nome :")
if delete=='sair':
    exit()
if (delete==nome):
  d1.clear()
  print(d1)
else:
  print("Nome não encontrado")