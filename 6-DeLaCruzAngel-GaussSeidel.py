'''NAME
        6-DeLaCruzAngel-GaussSeidel.py
VERSION
        1.0
AUTHOR
        Angel Adrian De la Cruz Castillo <angeldc@lcg.unam.mx>
DESCRIPTION
      Programa que calcula soluciones de sistemas de ecuaciones usando metodo de Gauss-Seidel
CATEGORY
       Calculadora de sistemas de ecuaciones
USAGE
        Usuario ingresa coeficientes de ecuaciones, simbolos a usar y decimales de precision requeridos
ARGUMENTS
  N/A
DICCIONARIO DE VARIABLES
numeroEcuaciones: numero de ecuaciones que hay en el sistema
variables: lista de variables que habra en el sistema
simbolos: variables del sistema convertidas a simbolos
letra: variable que itera en cada letra de la lista de simbolos
aproximacionVariables: diccionario que asocia una variable con su valor aproximado en la iteracion n
aproximacionVariablesAnterior: diccionario que asocia una variable con su valor aproximado en la iteracion n-1
matriz: matriz extendida de coeficientes que representa las ecuaciones
listaTemporal: guarda los coeficientes de un renglon y los sustituye en la matriz
renglon: variable contadora que itera los renglones de la matriz
columna: variable contadora que itera las columnas de la matriz
contador: variable contadora auxiliar en los ciclos
posicionMaxima: guarda la posicion del vector donde se encuentra el coeficiente de mayor valor absoluto
ecuaciones: diccionario que asocia las variables con su despeje
ecuacion: variable que arma la ecuacion de cada renglon al multiplicar renglon de la matriz por vector de variables
ecuacionTemporal: guarda el resultado de despejar la ecuacion respecto a una variable
contadorCiclo: lleva la cuenta de la iteracion en la que se va al hacer las aproximaciones de las variables
variable: ayuda a iterar los valores asociados a las llaves del diccionario de aproximaciones de variables
letra1: ayuda a iterar los valores asociados a las llaves del diccionario de ecuaciones
letra2: itera los valores asociados a las llaves del diccionario de aproximaciones de variables
ecuacionSustituida: resultado de sustituir todas las variables en las ecuaciones despejadas
efeDeVariable: resultado de evaluar la ecuacion con todas las sustituciones hechas
'''

from math import *
from sympy import *
import numpy as np

print("Este programa calcula soluciones a sistemas de ecuaciones usando metodo de Gauss-Seidel\n")

print("Ingrese el numero de ecuaciones de su sistema")

numeroEcuaciones = int(input())

print("ingrese las variables que hay en sus ecuaciones SEPARADAS POR UN ESPACIO")

variables = input()

# Se crea una lista a partir de todas las variables introducidas

variables = variables.split()

simbolos = []

# Las variables se convierten en simbolos y se agregan a nueva lista

for letra in variables:

    simbolos.append(symbols(letra))

'''
Se crean dos diccionarios, uno con la aproximacion n y otro con la aproximacion n+1, 
para comparar al momento de entrar al ciclo
'''

aproximacionVariables = {}

aproximacionVariablesAnterior = {}

'''
A las variables del primer diccionario se les asigna valor de cero 
para la iteracion inicial y al otro diccionario se le asignan valores de uno
para que se cumpla la condicion que hace que se entre en el while
'''

for letra in simbolos:
     
     aproximacionVariables[letra] = 0
     aproximacionVariablesAnterior[letra] = 1



print("Ingresa los coeficientes de tus ecuaciones")

# Crea matriz para insertar los coeficientes en su lugar correspondiente

matriz = np.zeros(shape = (numeroEcuaciones, numeroEcuaciones+1), dtype = float)

listaTemporal = []

# Llena lista temporal para que tenga la longitud adecuada para guardar todos los coeficientes

for columna in range(numeroEcuaciones + 1):
    
    listaTemporal.append(0)

# Recorre matriz 

for renglon in range(numeroEcuaciones):

    for columna in range(numeroEcuaciones + 1):

        # Llena espacios correspondientes a coeficientes en la matriz

        if (columna < numeroEcuaciones):

            print(f"Ingresa el coeficiente de {simbolos[columna]} de la ecuacion {renglon + 1}")
        
            listaTemporal[columna] = input() 

            listaTemporal[columna] = sympify(listaTemporal[columna])

            # Guarda la posicion donde se encuentra el coeficiente con mayor valor absoluto para crear matriz diagonalmente dominante

            posicionMaxima = listaTemporal.index(max(listaTemporal, key = abs))
        
        # Llena espacios correspondientes al lado derecho de la igualdad

        else:

            print(f"Ingresa a que esta igualada tu ecuacion {renglon + 1}")

            matriz[renglon, columna] = input()

            matriz[renglon, columna] = sympify(matriz[renglon, columna])

    # Llena renglon de la matriz segun la posicion del coeficiente de mayor valor absoluto

    for contador in range(numeroEcuaciones):

         matriz[posicionMaxima, contador] = listaTemporal[contador]


ecuaciones = {}

#Llena diccionario de ecuaciones de variable con cadenas vacias

for letra in simbolos:
    
    ecuaciones[letra] = ""

#Multiplica la matriz de coeficientes por vector de variables y asigna la ecuacion resultante de cada renglon a su vaariable correspondiente

for renglon, letra in zip(range(numeroEcuaciones), simbolos):

    ecuacion = 0

    #Crea ecuaciones de acuerdo a cada renglon de la matriz
    
    for columna in range(numeroEcuaciones):

        ecuacion = ecuacion + (matriz[renglon, columna] * simbolos[columna])

    # Iguala ecuacion creada al resultado que corresponda segun el renglon

    ecuacion = Eq(ecuacion, matriz[renglon, numeroEcuaciones])

    # Resuelve ecuacion creada respecto a la letra correspondiente al renglon
    
    ecuacionTemporal = solve(ecuacion, letra)

    # Convierte la lista devuelta de resolver la ecuacion en un solo string 

    ecuaciones[letra] = ecuaciones[letra].join(map(str,ecuacionTemporal))

    #convierte string en expresion

    ecuaciones[letra] = sympify(ecuaciones[letra])




print("Ingresa con cuantos decimales de exactitud quieres los resultados")

numDecimales = int(input())

contadorCiclo = 0


while aproximacionVariablesAnterior != aproximacionVariables:

    contadorCiclo = contadorCiclo + 1
   
    print(f"\nITERACION NUMERO {contadorCiclo}")

    ecuacionSustituida = ""

    # Asigna valor de cada variable en la iteracion anterior al diccionario correspondiente

    for variable in aproximacionVariables:

        aproximacionVariablesAnterior[variable] = aproximacionVariables[variable]
    
    # Recorre cada ecuacion despejada y la asigna a variable para ser sustituida
   
    for letra1 in ecuaciones:

        ecuacionSustituida = ecuaciones[letra1]

        ecuacionSustituida = sympify(ecuacionSustituida)


        # Recorre cada variable y en cada ecuacion sustituye la variable por su valor asociado

        for letra2 in simbolos:

            ecuacionSustituida = ecuacionSustituida.subs(letra2, aproximacionVariables[letra2])

    
        efeDeVariable = ecuacionSustituida.evalf()


        # Anade el valor aproximado de la variable encontrado de sustituir los valores aproximados encontrados

        aproximacionVariables[letra1] = round(efeDeVariable, numDecimales)

    print(aproximacionVariables)



print("\nLos resultados obtenidos son: \n")

print(aproximacionVariables)

print(f"Completado en {contadorCiclo} iteraciones")  		
