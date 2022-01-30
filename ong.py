
# Funcion que calcula e imprime el factorial de un numero
def obtener_factorial(numero):
    resultado = 1
    for i in range(1,numero+1):
        resultado *= i
    print(f"El factorial de {numero} es {resultado}")

# Funcion que calcula e imprime el resultado de la productoria de una lista de numeros
def obtener_productoria(lista):
    resultado = 1
    for i in lista:
        resultado *= i
    print(f"La productoria de {lista} es {resultado}")

# funcion que ejecuta las funciones de calcular factorial o productoria segun los argumentos entregados
def calcular(**kwargs):
    for k,v in kwargs.items():
        if "fact" in k:
            obtener_factorial(v)
        elif "prod" in k:
            obtener_productoria(v)

calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)
