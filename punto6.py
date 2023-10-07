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