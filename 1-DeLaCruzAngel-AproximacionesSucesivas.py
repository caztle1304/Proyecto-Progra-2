'''NAME
        1-DeLaCruzAngel-AproximacionesSucesivas.py
VERSION
        1.0
AUTHOR
        Angel Adrian De la Cruz Castillo <angeldc@lcg.unam.mx>
DESCRIPTION
      Programa que calcula raíces de ecuaciones usando el metodo de aproximaciones sucesivas
CATEGORY
       Calculadora de raices de ecuaciones
USAGE
        EL usuario ingresa su ecuacion inicial, el despeje deseado y los intervalos a evaluar 
ARGUMENTS
  N/A

DICCIONARIO DE VARIABLES
ecuacionInicial: Ecuacion intriducida por el usuario a la cual se quiere encontnrar la raiz
ecuacionDespejada: Ecuacion con el despeje deseado por el usuario
limInferior: Limite inferior del intervalo a evaluar
limSuperior: Limite superior del intervalo a evaluar
numDecimales: Numero de decimales de exactitud que se requiere
fDeEquis: Diccionario donde se guardan valores de X y sus valores asociados Y
contador: contador que se usa en ciclos
posicionAnterior: Variable donde se guarda el valor de Y asociado a X
posicion: Variable donde se guarda el valor de Y asociado a Xn+1
equisCero: Guarda el valor de la primera aproximacion de X
equis: Aproximacion de X
equisEneMasUno: Aproximacion de Xn+1 que se ira comparando con equis



'''

from sympy import *
from math import *

# Se establece x como simbolo

x = symbols("x")

print("Escribe tu ecuacion inicial")
ecuacionInicial = input()

# Convierte cadena a una expresion

ecuacionInicial = sympify(ecuacionInicial)

print ("Escribe la ecuacion con el despeje deseado")
ecuacionDespejada = input()

# Convierte cadena a una expresion

ecuacionDespejada = sympify(ecuacionDespejada)

print("Escribe el limite inferior del intervalo a evaluar")
limInferior = int(input())

print("Escribe el limite superior del intervalo a evaluar")
limSuperior = int(input())

print("Escribe el numero de decimales de exactitud que requieres")
numDecimales = int(input())

fDeEquis = {}

'''
Crea diccionario de valores de y asociados a x,
se evalua la funcion en el intervalo dado
'''

for contador in range (limInferior, limSuperior+1):

    fDeEquis[contador] = ecuacionInicial.subs(x, contador)
    fDeEquis[contador]=fDeEquis[contador].evalf()

    

# Se inicializa posicion anterior para que el primer valor del array pueda ser compardo con algo

posicionAnterior = limInferior

for posicion in fDeEquis:
    
   # Si se detecta cambio de signo el valor de equis cero es asignada y el ciclo se rompe

    if (fDeEquis[posicionAnterior] < 0 and fDeEquis[posicion] > 0) or (fDeEquis[posicionAnterior] > 0 and fDeEquis[posicion] < 0): 

        equisCero = (posicion + posicionAnterior)/2
        print (equisCero)
        break
    posicionAnterior = posicion


# La primera iteracion se hace fuera del ciclo para tener valores iniciales

equis = equisCero
equisEneMasUno = ecuacionDespejada.subs(x, equis)
equisEneMasUno = equisEneMasUno.evalf()

'''
Comienza el ciclo para encontrar valor de x, el ciclo
se rompe una vez que la cantidad de decimales deseados
es igual en xn y xn+1
'''

while (round(equis, numDecimales) != round(equisEneMasUno, numDecimales)):

    equis = equisEneMasUno

    equisEneMasUno= ecuacionDespejada.subs(x, equis)

    equisEneMasUno = equisEneMasUno.evalf()


print(f"La raíz de tu ecuación en el intervalo dado es {round(equis,numDecimales)}")



