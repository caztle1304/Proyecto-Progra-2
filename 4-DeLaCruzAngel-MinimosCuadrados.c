/*NAME
        4-DeLaCruzAngel-MinimosCuadrados.py
VERSION
        1.0
AUTHOR
        Angel Adrian De la Cruz Castillo <angeldc@lcg.unam.mx>
DESCRIPTION
      Programa que aproxima una ecuacion de grado n a un conjunto de puntos 
CATEGORY
       Aproximacion funcional
USAGE
        Usuario ingresa puntos que se tienen y grado de la ecuacion a aproximar
ARGUMENTS
  N/A
DICCIONARIO DE VARIABLES
valoresX : puntero hacia los valores de X de los puntos que se tienen
valoresY: puntero hacia los valores de Y de los puntos que se tienen
matriz: puntero a punteros para hacer matriz a para resolver sistema de ecuaciones
xTemporal: guarda temporalmente un valor de X en una posicion n 
yTemporal: guarda temporalmente un valor de Y en una posicion n 
sumaX: acumulador que guarda el resultado de sumar las x elevadas a un grado n
sumaXY: acumulador que guarda el resultado de sumar las x elevadas a un grado n y luego multiplicarlas por su Y asociada
cantidadPuntos: cantidad de puntos que el usuario ingresara
temporalMatriz: guarda temporalmente el valor de la matriz en una posicion n
gradoEcuacion: grado de la ecuacion que se desea obtener
contador: variable contadora auxiliar en los ciclos
contador2: variable contadora auxiliar en los ciclos 
potencia: variable que determina la potencia a la cual se elevara un valor de X segun la el renglon y columna en la que este
iniciadorPotencia: determina en que numero iniciara la potencia para irse incrementando, con cada cambio de renglon aumenta en uno
renglon: variable contadora auxiliar para recorrer la matriz
columna:variable contadora auxiliar para recorrer la matriz

*/

#include <stdio.h>
#include <stdlib.h>

