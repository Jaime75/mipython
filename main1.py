from empleado1 import Empleado
from cliente1 import Cliente

#emp = Empleado('Jaime', 'Esq', '123', '3112', '100')
#cli = Cliente('Rox', 'Mor', '234', '3232', 'may')


def cargar():
    respuesta = input('¿Va a agregar un empleado?')
    nombre = input('Ingrese el nombre: ')
    apellido = input('Ingrese el apellido')
    dni = input('Ingrese el dni: ')
    telefono = input('Ingrese el telefono')

    if (respuesta == 'si'):
        salario = input('Ingrese el salario')
        emp = Empleado(nombre, apellido, dni, telefono, int(salario))
        personas.append(emp)
    else:
        categoria = input('Ingrese la categoría: ')
        cli = Cliente(nombre, apellido, dni, telefono, categoria)
        personas.append(cli)

personas = []
cargar()
cargar()

for persona in personas:
    print(persona)
