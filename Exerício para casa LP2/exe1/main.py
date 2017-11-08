#Gabriel George - 1700824
#Alisson Ferrari - 1700784
#Lucca Marques- 1700726
#Fillipe Borges - 1700135

from classe_triangulos import Triangulo
import math

t1 =int(input("Digite o tamanho do 1º lado: "))
t2=int(input("Digite o tamanho do 2º lado: "))
t3=int(input("Digite o tamanho do 3º lado: "))
triangulo1 = Triangulo(t1,t2,t3)

semi_perimetro = (triangulo1.calcular_perimetro())/2
t1 = triangulo1.ladoa
t2 = triangulo1.ladob
t3 = triangulo1.ladoc
heron = (semi_perimetro*(semi_perimetro-a)*(semi_perimetro-b)*(semi_perimetro-c))
heron = math.sqrt(heron)

# Esse print mostra a área.Tendo o perímetro em mãos, foi utilizado a fórmula de Heron 
# para o cálculo da área.
print(heron)

maiorlado = instancia.pega_maior()

# Esse print mostra o maior lado
print(maiorlado)


