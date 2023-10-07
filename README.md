# Reto-6_QUE-DIFICIL-FUE...
## El reto 6 consiste en los siguiente ejercicios. Consiguiente a cada ejercicios está su solución.Tener en cuenta que cada ejercicios está subido en formato .py.Espero sea de su agrado este repositorio.
### 1. Dado la figura de la imagen, desarrolle:
![Ejercicio1](https://camo.githubusercontent.com/5b3d4141c9f98bb266ed388206798488c7845886759de5fb33d61769c3a7632f/68747470733a2f2f692e706f7374696d672e63632f465276436d7078782f696d6167652e706e67)
 ### *Una función matemática para calcular el volumen y el área superficial.
 ### *Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.
 ### *Revise como utilizar el valor de pi usando import math y math.pi
#### Solución:
* Primero lo se hizo fue importar el paquete math para poder usar el math.pi
* Siguiente a ello creamos la funciones con su respectivo nombre, las variables que involucraría, las fórmulas para cada caso y añadimos el return.
* De ahí partimos al if, con el math.pi, inicalizamos variables y su respectivo print para dar la respuesta.
```
#importamos el paquete math para poder más adelante añadir el valor de pi a través de math.pi
import math
#La primera función que crearemos es la función para hallar el VOLUMEN de la ESFERA
def calcularVolumenDeLaEsfera(r1:float) -> float:
    volumenDeLaEsfera = (4/3)*(pi)*(r1**2) #Esta es la formula para hallar el volumen de la esfera
    return volumenDeLaEsfera
#Ahora calcularemos el ÁREA SUPERFICIAL de la ESFERA a tráves de la siguiente función
def calcularAreaSuperficialDeLaEsfera(r1:float) -> float:
    areaSuperficialDeLaEsfera = 4*pi*(r1**2) #Ecuación de el área superficial
    return areaSuperficialDeLaEsfera
#Ahora calcularemos el VOLUMEN del CONO a través de la siguiente función
def calcularVolumenDelCono(r2:float, h:float) -> float:
    volumenDelCono = ((pi)*(r2**2)*(h))/3 #Formula para hallar el volumen del cono
    return volumenDelCono
#Ahora calcularemos el ÁREA SUPERFICIAL del CONO a tráves de la siguiente función
def calcularAreaSuperficialDelCono(r2:float, h:float) -> float:
    generatriz = ((h**2)+(r2**2))**0.5
    areaSuperficialDelCono = ((pi)*(r2**2)) + ((pi)*(r2)*(generatriz))
    return areaSuperficialDelCono
#Ponemos las variables sin olvidarnos del math.pi para tener el valor de pi
if __name__ == "__main__":
    r1 : float = float(input("Ingrese el radio de la esfera: "))
    pi : float = math.pi
    r2 : float = float(input("Ingrese el radio del cono: "))
    h : float = float(input("Ingrese la altura del cono: "))
    volumen = calcularVolumenDeLaEsfera(r1)
    area = calcularAreaSuperficialDeLaEsfera(r1)
    volumen1 = calcularVolumenDelCono(r2, h)
    area1 = calcularAreaSuperficialDelCono(r2, h)
    print("El volumen de la esfera es", str(volumen), "y el área superficial de la esfera es", str(area))
    print("El volumen del cono es", str(volumen1), "y el área superficial del cono es", str(area1))
```
### 2. Dado la figura de la imagen, desarrolle:
![Ejercicio2](https://camo.githubusercontent.com/28efbd1c6a4c4c37c454cf7444d76fb0e4142cd3663caa030ce88ef3e153dd55/68747470733a2f2f692e706f7374696d672e63632f3174344d727a734c2f696d6167652e706e67)
### * Una función matemática para calcular el área y el perimetro.
### * Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.
### * Revise como utilizar el valor de pi usando import math y math.pi
#### Solución
* Importamos el paquete math para poder usar el math.pi
* Siguiente a ello creamos la funciones con su respectivo nombre, las variables que involucraría, las fórmulas para cada caso y añadimos el return.
* De ahí partimos al if, con el math.pi, inicalizamos variables y su respectivo print para dar la respuesta.
```
#Importamos parquete
import math
pi = math.pi
#Primero haremos las funciones
#Iniciaremos por el PERIMETRO del RECTÁNGULO
def calcularPerimetroDelRectangulo(a:float, b:float) ->float:
    perimetroRectangulo = (a*2) + (b*2) #Esta será fórmula para hallar el perimetro
    return perimetroRectangulo
#Ahora haremos la función para el ÁREA del RECTÁNGULO
def calcularAreaDelRectangulo(a: float, b:float) -> float:
    areaRectangulo = (a*b) #Esta será la fórmula para hallar el área
    return areaRectangulo
#Siguiente será el PERIMETRO de la CIRCUNFERENCIA
def calcularPerimetroDelaCircunferencia (r:float) -> float:
    perimetroCircunferencia = 2*pi*r #Esta es la fórmula para calcular el perimetro del circulo
    return perimetroCircunferencia
#Por último haremos la función para calcular el ÁREA de la CIRCUNFERENCIA
def calcularAreaDelCirculo(r:float) -> float:
    areaDelCirculo = pi*(r**2)
    return areaDelCirculo
#Ingresamos variables
if __name__ == "__main__":
    a:float=float(input("Ingrese un valor para un lado del rectángulo: "))
    b:float=float(input("Ingrese  un valor para la base del rectángulo: "))
    r:float=float(input("Ingrese un valor para el radio del circulo: "))
    perimetroR = calcularPerimetroDelRectangulo(a, b)
    areaR = calcularAreaDelRectangulo(a, b)
    perimetroC = calcularPerimetroDelaCircunferencia(r)
    areaC = calcularAreaDelCirculo(r)
    print("El perimetro y el área del rectangulo son", str(perimetroR), "y", str(areaR), "respectivamente.")
    print("El perimetro y el área del circulo son", str(perimetroC), "y", str(areaC), "respectivamente.")
```
### 3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.
#### Solución
* Siguiente a ello creamos la funciones con su respectivo nombre, las variables que involucraría, las fórmulas para cada caso y añadimos el return.
* Llegamos a la parte del if, en la cual inicializamos las variables y además de ello añadimos las variables del peso que se dieron al inicio del ejercicio, hacemos el debido procedimiento y seguido a esto incluimos el print para recibir la respuesta
```
#Mensaje contextulizador sobre el programa
print("Dinos el número de gallinas, gallos y/o pollitos que tienes y te diremos cuanta carne te llevaras de cada uno")
#Para hacer este ejercicio crearemos tres funciones
#Primero crearemos la función relacionada con las gallinas
def calcularCantidadCarneGallina(N:int) -> float:
    cantidadCarneGallina = N*pesoGallina
    return cantidadCarneGallina
#Después crearemos la función relacionada con los gallos
def calcularCantidadCarneGallo(M:int) -> float:
    cantidadCarneGallo = M*pesoGallo
    return cantidadCarneGallo
#Y por último crearemos la función relacionada con los pollitos
def calcularCantidadCarnePollito(K:int) -> float:
    cantidadCarnePollito = K*pesoPollito
    return cantidadCarnePollito
#Al tener las funciones procedemos a Declarar e inicializar las variables
if __name__ == "__main__":
    N:int=int(input("Ingrese el numero de gallinas que tiene: "))
    M:int=int(input("Ingrese el numero de gallos que tiene: "))
    K:int=int(input("Ingrese el numero de pollitos que tiene: "))
    pesoGallina:float=6
    pesoGallo:float=7
    pesoPollito:float=1
    carneGallina = calcularCantidadCarneGallina(N)
    carneGallo = calcularCantidadCarneGallo(M)
    carnePollito = calcularCantidadCarnePollito(K)
    print("La cantidad de carne de gallina en función del número de gallinas que tenía es de", str(carneGallina),"Kg")
    print("La cantidad de carne de gallo en función del número de gallos que usted tenía es de", str(carneGallo),"Kg")
    print("La cantidad de carne de pollo en función del número de pollitos que usted tenía es de", str(carnePollito),"Kg")
```
### 4. Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.
#### Solución
* Siguiente a ello creamos la funciones con su respectivo nombre, las variables que involucraría, las fórmulas para cada caso y añadimos el return.
* Llegamos a la parte del if, en la cual inicializamos las variables y además de ello añadimos las variables del precio que se dieron al inicio del ejercicio, hacemos el debido procedimiento y seguido a esto incluimos el print para recibir la respuesta.
* Después de recibir el valor de cada una de las compras las sumamos para dar el total.
* Por último utilizamos el if, else, y elif para ver que pasa dependiendo de lo que el cliente pague.
```
#Mensaje contextualizador sobre el programa
print("Ingrese la cantidad de productos que va a comprar de panes, bolsas de leche y huevos. Te daremos el precio que tiene que pagar, se te informará de las vueltas o lo que quedas debiendo.")
#Crearemos un programa con las siguientes funciones
#Una función que me diga el precio dependiendo de el número de panes que compre
def calcularPrecioPanes(P:int) -> int:
    precioPanes = P*valorPan
    return precioPanes
#Otra función que me diga el precio dependiendo del número de bolsas de leche que compre
def calcularPrecioBolsasDeLeche(M:int) -> int:
    precioBolsasDeLeche = M*valorBolsasDeLeche
    return precioBolsasDeLeche
#Y por último una función que diga el precio dependiendo del número de huevos que compre
def calcularPrecioHuevo(H:int) -> int:
    precioHuevos = H*valorHuevo
    return precioHuevos
#Ahora declaramos e inicializamos variables, haciendo la suma entre los resultados de las funciones
if __name__ == "__main__":
    P:int=int(input("Ingrese el numero de panes que comprará: "))
    M:int=int(input("Ingrese el numero de bolsas de leche que comprará: "))
    H:int=int(input("Ingrese el numero de huevos que comprará: "))
    valorPan:int=300
    valorBolsasDeLeche:int=3300
    valorHuevo:int=350
    precioDelPan = calcularPrecioPanes(P)
    precioDeLasBolsasDeLeche = calcularPrecioBolsasDeLeche(M)
    precioDeLosHuevos = calcularPrecioHuevo(H)
    valorTotal = precioDelPan + precioDeLasBolsasDeLeche + precioDeLosHuevos
    print("El precio de los panes en función del número de panes que comprará es de", str(precioDelPan),"pesos.")
    print("El precio de las bolsas de leche en función del número de bolsas de leche que comprará es de", str(precioDeLasBolsasDeLeche),"pesos.")
    print("El precio de los huevos en función del número de huevos que comprará es de", str(precioDeLosHuevos),"pesos.")
    print("El valor total que debe pagar es de", str(valorTotal),"pesos")
    dineroIngresado:int=int(input("Ingrese dinero con el que pagará: "))
    if dineroIngresado > valorTotal:
        vueltas = dineroIngresado - valorTotal
        print("Las vueltas de su compra son", str(vueltas), "pesos")
    elif dineroIngresado < valorTotal:
        debe = valorTotal - dineroIngresado
        print("No ingresó el dinero total que debía, queda debiendo", str(debe), "pesos")
    else:
        print("¡Gracias por su compra!")
```
### 5. Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.
#### Solución
* Siguiente a ello creamos la funciones con su respectivo nombre, las variables que involucraría, las fórmulas para este caso que sería la del interes compuesto y añadimos el return.
* Llegamos a la parte del if, en la cual inicializamos las variables que se dieron al inicio del ejercicio, hacemos el debido procedimiento y seguido a esto incluimos el print para recibir la respuesta. Para la variable i ponemos una condición que usamos para el interes mensual que se usa en el ejercicio.
```
#Mensaje contextualizador de lo que hace el programa
print("Ingrese el capital que se le prestará al cliente, el interés del prestamo  que será MENSUAL y el tiempo en el que se pagará en MESES")
#Hacemos la función para hacer el cálculo
def calcularValorDelPrestamo(c:float, i:float, n:int) -> float:
    valorDelPrestamo = c*((1+i)**n)
    return valorDelPrestamo
#Ahora declaramos y inicializamos a las variables
if __name__ == "__main__":
    c:float=float(input("Ingrese el capital que se le prestará al cliente: "))
    i:float=float(input("Ingrese el interes mensual del prestamo, tenga en cuenta que SOLO podrá ingresar valores  de 0 a 1: "))
    if 0 <= i <=1:
        print("Gracias por darnos el interes con las condiciones establecidas")
    else:
        print("Ingrese un valor para el interés con las condiciones establecidas")
    n:int=int(input("Ingrese el número de meses del prestamo: "))
    valorPrestamo = calcularValorDelPrestamo(c, i, n)
    print("El valor del prestamo que usted deberá tener pagado al finalizar el prestamos es de", str(valorPrestamo))
```
### 6. El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.
#### Solución
* Siguiente a ello creamos la función con su respectivo nombre, las variables que involucraría, las fórmula para el caso y añadimos el return.
* Llegamos a la parte del if, en la cual inicializamos las variables que se dieron al inicio del ejercicio, hacemos el debido procedimiento y seguido a esto incluimos el print para recibir la respuesta.
```
#Mensaje contextualizador de lo que hace el programa
print("Ingrese el número de contagiados actuales de Covid-19 en NuncaLandia y un número de días para calcular cuantos habrá en un futuro dependiendo de los contagiados actuales")
#Hacemos la función para hacer el cálculo
def calcularAproximacionContagiadosNuncalandia(c:int, d:int) -> int:
    aproximacionContagiadosNuncalandia = c*(2**d)
    return aproximacionContagiadosNuncalandia
#Ahora declaramos y inicializamos a las variables
if __name__ == "__main__":
    c:int=int(input("Ingrese el número de actuales contagiados en Nuncalandia: "))
    d:int=int(input("Ingrese el número de días apartir de hoy que se va a analizar: "))
    proximosContagiadosNuncalandia = calcularAproximacionContagiadosNuncalandia(c, d)
    print("El número de contagiados en Nuncalandia será de", str(proximosContagiadosNuncalandia), "teniendo en cuenta los días a partir de hoy.")
```
### 7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:

### * El promedio
### * La mediana
### * El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
### * Ordenar los números de forma ascendente
### * Ordenar los números de forma descendente
### * La potencia del mayor número elevado al menor número
### * La raíz cúbica del menor número

#### Solución
```
#Mensaje contextualizador del ejercicio
print("Introduzca 5 número reales que usted quiera y vea la magia")
#Función 1. Promedio
def calcularPromedio(x:float, y:float, z:float, m:float, n:float) -> float:
    promedio = (x + y + z + m + n)/5
    return promedio
#Función 2. Mediana
def calcularMediana(x:float, y:float, z:float, m:float, n:float) -> float:
    listaReales = [x, y, z, m, n]
    listaReales_ordenados = sorted(listaReales)
    mediana = listaReales_ordenados[len(listaReales) // 2]
    return mediana
#Función 3. Promedio Multiplicativo
def calcularPromedioMultiplicativo(x:float, y:float, z:float, m:float, n:float) -> float:
    promedioMultiplicativo = (x*y*z*m*n)**(0.2) 
    return promedioMultiplicativo
#Función 4. Números forma ascendente
def calcularAscendente(x:float, y:float, z:float, m:float, n:float) -> float:
    listaReales = [x, y, z, m, n]
    ascendente = sorted(listaReales)
    return ascendente
#Función 5. Números forma descendente
def calcularDescendente(x:float, y:float, z:float, m:float, n:float) -> float:
    listaReales = [x, y, z, m, n]
    descendente = sorted(listaReales, reverse=True)
    return descendente
#Función 6. Potencia del mayor número elevado al menor número
def calcularPotenciaNumeroMayorElevadoMenorNumero(x:float, y:float, z:float, m:float, n:float) -> float:
    listaReales = [x, y, z, m, n]
    numeroMayor = max(listaReales)
    numeroMenor = min(listaReales)
    mayorElevadoAlMenor = numeroMayor**numeroMenor
    return mayorElevadoAlMenor
#Función 7. Raiz cubica del numero menor
def calcularRaizCubicaNumeroMenor(x:float, y:float, z:float, m:float, n:float) -> float:
    listaReales = [x, y, z, m, n]
    numeroMenor = min(listaReales)
    return numeroMenor
#Declaramos e inicializamos variables
if __name__ == "__main__":
    x:float=float(input("Ingrese un valor para x: "))
    y:float=float(input("Ingrese un valor para y: "))
    z:float=float(input("Ingrese un valor para z: "))
    m:float=float(input("Ingrese un valor para m: "))
    n:float=float(input("Ingrese un valor para n: "))
    promedioF = calcularPromedio(x, y, z, m, n)
    medianaF = calcularMediana(x, y, z, m, n)
    promedioMultiplicativoF = calcularPromedioMultiplicativo(x, y, z, m, n)
    ascendenteF = calcularAscendente(x, y, z, m, n)
    descendenteF = calcularDescendente(x, y, z, m, n)
    mayorElevadoMenorF = calcularPotenciaNumeroMayorElevadoMenorNumero(x, y, z, m, n)
    numeroMenorF = calcularRaizCubicaNumeroMenor(x, y, z, m, n)
    print("El promedio, la mediana, el promedio multiplicativo, los número ordenados ascendentemente, los números ordenados descendentemente, el número mayor elevado al menor y la raiz cúbica del menor número de los 5 reales que se pusieron son", str(promedioF), ";", str(medianaF), ";", str(promedioMultiplicativoF), ";", str(ascendenteF),";", str(descendenteF),";", str(mayorElevadoMenorF),"y", str(numeroMenorF), "respectivamente.")
```
### 8. Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.
#### Solución
* Importamos desde el anterior punto a este, por lo que funcionaría el paquete
```
from punto7 import *
if __name__ == "__main__":
    x:float=float(input("Ingrese un valor para x: "))
    y:float=float(input("Ingrese un valor para y: "))
    z:float=float(input("Ingrese un valor para z: "))
    m:float=float(input("Ingrese un valor para m: "))
    n:float=float(input("Ingrese un valor para n: "))
    promedioF = calcularPromedio(x, y, z, m, n)
    medianaF = calcularMediana(x, y, z, m, n)
    promedioMultiplicativoF = calcularPromedioMultiplicativo(x, y, z, m, n)
    ascendenteF = calcularAscendente(x, y, z, m, n)
    descendenteF = calcularDescendente(x, y, z, m, n)
    mayorElevadoMenorF = calcularPotenciaNumeroMayorElevadoMenorNumero(x, y, z, m, n)
    numeroMenorF = calcularRaizCubicaNumeroMenor(x, y, z, m, n)
    print("El promedio, la mediana, el promedio multiplicativo, los número ordenados ascendentemente, los números ordenados descendentemente, el número mayor elevado al menor y la raiz cúbica del menor número de los 5 reales que se pusieron son", str(promedioF), ";", str(medianaF), ";", str(promedioMultiplicativoF), ";", str(ascendenteF),";", str(descendenteF),";", str(mayorElevadoMenorF),"y", str(numeroMenorF), "respectivamente.")
```
### 9. Consultar qué es y cómo funciona pip en python.
#### Solución
pip es el programa de instalación preferido. Desde Python 3.4 viene incluido por defecto con los instaladores binarios de Python.

Un entorno virtual es un entorno de Python parcialmente aislado que permite instalar paquetes para que los use una aplicación en particular, en lugar de instalarlos en todo el sistema.
### 10. Hacer un listado de módulos populares para python que se puedan instalar com pip y consultar cómo instalarlos.
#### Solución
* Tkinter. Tkinteres un módulo incorporado para el desarrollo de aplicaciones GUI (Interfaz Gráfica de Usuario). ...
* Numpy. Numpy se utiliza para la computación científica. ...
* Pandas. Pandas es un módulo de análisis de datos. ...
* Matplotlib. Matplotlib es una biblioteca de trazado de gráficos 2D. ...
* TensorFlow. ...
* Keras. ...
* Scikitt-Learn. ...
* Django.

Para instalar se hace el siguiente procedimiento:
```
pip install requests
pip install beautifulsoup4
pip install simplekml
```  
