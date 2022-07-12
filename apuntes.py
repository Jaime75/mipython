#print('Hola munto') # esto imprime en pantalla lo que esta entre parentesis
#x = 5 # se crea la variable x, ademas se le asigna el valor de 5

#nombre = 'Lucas' # se crea la variable nombre y se le asigna la cadena Lucas
#edad = 20
#print('Hola mundo, soy ' + nombre  + ' y tengo ' + str(edad) + ' años ') #ejemplo de uso
#texto = 'Hola mundo, soy ' + nombre + ' y tengo ' + str(edad) + ' años'
#print(texto)    # tambien se puede hacer de esta otra manera

# == igual
# >= mayor o igual
# != distinto

#edad = 18
#if edad >= 18: 
#    print('Es mayor de edad')
#else: 
#    print('Es menor de edad')

#nombre = input('¿Cómo te llamas?')
#print('Hola ' + nombre)
#edad = int(input('¿Cuántos años tienes?')) #int en esta parte permite despues emplear elementos de comparación dentro del if
#if edad >= 18:
#    print('Es mayor de edad')
#else:
#    print('Es menor de edad')

#edad = int(input('¿Cuántos años tienes?'))
#esMayorDeEdad = edad >= 18 #otra forma de hacer lo mismo que el anterior pero primero se genera una variable booleana
#if esMayorDeEdad:
#    print('Es mayor de edad')
#else:
#    print('Es menor de edad')

#edad = int(input('¿Cuántos años tienes?'))
#masDe12 = edad >= 12
#respuestaHijoDelDueño = input('Eres hijo del dueño')
#esHijoDelDueño = respuestaHijoDelDueño == 'si'
#puedePasar = masDe12 or esHijoDelDueño 
#if puedePasar:
#    print('Usted puede pasar a la montaña rusa')
#else:
#    print('No puede pasar')

# % modulo
# ** potencia

#numero = int(input('Ingrese un número'))
#if numero%2 == 0:
#    print('El número es par')
#else:
#    print('El números es impar')

# Calculadora de IMC
# IMC = peso / altura**2
# <19:delgadez
# entre 20 y 25: normal
# entre 26 y 30: sobrepeso
# > 30: obesidad
#peso = float(input('Introduzca su peso en kg \n'))
#altura = float(input('Introduzca su altura en Cm \n'))
#altura = altura/100
#imc = peso / altura**2
#print(imc)
#if imc < 20:
#    print('Usted esta delgado')
#if imc >=20 and imc < 26:
#    print('Su peso es normal')
#if imc > 26 and imc <= 30:
#    print('Usted tiene sobrepeso')
#if imc > 30:
#    print('Usted tiene obesidad')

#def funcionDePrueba(parametro1, parametro2):
#    print('El valor de los parametros son: ' + parametro1 + 'y tambien: ' + parametro2)

#funcionDePrueba('45', '60')

#def calcularIMC(peso, alturaEnMetros):
#    imc = peso / alturaEnMetros**2
#    return imc 

#def pedirElIMC():
#    peso = float(input('Ingrese su peso en kg'))
#    alturaEnCm = int(input('Ingrese su altura en cm'))
#    alturaEnMetros = alturaEnCm / 100
#    imc = calcularIMC(peso, alturaEnMetros)

#    print('Su IMC es de ' + str(imc))

#print('Calcular el IMC de la primer persona')
#pedirElIMC()
#print('Calcular el IMC de la segunda persona')
#pedirElIMC()
#print('Calcular el IMC de la tercer persona')
#pedirElIMC()

#contador = 0
#while contador < 5:
#    print("El valor del contador es: " + str(contador))
#    contador +=1

#contador = 0
#while contador <= 5:
#    if contador != 3:
#        print("El valor del contador es: " + str(contador))
#    contador +=1

#contador = -1
#while contador < 5:
#    contador += 1
#    if contador == 3:
#        continue
#    print("El valor del contador es: " + str(contador))
    
# Cuando se desea buscar algo de programación escribir en le buscador "stackoverflow python loQueEstoyBuscando"

#😀😄😆🤣😀

#seguirChateando = True
#while seguirChateando:
#    texto = input('>')
#    if texto == 'salir':
#        seguirChateando = False
#    texto = texto.replace(':)', '😀')
#    texto = texto.replace(':8', '😆')
#    texto = texto.replace(':9', '🤣')
#    texto = texto.replace(':(', '😀')
#    print(texto)

