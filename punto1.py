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