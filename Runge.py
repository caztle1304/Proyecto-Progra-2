from math import *
from sympy import *

x = symbols("x")

y = symbols("y")

print("Ingresa tu ecuacion inicial")

ecuacionInicial = input()

ecuacionInicial = sympify(ecuacionInicial)

print("Ingresa tu x(0)")

equisCero = float(input())

print("Ingrea tu y(0)")

yeCero = float(input())

print("Escribe la x para la cual quieres la solucion")

equisSolucion = float(input())

print("Ingresa el ancho de tu banda h")

h = float(input())

# Se asignan valores iniciales para entrar en el ciclo while

equisEne = equisCero

yeEne = yeCero

contador = 0

while equisEne < equisSolucion:

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

print(f"La solucion de tu ecuacion en la x dada es {yeEne}")
