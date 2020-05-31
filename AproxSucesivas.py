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
    
    respaldoEcuacionInicial = ecuacionInicial
    ecuacionInicial = ecuacionInicial.subs(x, contador)
    fDeEquis[contador] = ecuacionInicial.evalf()
    ecuacionInicial = respaldoEcuacionInicial

    print(ecuacionInicial)

print (fDeEquis)


# Se inicializa posicion anterior para que el primer valor del array pueda ser compardo con algo

posicionAnterior = limInferior

for posicion in fDeEquis:
    
    print ("posicion")
    print (fDeEquis[posicion])
    print("Posicion anterior")
    print(posicionAnterior)
   
    # Si se detecta cambio de signo el valor de equis cero es asignada y el ciclo se rompe

    if (fDeEquis[posicionAnterior] < 0 and fDeEquis[posicion] > 0) or (fDeEquis[posicionAnterior] > 0 and fDeEquis[posicion] < 0): 

        equisCero = (posicion + posicionAnterior)/2
        print (equisCero)
        break
    posicionAnterior = posicion

# Se crea respaldo de ecuacion para no perderla al substituir

respaldoEcuacionDespejada = ecuacionDespejada

# La primera iteracipn se hace fuera del ciclo para tener valores iniciales

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
    
    ecuacionDespejada = respaldoEcuacionDespejada

    ecuacionDespejada = ecuacionDespejada.subs(x, equis)

    equisEneMasUno = ecuacionDespejada.evalf()
    
    ecuacionDespejada = respaldoEcuacionDespejada


print(f"La raíz de tu ecuación en el intervalo dado es {round(equis,numDecimales)}")



