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