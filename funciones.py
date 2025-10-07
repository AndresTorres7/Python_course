def mi_funcion():
    print("Hola mundo desde una función")


mi_funcion()


def saludar(nombre, apellido=""):
    print("Hola", nombre, apellido)


# saludar("Andres", "Torres")
# saludar("Andres")


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


resultado = sumar(2, 3)
# print(resultado)

# print(dividir(10, 2))

# Funcion lambda; función pequeña y anónima.

x = lambda a, b: a + b

print(x(2, 3))


def mifuncion(n):
    return lambda a: a * n


duplicador = mifuncion(2)
triplicador = mifuncion(3)
quintuplicador = mifuncion(5)
print(quintuplicador(10))

print(duplicador(4))
print(quintuplicador(10))
