from math import *
from sympy import *

# Establece x como simbolo

x = symbols("x")

# Establece y como simbolo

y = symbols("y")

print("Escribe tu ecuacion inicial")

ecuacionInicial = input()

# Convierte la cadena a una expresion

ecuacionInicial = sympify(ecuacionInicial)

print("Escribe tu x0")

equisCero = float(input())

print("Escribe tu y0")

yeCero = float(input())

print("Escribe la x para la cual quieres la solucion")

equisSolucion = float(input())

print("Escribe el ancho de banda h")

h = float(input())

# Se le asigna el valor y0 a yn para iniciar el ciclo

yeEne = yeCero

# Se le asigna el valor x0 a xn para iniciar el ciclo

equisEne = equisCero

# Se crea respaldo de ecuacion inicial para no perderla

respaldoEcuacionInicial = ecuacionInicial

contador = 0

while equisEne < equisSolucion:

    contador = contador + 1

    ecuacionInicial = respaldoEcuacionInicial

    ecuacionInicial = ecuacionInicial.subs(x, equisEne).subs(y, yeEne)

    ecuacionInicial = ecuacionInicial.evalf()

    yeEneMasUno = yeEne + h * ecuacionInicial

    yeEne = yeEneMasUno

    equisEne = equisEne + h

    print(f"Y {contador} es {yeEne}")

print(f"La solucion para tu ecuacion con la x dada es {yeEneMasUno}")    
