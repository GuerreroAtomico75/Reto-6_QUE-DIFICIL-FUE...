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