int main ()
{
 float *valoresX, *valoresY, **matriz;
 float xTemporal, yTemporal, sumaX=0, sumaXY=0, cantidadPuntos, temporalMatriz;
 int gradoEcuacion, contador, contador2, potencia, iniciadorPotencia=-1, renglon, columna;

 printf("Introduzca la cantidad de puntos\n");
 scanf("%f", &cantidadPuntos);
 printf("Introduzca el grado de la ecuacion\n"); 
 scanf("%d", &gradoEcuacion);
 printf("Ingrese los valores de X y Y de los puntos\n");

 //Se reserva memoria para guardar los valores Y asociados a los X y para un puntero de punteros
 valoresX=(float*)malloc(cantidadPuntos*sizeof(float));
 valoresY=(float*)malloc(cantidadPuntos*sizeof(float));
 matriz=(float**)malloc((gradoEcuacion+1)*sizeof(float));
 
 //Se guardan los valores X y sus Y asociados en las mismas posiciones para facilitar su acceso posteriormente
 for(contador=0; contador<cantidadPuntos; contador++)
 {
  printf("Introduzca el valor de X %d \n", contador+1);
  scanf("%f", &valoresX[contador]);
  printf("Introduzca el valor de Y %d \n", contador+1);
  scanf("%f", &valoresY[contador]);	
 }	
 
 //Se crea un array bidimensional, un puntero de punteros 
 for(renglon=0; renglon<(gradoEcuacion+1); renglon++)
 {
   matriz[renglon] = (float*)malloc(((gradoEcuacion+1)*sizeof(float))+1);
 }

//Se llena la matriz con la suma correspondiente a X, Y o a XY, todo con el grado correspondiente a cada renglon y columna
 for(renglon=0; renglon<(gradoEcuacion+1); renglon++)
  {
  	//Despues de cambiar de renglon la suma de X^nY se reinicia
    sumaXY = 0;
    //La potencia se iguala al contador que detecta cambios de renglon y aumenta cuando se baja un renglon
  	potencia = iniciadorPotencia;

  	//PARA SUMA DE X^n
  	for(columna=0; columna<(gradoEcuacion+1); columna++)
  	{
  	 //Con cada cambio de columna la suma de X^n se reinicia
  	 sumaX = 0;
  	 /*Si la casilla es la [0][0], es decir cuando el iniciador de potencia no ha detectado ningún cambio de renglon, 
  	 el valor de la casilla es asignado a la cantidad de puntos ingresados por el usuario*/
     if(potencia==-1)
     {
      sumaX=cantidadPuntos;
     }
     //Para cualquier otra casilla
     else
     {
      for(contador=0; contador<cantidadPuntos; contador++)
       {
       	//el valor de X de los puntos dados por el usuario se guarda en una variable temporal
       	xTemporal = valoresX[contador];

       	//El valor x se eleva a la potencia correspondiente a la columna en la que se encuentra
        for(contador2=0; contador2<potencia; contador2++)
        {
         xTemporal = valoresX[contador]*xTemporal;
        }
        //La suma de los valores de X se guardan en una variable temporal
        sumaX = sumaX + xTemporal;
       }
     }
     // Se guarda el valor de la suma en la casilla de la matriz correspondiente
     matriz[renglon][columna]=sumaX;
     //Cuando hay cambio de columna la potencia a la cual X sera elevada aumenta en uno
     potencia = potencia + 1;
  	}

  	//PARA SUMA DE X^nY
    for(contador=0; contador<cantidadPuntos; contador++)
      {
        //Se toman valores de X y sus Y asociados
      	xTemporal=valoresX[contador];
      	yTemporal=valoresY[contador];

      	//Para el primer renglon es X^0, por lo cual los valores de Y solo se multiplican por 1
      	if(iniciadorPotencia == -1)
        {
         xTemporal=1;
        }
       //Para todos los otros renglones el valor de X se eleva a la potencia correspondiente 
       for(contador2=0; contador2<iniciadorPotencia; contador2++)
       {
        xTemporal=valoresX[contador]*xTemporal;
       }

       //La suma de los valores X^nY se va acumulando
       sumaXY=sumaXY + (xTemporal*yTemporal);
      }
    //la suma de X^nY se guarda en el espacio de la matriz correspondiente
    matriz[renglon][gradoEcuacion+1] = sumaXY;
    //Con cada cambio de renglon el iniciador de la potencia va aumentando en 1
    iniciadorPotencia = iniciadorPotencia + 1;
    printf("\n");
    printf("\n");
  }


//Se imprime la matriz de coeficientes creada con los datos anteriores
printf("Tu matriz de coeficientes es la siguiente: \n");
for(contador=0; contador<gradoEcuacion+1; contador++)
{
 for(contador2=0; contador2<gradoEcuacion+2; contador2++)
 {
 printf("%f    ", matriz[contador][contador2]);
 }
 printf("\n");
}


/*HASTA AQUI VAS BIEN*/


//Para resolver matriz con metodo de Gauss-Jordan
/*Se crea una matriz con ceros en todas las entradas excepto en la diagonal
para después despejar los valores de x0, x1... xn con mayor facilidad*/
for(columna=0;columna<(gradoEcuacion+1);columna++)
{
 for(renglon=0; renglon<(gradoEcuacion+1);renglon++)
 {
   //Las operaciones siguientes solo se hacen fuera de los valores de la diagonal porque esos son necesarios para el  despeje final
   if(renglon!=columna)
   {
   /*Se crea variable temporal que multiplica al renglón que se quiere simplificar y se lo resta 
   	al valor de cada casilla para dejar cero la casilla de cada renglon de la columna n y afectar a los demas valores del mismo renglon*/
   temporalMatriz=matriz[renglon][columna];
  for(contador=0; contador<(gradoEcuacion+2); contador++)
  {
   //Se efectua la operacion para dejar cero en una entrada y afectar a las otras entradas del mismos renglón con la misma operacion
   matriz[renglon][contador]=(matriz[columna][columna]*matriz[renglon][contador])-(temporalMatriz*matriz[columna][contador]);
  }
  }
 }
}

//Se hace el despeje necesario para dejar uno en las diagonales y obtener los valores de xn
for(columna=0; columna<gradoEcuacion+1;columna++)
{
 matriz[columna][gradoEcuacion+1]=matriz[columna][gradoEcuacion+1]/matriz[columna][columna];
 matriz[columna][columna]=1;
}

printf("\n \n");
printf("La matriz de ecuaciones resuelta es: \n");

//Se imprime la matriz con la solucion final
for(contador=0; contador<gradoEcuacion+1; contador++)
{
 for(contador2=0; contador2<gradoEcuacion+2; contador2++)
 {
 printf("%f    ", matriz[contador][contador2]);
 }
 printf("\n");
}
printf("La ecuacion de grado %d que mas se adapta a los datos dados es: \n", gradoEcuacion);

//Se imprime la ecuacion final
for(contador=0; contador<(gradoEcuacion+1); contador++)
{
 //Para el ultimo valor de x se evita imprimir el signo de + para no dejar sin usar el ultimo signo
 if(contador == gradoEcuacion)
 {
 printf("%fx^%d ", matriz[contador][gradoEcuacion+1], contador);
 }
 else
 {
  printf("%fx^%d + ", matriz[contador][gradoEcuacion+1], contador);
 }
}
//Se libera memoria reservada para vectores con valores de X, Y y para la matriz donde se resolvió el sistema de ecuaciones
free(valoresX);
free(valoresY);
for(renglon=0; renglon<gradoEcuacion+1; renglon++)
{
 free(matriz[renglon]);
}
}
