'''NAME
        8-DeLaCruzAngel-Romberg.py
VERSION
        1.0
AUTHOR
        Angel Adrian De la Cruz Castillo <angeldc@lcg.unam.mx>
DESCRIPTION
      Programa que calcula area bajo la curva usando metodo de Romberg
CATEGORY
       Calculadora de area bajo la curva
USAGE
        Usuario ingresa su funcion y los limites superior e inferior del intervalo a evaluar
ARGUMENTS
  N/A
DICCIONARIO DE VARIABLES
ecuacionInicial: ecuacion inicial a partir de la cual se calcula area bajo la curva
limInferior: limite inferior del intervalo del cual se obtendra el area
limSuperior: limite superior del intervalo del cual de obtendra el area
numDecimales: numero de decimales de exactitud que se requiere
matriz: matriz donde se guardan las aproximaciones del area y sus refinamientos
efeDeA: resultado de evaluar el limite inferior en la ecuacion dada
efeDeB: resultado de evaluar el limite superior en la ecuacion dada
c: Tamano del intervalo a evaluar
a: limite inferior que se usa para sustituir en las formulas
b: limite superior que se usa para sustituir en las formulas
j: variable usada para sustituir en la formula de las aproximaciones de I y sus refinamientos
i: aproximaciones del area bajo la curva y sus refinamientos
contadoriMultDeDos: variable que se multiplica por 2 para generar nuevas formulas de I cuantas veces sea necesario
contadoriMultDeCuatro: variable que se multiplica por 4 para generar nuevas formulas de I cuantas veces sea necesario
contadorjDenominador: variable que se multiplica por dos cuantas veces sea necesario para generar nuevas formulas de J
contadorjNumerador: variable que va aumentando en 1 cuantas veces sea necesario para generar nuevas formulas de J
repeticiones: variable que sirve para determinar el numero de veces que se efectuara la suma en J 
acumulador: contador utilizado en la determinacion de veces que se hace la suma de J
acumulador2: contador usado para cambiar de renglon en la matriz
valor: variable que guarda el valor del refinamiento de I en la posicion n
valorAnterior: variable que guarda el valor del refinamiento de I en la posicion n-1
contador: variable cuntadora usada para efectuar la suma de J n veces
sustitucion: guarda resultado de realizar las sustituciones correspondientes en la formula para el calculo de J
acumuladorSumaJ: guarda resultado final de la suma de J
renglon: variable contador que sirve para recorrer los renglones de la matriz
columna: variable contadora que sirve para recorrer las columnas de la matriz


'''

from math import *
from sympy import *
import numpy

# Crea simbolo de x

x = symbols("x")

print("Este programa calcula area bajo la curva usando el metodo de Romberg\n")

print("Ingresa tu ecuacion inicial")

ecuacionInicial = input()

ecuacionInicial = sympify(ecuacionInicial)

print("Ingresa el limite inferior del intervalo a evaluar")

limInferior = input()
limInferior = sympify(limInferior)

print("Ingresa el limite superior del intervalo a evaluar")

limSuperior = input()
limSuperior = sympify(limSuperior)

print("Ingresa los decimales de exactitud que quieres")

numDecimales = int(input())

# Se crea matriz para guardar los valores de I y sus refinamientos

matriz = numpy.zeros(shape = (10,10), dtype = float)

efeDeA = ecuacionInicial.subs(x, limInferior)

efeDeA = efeDeA.evalf()

efeDeB = ecuacionInicial.subs(x, limSuperior)

efeDeB = efeDeB.evalf()

# Se definen valores iniciales que se usaran para las formulas posteriores

c = limSuperior - limInferior

a = limInferior

b = limSuperior

# Se hace la primera aproximacion de i fuera del ciclo para asignar valores iniciales

j = (1/2) * (efeDeA + efeDeB)

i = c * j

# Se asigna la primera aproximacion de i 

matriz[0,0] = i

# Se dan valores iniciales a variables que entraran en ciclo while


#Variable que se ira multiplicando por 2,se ocupa para la formula de las aproximaciones de I 


contadoriMultDeDos = 1


# Variable que se ira multiplicando por 4, se usa para los refinamientos de las aproximaciones de I


contadoriMultDeCuatro = 1

# Variable que se ira multiplicando por 2, se usa para los denominadores de j

contadorjDenominador = 1

# Variable que se multiplica por 2 cada ciclo del while para determinar el numero de veces que se repetira la suma de j

acumulador = 1 

# variable que ira sumando 1 cada ciclo del while para ir cambiando de renglon en la matriz

acumulador2 = 0

# Variable que guarda los refinamientos de I y sus aproximaciones anteriores para comparar

valorAnterior = round(i, numDecimales)

#  variable que guarda refinamientos y aproximaciones de I para comparar con sus anteriores, se asigna a -1 porque no hay area negativa

valor = -1

while round(valorAnterior, numDecimales) != round(valor, numDecimales):


    acumulador = acumulador * 2

    acumulador2 = acumulador2 + 1

    # Se asigna jAnterior para sustituir en la formula de jn+1

    jAnterior = j 

    # El acumulador de la suma se vuelve cero otra vez para reiniciarlo

    acumuladorSumaJ = 0

    # Se guarda el valor anterior de I o su aproximacion para comparar con n+1

    valorAnterior = round(i, numDecimales) 

    # Se reinicia el contador de los numeradores de j a 1
    
    contadorjNumerador = 1

    # El contador se multiplica por dos cada que hay un cambio de renglon en la matriz
    
    contadoriMultDeDos = contadoriMultDeDos * 2

    # El contador se multiplica por 2 cada que hay cambio de renglon en matriz

    contadorjDenominador = contadorjDenominador * 2

    # El numero de repeticiones de la suma de j se calcula con la siguiente formula

    repeticiones = acumulador - (acumulador / 2)

    repeticiones = int(repeticiones)


    
    for contador in range(repeticiones):


        sustitucion = a + ((contadorjNumerador/contadorjDenominador) * c) 

        sustitucion = ecuacionInicial.subs(x, sustitucion)

        sustitucion = sustitucion.evalf()

        acumuladorSumaJ = acumuladorSumaJ + sustitucion

        # el contador del numerador ira sumando uno cada que se cambie de suma

        contadorjNumerador = contadorjNumerador + 2

    j = jAnterior + acumuladorSumaJ

    for renglon in range(acumulador2, acumulador2 + 1):

        # El condtador se multiplica por cuatro cada que hay un cambio de columna

        contadoriMultDeCuatro = 1

        for columna in range(acumulador2 + 1):


            
            # Si esta en la primera columna se aplica la formula sencilla de I = 1/n cJ
            
         
            if columna == 0:

                i = (1/contadoriMultDeDos) * c * j

                matriz[renglon, columna] = i
            
            # Si no se esta en la primera columna se aplican las formulas mas complejas y su denominador va cambiando

            if columna != 0: 

            	# Multiplica por 4 el contador que se ira aplicando en la formula con cada cambio de columna

                contadoriMultDeCuatro = contadoriMultDeCuatro * 4

                i = (1/(contadoriMultDeCuatro - 1)) * (contadoriMultDeCuatro * matriz[renglon, columna - 1] - matriz[renglon - 1, columna - 1])

                matriz[renglon, columna] = i

                valor = i

                valorAnterior = matriz[renglon, columna - 1]

print("Las matriz escalonada de aproximaciones y refinamientos de area es la siguiente")

print(matriz)
        
print(f"El area bajo la curva en los intervalos dados es {round(i, numDecimales)}")
