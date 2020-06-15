'''NAME
        7-DeLaCruzAngel-Simpson.py
VERSION
        1.0
AUTHOR
        Angel Adrian De la Cruz Castillo <angeldc@lcg.unam.mx>
DESCRIPTION
      Programa que calcula area bajo la curva usando metodo de Simpson
CATEGORY
       Calculadora de area bajo la curva
USAGE
       Usuario ingresa su funcion, los limites superior e inferior y el numero de bandas a usar para el calculo del area
ARGUMENTS
  N/A
DICCIONARIO DE VARIABLES
ecuacionInicial: funcion a partir de la cual se calcula area bajo la curva
limInferior: limite inferior del intervalo a obtener el area
limSuperior: limte superior del intervalo a obtener el area
bandas: numero de bandas (subintervalos) a usar para calcular el area
h: tamano de subintervalo
fDeEquis: diccionario de posiciones de X asociados a su f(x)
contador: variable contadora auxiliar en ciclos
acumulador: variable contadora auxiliar en aumentos decimales que no pueden ser implementados en un ciclo
acumulador4: variable que acumula los valores resultantes de multiplicar por 4 los valores de f(x) correspondientes
acumulador2: variable que acumula los valores resultantes de multiplicar por 2 los valores de f(x) correspondientes
yeCero: resultado de evaluar funcion en x0, es decir en el limite inferior
yeEne: resultado de evaluar funcion en xn, es decir en el limte superior
area: resultado de sustituir todos los datos obtenidos en la formula de Simpson


'''

from sympy import *
from math import *

# Se establece x como simbolo

x = symbols("x")

print("Este programa calcula area bajo una curva usando metodo de Simpson\n")

print("Ingresa tu ecuacion inicial")

ecuacionInicial = input()

# Convierte cadena a una expresion

ecuacionInicial = sympify(ecuacionInicial)

print("Ingresa el limite inferior del intervalo a evaluar")

limInferior = input()
limInferior = sympify(limInferior)

print("Ingresa el limite superior del intervalo a evaluar")

limSuperior = input()
limSuperior = sympify(limSuperior)


print("Ingresa el numero de bandas que quieres usar")

bandas = int(input())

# Se asigna el intervalo que aumentara en cada cambio de x

h = (limSuperior - limInferior) / bandas

# Se crea diccionario vacio de x asociados a su f(x)

fDeEquis = {}

# Se inicia el acumulador al limite inferior para empezar la sustitucion de valores desde ahi

acumulador = limInferior

'''
Se anaden valores de f(x) asociados a x, se exluyen x0 y xn
para que no se multiplique por 4 o por 2 al hacer la multiplicacion de la formula
'''

for contador in range(bandas-1):

    acumulador = acumulador + h
    fDeEquis[contador] = ecuacionInicial.subs(x, acumulador)
    fDeEquis[contador] = fDeEquis[contador].evalf()


acumulador4 = 0
acumulador2 = 0

'''
En el acumulador 4 se guarda el resultado de multiplicar por 4
las f(x) correspondientes.
En el acumulador 2 se hace lo mismo que con el 2 pero multiplicando
por 2 en lugar de por 4
'''

for contador in range(0, bandas-1, 2):

    acumulador4 =  acumulador4 + (4 * fDeEquis[contador])
    
for contador in range(1, bandas-1, 2):

    acumulador2 = acumulador2 + (2 * fDeEquis[contador])

# Se evalua la funcion en x0    

yeCero = ecuacionInicial.subs(x, limInferior)

yeCero = yeCero.evalf()

# Se evalua la funcion en xn

yeEne = ecuacionInicial.subs(x, limSuperior)

yeEne = yeEne.evalf()

#Se sustituye los valores obtenidos en la formula

area = (h/3) * (yeCero + acumulador2 + acumulador4 + yeEne)


print(f"El area bajo la curva en  los intervalos dados es {area.evalf()}")
