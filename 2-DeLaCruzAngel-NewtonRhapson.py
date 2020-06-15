'''NAME
        2-DeLaCruzAngel-NewtonRhapson.py
VERSION
        1.0
AUTHOR
        Angel Adrian De la Cruz Castillo <angeldc@lcg.unam.mx>
DESCRIPTION
      Programa que calcula raices de ecuaciones usando el metodo de Newton-Rhapson
CATEGORY
       Calculadora de raices de ecuaciones
USAGE
        EL usuario ingresa su ecuacion inicial, el intervalo a evaluar y el step de incremento en el intervalo
ARGUMENTS
  N/A
DICCIONARIO DE VARIABLES
ecuacionInicial : Ecuacion de la cual se obtendran las raices
derivada: Derivada de la ecuacion inicial
limSuperior: Limite superior del intervalo a evaluar
limInferior: Limite inferior del intervalo a evaluar
step: Paso de incremento al evaluar las funciones
numDecimales: Numero de decimales de exactitud requeridos por el usuario
fDeEquis: Diccionario de valores de X asociados a su funcion
contador: contador auxiliar en los ciclos
posicion: variable que guarda f(x) en la posicion n+1
posicionAnterior: variable que guarda f(x) en la posicion n
equisCero: aproximacion inicial de x (x0)
equis: Aproximacion de xn
equisEneMasUno: Aproximacion de xn+1


'''

from sympy import *
from sympy import *


# Se establece x como símbolo

x = symbols("x")

print("Escribe tu ecuacion inicial")

ecuacionInicial = input()

# Convierte la cadena en una expresion

ecuacionInicial = sympify(ecuacionInicial)

derivada = ecuacionInicial.diff(x)

print("Escribe el limite inferior del intervalo a evaluar")
limInferior = input()
limInferior = sympify(limInferior)

print("Escribe el limite superior del intervalo a evaluar")
limSuperior = input()
limSuperior = sympify(limSuperior)

print("Escribe el paso de aumento en la evaluacion de tu intervalo")
step = input()
step = sympify(step)
print("Escribe el numero de decimales de exactitud que requieres")
numDecimales = int(input())

fDeEquis = {}

'''

Se crea diccionario de valores de y asociados a x,
se evalua la funcion en el intervalo
'''
contador = limInferior

while contador < (limSuperior + step):

    fDeEquis[contador] = ecuacionInicial.subs(x,contador)
    fDeEquis[contador] = fDeEquis[contador].evalf()
    contador = contador + step

# Se inicializa posicion anterior para que el primer valor del array pueda ser comparado con algo

posicionAnterior = limInferior

for posicion in fDeEquis:
    
   # Al detectarse un cambio de signo en los valores de y, el proceso termina y equis cero es asignada

    if (fDeEquis[posicionAnterior] < 0 and fDeEquis[posicion] > 0) or (fDeEquis[posicionAnterior] > 0 and fDeEquis[posicion] < 0): 

        equisCero = (posicion + posicionAnterior) / 2
        break
    posicionAnterior = posicion


# La primera iteracion se hace fuera del ciclo para asignar valores iniciales
equis = equisCero
equisEneMasUno = equisCero - ((ecuacionInicial.subs(x, equis)) / (derivada.subs(x, equis)))
equisEneMasUno = equisEneMasUno.evalf()


'''
Comienza el ciclo para encontrar valor de x, el ciclo
se rompe una vez que la cantidad de decimales deseados
es igual en xn y xn+1
'''

while(round(equis, numDecimales)) != (round(equisEneMasUno, numDecimales)):
    
    equis = equisEneMasUno

    equisEneMasUno = equis - ((ecuacionInicial.subs(x, equis)) / (derivada.subs(x, equis)))

    equisEneMasUno = equisEneMasUno.evalf()


print(f"La raiz de tu ecuacion en el intervalo dado es {round(equis, numDecimales)}")
