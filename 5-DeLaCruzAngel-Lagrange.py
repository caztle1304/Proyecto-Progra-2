'''NAME
        5-DeLaCruzAngel-Lagrange.py
VERSION
        1.0
AUTHOR
        Angel Adrian De la Cruz Castillo <angeldc@lcg.unam.mx>
DESCRIPTION
      Programa que aproxima un polinomio a partir de un set de datos e interpola el valor deseado
CATEGORY
       Aproximacion Funcional
USAGE
        EL usuario ingresa el numero de puntos disponibles, los valores de X y Y de los puntos y un valor a interpolar
ARGUMENTS
  N/A
DICCIONARIO DE VARIABLES
listaX: lista de valores de X introduciodos por el usuario
listaY: lista de valores de Y introducidos por el usuario
cantidadPuntos: cantidad de puntos que se disponen 
punto: variable contadora utilizada en los ciclos
valorX: variable temporal que guarda el valor X introducido por el usuario y posteriormente lo introduce en la lista de X
valorY: variable temporal que guarda el valor Y introducido por el usuario y posteriormente lo introduce en la lista de Y
valorInterpolar: el valor para el cual se desea hacer la interpolacion
contadorI: contador auxiliar para realizar la suma de los valores X y Y al aplicarseles la formula
contadorJ: contador auxiliar para realizar las multiplicaciones correspondientes de los valores de X 
acumuladorPolinomio: acumula el resultado de sumar los polinomios resultantes de cada iteracion
acumuladorNumerador: acumula las multiplicaciones correspondientes al numerador del polinomio
acumuladorDenominador: acumula las multiplicaciones correspondientes al denominador del polinomio
polinomio: variable temporal que guarda el polinomio resultante de cada iteracion
resultadoValorInterpolar: resultado de hacer la interpolacion del valor introducido por el usuario
'''

from math import *
from sympy import *

x = symbols("x")

print("Este programa aproxima un polinomio a partir de puntos dados e interpola para el valor deseado")

print("Ingrese la cantidad de puntos que se tienen")

cantidadPuntos = int(input())

listaX = []

listaY = []

# Se crean listas con valores de X y Y 

for punto in range(cantidadPuntos):
    
    print("Ingrese el valor X")

    valorX = float(input())

    print(f"Ingrese el valor Y asociado al valor {valorX}")

    valorY = float(input())

    listaX.append(valorX)

    listaY.append(valorY)
   

print("Ingrese el valor para el que desea interpolar")

valorInterpolar = float(input())

# Se inician contadores para entrar al ciclo

contadorI = 0

contadorJ = 0

acumuladorPolinomio = 0

for contadorI in range(cantidadPuntos):

    # Acumuladores se reinician tras cada cambio en contadorI
    
    acumuladorNumerador = 1

    acumuladorDenominador = 1

    for contadorJ in range(cantidadPuntos):

        # Se aplica la formula para sacar el numerador y el denominador del polinomio con la condicion dada de i!=j

        if contadorI != contadorJ:
            
            acumuladorNumerador = acumuladorNumerador * (x - round(listaX[contadorJ], 5))

            acumuladorDenominador = acumuladorDenominador * (listaX[contadorI] - listaX[contadorJ])
           
    # Se forma el polinomio de la iteracion n a partir de sustituir en la formula

    polinomio = (acumuladorNumerador / round(acumuladorDenominador, 5)) * listaY[contadorI]

    # Se anade el polinomio a un acumulador para ir sumando los polinomios obtenidos

    acumuladorPolinomio = acumuladorPolinomio + polinomio


acumuladorPolinomio = simplify(acumuladorPolinomio)

resultadoValorInterpolar = acumuladorPolinomio.subs(x, valorInterpolar)

resultadoValorInterpolar = resultadoValorInterpolar.evalf()

print("\n")

print("El polinomio que mejor representa a los datos dados es:\n")

print(acumuladorPolinomio)

print("\n")

print(f"Interpolando para el valor {valorInterpolar} se obtiene que \n f({valorInterpolar}) = {resultadoValorInterpolar}")

