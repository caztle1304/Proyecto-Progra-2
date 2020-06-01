from math import *
from sympy import *

x = symbols("x")

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

    # Se añade el polinomio a un acumulador para ir sumando los polinomios obtenidos

    acumuladorPolinomio = acumuladorPolinomio + polinomio


acumuladorPolinomio = simplify(acumuladorPolinomio)

resultadoValorInterpolar = acumuladorPolinomio.subs(x, valorInterpolar)

resultadoValorInterpolar = resultadoValorInterpolar.evalf()

print("\n")

print("El polinomio que mejor representa a los datos dados es:\n")

print(acumuladorPolinomio)

print("\n")

print(f"Interpolando para el valor {valorInterpolar} se obtiene que \n f({valorInterpolar}) = {resultadoValorInterpolar}")
