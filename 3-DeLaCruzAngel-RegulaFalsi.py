'''NAME
        3-DeLaCruzAngel-RegulaFalsi.py
VERSION
        1.0
AUTHOR
        Angel Adrian De la Cruz Castillo <angeldc@lcg.unam.mx>
DESCRIPTION
      Programa que calcula raices de ecuaciones usando el metodo de regula falsi
CATEGORY
       Calculadora de raices de ecuaciones
USAGE
        EL usuario ingresa su ecuacion inicial, el despeje deseado, los intervalos a evaluar y el step de incremento en la evaluacion de la funcion
ARGUMENTS
  N/A
DICCIONARIO DE VARIABLES
ecuacionInicial: Ecuacion de la cual se obtendra la raiz deseada
limInferior: Limite inferior del intervalo a evaluar
limSuperior: Limite superior del intervalo a evaluar
step: paso de incremento en la evaluacion de la funcion
numDecimales: Numero de decimales de exactitud que el usuario requiere
fDeEquis: diccionario donde se guardan las X y sus f(x)
contador: contador auxiliar en los ciclos
posicionAnterior: Guarda f(x) en la posicion xn
posicion: Guarda f(x) en la posicion xn+1
a: limite inferior del intervalo
b: limite superior del intervalo
efeDeA: funcion evaluada en a
efeDeB: funcion evaluada en b
equisCero: Aproximacion inicial de la raiz
efeDeEquisCero: funcion evaluada en la aproximacion inicial
k: pivote de la funcion
efeDeK: Funcion evaluada en el pivote
equisEne: aproximacion de Xn
equisEneMasUno: aproximacion de Xn+1
'''  

from sympy import *
from math import *

# Se establece x como simbolo

x = symbols("x")

print("Este programa encuentra raices de ecuaciones en intervalos dados usando el metodo de regula falsi\n")

print("Escribe tu ecuacion inicial")
ecuacionInicial = input()

# Convierte cadena a una expresion

ecuacionInicial = sympify(ecuacionInicial)


print("Escribe el limite inferior del intervalo a evaluar")
limInferior = input()
limInferior = sympify(limInferior)

print("Escribe el limite superior del intervalo a evaluar")
limSuperior = input()
limSuperior = sympify(limSuperior)

print("Escribe el paso de incremento para evaluar tu funcion")
step = input()
step = sympify(step)

print("Escribe el numero de decimales de exactitud que requieres")
numDecimales = int(input())

fDeEquis = {}

'''
Crea diccionario de valores de y asociados a x,
se evalua la funcion en el intervalo dado
'''
contador = limInferior

while contador < (limSuperior + step):
    
    fDeEquis[contador] = ecuacionInicial.subs(x, contador)
    fDeEquis[contador] = fDeEquis[contador].evalf()
    contador = contador + step


# Se inicializa posicion anterior para que el primer valor del array pueda ser compardo con algo

posicionAnterior = limInferior

for posicion in fDeEquis:
   
    # Si se detecta cambio de signo en f(x), a y b son asignados y el ciclo se rompe

    if (fDeEquis[posicionAnterior] < 0 and fDeEquis[posicion] > 0) or (fDeEquis[posicionAnterior] > 0 and fDeEquis[posicion] < 0): 

        a = posicionAnterior

        b = posicion

        break

    posicionAnterior = posicion


# Se obtiene f(a)

efeDeA = ecuacionInicial.subs(x, a)

efeDeA = efeDeA.evalf()

# Se obtiene f(b)

efeDeB = ecuacionInicial.subs(x, b)

efeDeB = efeDeB.evalf()

# Se sustituye la formula para sacar la aproximacion inicial

equisCero = ((a * efeDeB) - (b * efeDeA)) / (efeDeB - efeDeA)

efeDeEquisCero = ecuacionInicial.subs(x, equisCero)

efeDeEquisCero = efeDeEquisCero.evalf()

# Se aplican los criterios de abajo para asignar k

if efeDeA * efeDeEquisCero < 0:
   
   k = limInferior

if efeDeB * efeDeEquisCero < 0:
    
    k = limSuperior

# Se obtiene f(k)

efeDeK = ecuacionInicial.subs(x, k)

efeDeK = efeDeK.evalf()

# Se hace la primera iteracion fuera del ciclo para asignar valores iniciales

equisEneMasUno = ((equisCero * efeDeK) - (k * efeDeEquisCero)) / (efeDeK - efeDeEquisCero)

equisEne = equisCero
 
# Se hace el ciclo sustituyendo en la formula hasta obtener la precision deseada

while (round(equisEne, numDecimales)) != (round(equisEneMasUno, numDecimales)):

    equisEne = equisEneMasUno

    efeDeEquisEne = ecuacionInicial.subs(x, equisEne)

    efeDeEquisEne = efeDeEquisEne.evalf()

    efeDeK = ecuacionInicial.subs(x, k)

    efeDeK = efeDeK.evalf()

    equisEneMasUno = ((equisEne * efeDeK) - (k * efeDeEquisEne)) / (efeDeK - efeDeEquisEne)

print(f"La raiz de tu ecuacion en el intervalo dado es {round(equisEne, numDecimales)}")
