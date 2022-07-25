pregunta1 = "¿Qué desea hacer?"
textoInicial = 'Para calcula distancia presione "a" '

def calcularDistancia(velocidad, tiempo):
    distancia = velocidad * tiempo
    return distancia

def pedirDatos():
    velocidad = float(input('Cuál es la velocidad del móvil? \n'))
    tiempo = int(input('Cuál es el tiempo que esta en movimiento? \n'))
    distancia = calcularDistancia(velocidad, tiempo)
    print('La distancia recorrida por el móvil es: '+ str(distancia))

pedirDatos()