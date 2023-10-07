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