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