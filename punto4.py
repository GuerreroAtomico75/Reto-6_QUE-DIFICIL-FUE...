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