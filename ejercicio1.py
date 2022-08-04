
from cmath import sqrt

def calcularPerimetroRectangulo(base, altura):
    perimetro = base * 2 + altura * 2
    return perimetro

def calcularAreaRectangulo(base, altura):
    area = base * altura
    return area

def pedirDatosRectangulo():
    base = float(input('Cual es la medida de la base del rectángulo?: \n'))
    altura = float(input('Cual es la altura del rectángulo?: \n'))
    perimetro = calcularPerimetroRectangulo(base, altura)
    area = calcularAreaRectangulo(base, altura)
    print('El perimetro del rectángulo es: ' + str(perimetro) + ' el área del rectángulo es: ' + str(area))

def calcularDistanciaDosPuntos(x1, y1, x2, y2):
    distancia = sqrt((x2-x1)**2 +(y2 - y1)**2)
    return distancia

def pedirCoordenadas():
    x1 = float(input('Introduzca el valor de la abscisa del primer punto: '))
    y1 = float(input('Introduzca el valor de la ordenada del primer punto: '))
    x2 = float(input('Introduzca el valor de la abscisa del segundo punto: '))
    y2 = float(input('Introduzca el valor de la ordenada del segundo punto: '))
    distancia = calcularDistanciaDosPuntos(x1, y1, x2, y2)
    print('La distancia es: ' + str(distancia))

def calcularPuntaje(correctas, incorrectas, blanco):
    puntaje = (correctas * 3 + incorrectas * (-1) + blanco * 0)
    return puntaje

def pedirDatosPuntaje():
    correctas = int(input('Cuantas respuestas correctas son?: \n'))
    incorrectas = int(input('Cuantas respuestas incorrectas son?: \n'))
    blanco = int(input('Cuantas preguntas en blanco son?: \n'))
    puntaje = calcularPuntaje(correctas, incorrectas, blanco)
    print('El puntaje final es: ' + str(puntaje))

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
    print('Para calcular el puntaje presiona "c" ')
    print('Para calcular la distancia entre 2 puntos presiona "d"')
    print('Para calcular el perimetro y el área de un rectángulo presione "e"')
    print('Para salir presiona "x"')


def pregunta():
    textos()

    respuestaPregunta = input('Que desea hacer?: \n')

    if respuestaPregunta == 'a':
        pedirDatos()
        pregunta()

    if respuestaPregunta == 'b':
        pedirDatosPromedio()
        pregunta()
    
    if respuestaPregunta == 'c':
        pedirDatosPuntaje()
        pregunta()

    if respuestaPregunta == 'd':
        pedirCoordenadas()
        pregunta()

    if respuestaPregunta == 'e':
        pedirDatosRectangulo()
        pregunta()

    if respuestaPregunta == 'x':
        print('Hasta pronto')
        

pregunta()