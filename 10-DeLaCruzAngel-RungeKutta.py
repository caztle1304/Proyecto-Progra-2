'''NAME
        10-DeLaCruzAngel-RungeKutta.py
VERSION
        1.0
AUTHOR
        Angel Adrian De la Cruz Castillo <angeldc@lcg.unam.mx>
DESCRIPTION
      Programa que calcula soluciones de ecuaciones diferenciales usando el metodo de Runge-Kutta
CATEGORY
       Calculadora de soluciones de ecuaciones diferenciales
USAGE
        EL usuario ingresa su ecuacion inicial despejada en terminos dy/dx, x0, y0, la X solucion y el ancho de las bandas a utilizar
ARGUMENTS
  N/A
DICCIONARIO DE VARIABLES
ecuacionInicial: ecuacion introducida por el usuario a partir de la cual se va a calcular la solucion
equisCero: X inicial que se tiene en la ecuacion
yeCero: Y inicial que se tiene en la ecuacion
equisSolucion: X para la cual se quiere conocer el valor de Y
h: ancho de las bandas a usar para calcular la solucion
equisEne: Xn usada para calcular la apriximacion de Yn+1
yeEne: Aproximacion Yn de la solucion final
contador: contador usado para imprimir la aproximacion de Yn
contador2: contador usado para determinar el numero de veces que se repetira un ciclo 
k1: valor a sustituir en la formula final de la aprixmacion de Y
k2: valor a sustituir en la formula final de la aproximacion de Y
k3: valor a sustituir en la formula final de la aproximacion de Y
k4: valor a sustituir en la formula final de la aproximacion de Y
sustitucionX: valor a sustituir en X en f(x,y) segun corresponda en kn
sustitucionY: valor a sustituir en Y en f(x,y) segun corresponda en kn


'''
from math import *
from sympy import *
from decimal import *

x = symbols("x")

y = symbols("y")

print("Este programa calcula soluciones de ecuaciones diferenciales usando metodo de Runge-Kutta\n")

print("Ingresa tu ecuacion inicial en el formato dy/dx = ecuacion")

ecuacionInicial = input()

ecuacionInicial = sympify(ecuacionInicial)

print("Ingresa tu x(0)")

equisCero = input()

equisCero = Decimal(equisCero)

print("Ingresa tu y(0)")

yeCero = input()

yeCero = sympify(yeCero)

print("Escribe la x para la cual quieres la solucion")

equisSolucion = input()

equisSolucion = Decimal(equisSolucion)

print("Ingresa el ancho de tu banda h")

h = input()

h = Decimal(h)

# Se asignan valores iniciales para entrar en el ciclo while

equisEne = sympify(equisCero)

yeEne = yeCero

contador = 0

# Se aplica la formula dentro del range para determinar el numero de veces que es necesario repetir el ciclo for 

repeticiones = int(((equisSolucion - equisCero)/h))

for contador2 in range(1, repeticiones + 1):

    contador = contador + 1

    print(f"para Y {contador}\n")

    # Asigna valor de k1

    k1 = ecuacionInicial.subs(x, equisEne).subs(y, yeEne)

    k1 = k1.evalf()

    k1 = h * k1

    print(f"k1 es {k1}")

    # Valores a sustituir en X y Y para k2

    sustitucionX = equisEne + (h / 2)

    sustitucionY = yeEne + (k1 / 2) 

    # Se asigna valor a k2

    k2 = ecuacionInicial.subs(x, sustitucionX).subs(y, sustitucionY)

    k2 = k2.evalf()

    k2 = h * k2

    print(f"k2 es {k2}")

    # Cambia el valor a sustiuir en y en k3

    sustitucionY = yeEne + (k2 / 2)

    # Se asigna valor a k3

    k3 = ecuacionInicial.subs(x, sustitucionX).subs(y, sustitucionY)

    k3 = k3.evalf()

    k3 = h * k3

    print(f"k3 es {k3}")

    # Cambian valores a sustituir en X y Y en k4

    sustitucionX = equisEne + h

    sustitucionY = yeEne + k3

    # Se asigna valor a k4

    k4 = ecuacionInicial.subs(x, sustitucionX).subs(y, sustitucionY)

    k4 = k4.evalf()

    k4 = h * k4

    print(f"k4 es {k4}")

    # Se sustituyen valores en la formula para yn+1

    yeEneMasUno = yeEne + (1/6) * (k1 + (2 * k2) + (2 * k3) + k4)

    yeEne = yeEneMasUno

    print(f"Y {contador} es {yeEne}")

    print("\n" + "\n")

    equisEne = equisEne + h

    equisEne = equisEne.evalf()

print(f"La solucion de tu ecuacion en la x dada es {yeEne.evalf()}")