#arreglo = ['banana', 'melon', 'sandía', 'pera']

#for fruta in arreglo:
#    if fruta.endswith('a'):
#        print("La fruta es: " + fruta)

#for fruta in arreglo:
#    if fruta == 'sandía':
#        break
#    print("La fruta es: " + fruta)

#arreglo.reverse()

#for fruta in arreglo:
#    print("La fruta es: " + fruta)

#arreglo.remove('melon')
#arreglo.append('kiwi')

#for fruta in arreglo:
#    print("La fruta es: " + fruta)

#texto = "Hola mundo"
#for letra in texto:
#    print('letra: ' + letra)

#for numero in range(10):
#    print(numero)

#for numero in range(10):
#    if (numero > 5):
#        print(numero)

#for numero in range(6, 10):
#    print(numero)

#diccionario = {
#    "Programar": "Es transformar el cafe en código",
#    "POO": "Programación Orientada a Objetos"
#}

#print(diccionario["POO"])

#digitos = {
#    "0": "cero",
#    "1": "uno",
#    "2": "dos",
#    "3": "tres",
#    "4": "cuatro",
#    "5": "cinco",
#    "6": "seis",
#    "7": "siete",
#    "8": "ocho",
#    "9": "nueve"
#}

#numero = input("Introduce un numero: ")

#for dig in numero:
#    print(digitos[dig]) #aqui queda todo en lineas distintas

#numeroEnUnaLinea = ''
#for dig in numero:
#    numeroEnUnaLinea += digitos[dig] + ' '

#print(numeroEnUnaLinea)

#archivo = open('texto.txt', 'a') #crea un archivo, en este caso llamado texto.txt y lo abre
#archivo.write('Prueba de guardado en el archivo') #escribe en el archivo abierto
#archivo.close()# cierra el archivo abierto

#archivo1 = open('texto.txt', 'a')
#archivo1.write('podre gurdar mas texto en este mismo archivo?') #si se guarda, pero enseguida
#archivo1.close()

#archivo = open('texto.txt', 'r') #este parametro hace que sea de solo lectura
#print(archivo.read()) #aqui vemos directo en pantalla lo que contiene el archivo
#archivo2 = open('texto.txt', 'a') #el parametro 'a' permite agregar texto, 'w' para reemplazar
#archivo2.write('\n se guardara una segunda linea?')
#archivo2.close()
#archivo3 =open('texto.txt', 'a')
#archivo3.write('\n una vez abierto puedo seguir guardando texto')

#Ahora intentaré agregar texto desde un input
#def agregaTextoArchivo():
#    archivo4 = input('Escribe lo que quieres agregar: \n')
#    archivo5 = open('texto.txt', 'a')
#    archivo5.write('\n' + archivo4)
#    archivo5.close()
#    archivo6 = open('texto.txt', 'r')
#    print(archivo6.read())
#agregaTextoArchivo()

#def encriptar(textu):
#    textoFinal = ''
#    for letra in textu:
#        textoFinal += letra + 'x'
#    print('Texto Encriptado: ' + textoFinal)
#
#def desencriptar(textu):
#    print('El texto a desencriptar es: ' + textu)
#    textoFinal = ''
#    contador = 0
#    for letra in textu:
#            if contador % 2 == 0:
#            textoFinal += letra
#        contador += 1
#    print('Texto desencriptado:' + textoFinal)
#
#desencriptar('Hxoxlxax,x xcxoxmxox xexsxtxaxsx?x')

def encriptar(texto):
    textoFinal = ''
    for letra in texto:
        textoFinal += letra + 'x'
    return textoFinal

def desencriptar(texto):
    textoFinal = ''
    contador = 0
    for letra in texto:
        if contador % 2 == 0:
            textoFinal += letra
        contador += 1
    return textoFinal

def encriptarArchivo():
    archivo = open('texto.txt', 'r')
    texto = archivo.read()
    archivo.close()
    textoEncriptado = encriptar(texto)

    archivo = open('texto.txt', 'w')
    archivo.write(textoEncriptado)
    archivo.close()

#encriptarArchivo()

def desencriptarArchivo():
    archivo = open('texto.txt', 'r')
    texto = archivo.read()
    archivo.close()
    textoDesencriptado = desencriptar(texto)

    archivo = open('texto.txt', 'w')
    archivo.write(textoDesencriptado)
    archivo.close()

desencriptarArchivo()