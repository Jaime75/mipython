def calcularPromedio(n1, n2, n3):
    promedio = (n1 + n2 + n3) / 3
    return promedio

def pedirDatosPromedio():
    n1 = float(input('Cual es la primer nota: \n'))
    n2 = float(input('Cual es la segunda nota: \n'))
    n3 = float(input('Cual es la tercer nota: \n'))
    promedio = calcularPromedio(n1, n2, n3)
    print('El promedio de las 3 notas es: \n' + str(promedio))

def calcularDistancia(velocidad, tiempo):
    distancia = velocidad * tiempo
    return distancia

def pedirDatos():
    velocidad = float(input('Cuál es la velocidad del móvil? \n'))
    tiempo = int(input('Cuál es el tiempo que esta en movimiento? \n'))
    distancia = calcularDistancia(velocidad, tiempo)
    print('La distancia recorrida por el móvil es: '+ str(distancia))


def textos():
    print('Para calcular la distancia presiona "a" ')
    print('Para calcular el promedio de 3 notas presiona "b" ')
    print('Para salir presiona "x"')

textos()

respuestaPregunta = input('Que desea hacer?: \n')

if respuestaPregunta == 'a':
    pedirDatos()

if respuestaPregunta == 'b':
    pedirDatosPromedio()

if respuestaPregunta == 'x':
    print('Hasta pronto')