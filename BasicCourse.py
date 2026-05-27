# open(nombre, modo)

# # r (read)
# w (write)
# x (crete new one)

try:
    with open("archivo.txt", "r") as f:
        print(f.readline())
        print(f.readline())
except FileNotFoundError:
    print("El archivo no existe")


try:
    with open("archivo.txt", "a") as f:
        f.write("\n")
        f.write("Hola mundo desde write en el with")
    with open("archivo.txt", "r") as f:
        print(f.read())

except FileNotFoundError:
    open("archivo.txt", "x")
    print("El archivo no existe")

# 2
i = 0

while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)
else:
    print("i dejó de ser menor a 10")

    # bucle for

palabra = "Python"

for letra in palabra:
    print(letra)

frutas = ["Apple", "Orange", "Kiwi"]
adjetive = ["tasty", "healthy"]

for fruta in frutas:
    if fruta == "Orange":
        continue
    print(fruta)

for fruta in frutas:
    for ad in adjetive:
        print(fruta, ad)

# 3
saludo = "Hola"
nombre = "Mundo"
print(saludo)
print(nombre)

# 4
name = "Andres Felipe"
last_name = "    Ramos Torres"
print(5 * name)
print(name + " " + last_name)
print(len(name))
print(name.lower())
print(name.upper())
print(last_name.strip())

# 5
x = 10
y = 5.678
z = 1.2e6
a = 1.2e-6

print(type(x))
print(type(y))
print(z)
print(a)

# 6
# Operadores numéricos
a = 10
b = 3
print("suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a / b)
print(4**2)

# 7
nombre = input("Ingrese su nombre:  ")
print(nombre)
age = int(input("Ingrese su eddad:   "))
print(type(age))

# 8
# frutas = {"apple", "orange", "mandarine", "orange"}
# print(frutas)
# print(type(frutas))
# print(len(frutas))

# conjuntos = {"python", 156, True}
# print(conjuntos)
# print(type(conjuntos))

# frutas.add("pear")
# print(frutas)

# tropicalfruits = {"mango", "piña"}
# frutas.update(tropicalfruits)
# print(frutas)

# frutas.remove("mango")
# print(frutas)

a = {"a", "b", "c"}
b = {"c", "d", "e"}
c = a.union(b)

print(c)

i = a.intersection(b)

print(i)

d = a.difference(b)
print(d)

# 9

auto = {"marca": "Renault", "modelo": "Clio", "año": 2025}

print(auto)
print(auto["marca"])
print(auto.get("marca"))

print(auto.keys())
print(auto.values())

if "marca" in auto:
    print("Marca es una de las propiedades de este diccionario")

auto["año"] = 2020
print(auto)

auto["color"] = "Verde"
print(auto)

auto.update({"año": 2022, "puertas": "cuatro"})
print(auto)

# auto.pop("puertas")
# print(auto)

# auto.clear()
# print(auto)

for k in auto:  # keys
    print(k)

print("---")
for k in auto.values():
    print(k)

print("----")

for k, v in auto.items():  # key and values
    print(k, v)

# Diccionarios anidados
print("------------------")
familia = {
    "hijo1": {"nombre": "pedro", "edad": 8},
    "hijo2": {"nombre": "Ana", "edad": 15},
    "hijo3": {"nombre": "ANDY", "edad": 4},
}

print(familia)
print(familia["hijo1"]["edad"])

# 10


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
print
(quintuplicador(10))

# 11

# frutas = ["Manzana", "Naranaja", "Mandarina"]

# print(frutas)
# print(type(frutas))

# frutas[1] = "Banana"

# print(frutas[1])

# print(frutas)

# vehiculos = ["Auto", "Moto", "Avion"]

# # Métodos
# vehiculos.append("Barco")
# print(vehiculos)

# Insert
# vehiculos.insert(1, "Bicicleta")
# print(vehiculos)
# vehiculos.remove("Auto")
# print(vehiculos)

# vehiculos.pop(1)
# print(vehiculos)


# TUplas
tecnologias = ("python", "javascript", "go", "python")

print(tecnologias)
print(tecnologias[1])
print(len(tecnologias))

fruta = ("manzana",)
print(type(fruta))

tupla = ("python", 5, True)
print(tupla)

x, y, z = tupla
print(x)
print(y)
print(z)

tupla1 = (1, 2, 3)
tupla2 = (3, 4, 5)
tupla3 = tupla1 + tupla2
print(tupla3)

for item in tupla:
    print(item)

# 12
import unicodedata


def quitar_tildes(texto: str):
    nfkd = unicodedata.normalize("NFD", texto)
    return "".join(c for c in nfkd if not unicodedata.combining(c))


dia = input("Escribe un día:  ")
dia = quitar_tildes(dia)

match dia.strip().lower():
    case "lunes":
        print("Today is monday")
    case "martes":
        print("Today is tuesday")
    case "miercoles":
        print("Today is wednesday")
    case "jueves":
        print("Today is thursday")
    case "viernes":
        print("Today is friday")
    case "sabado":
        print("Today is saturday")
    case "domingo":
        print("Today is sunday")

# 13
# Este es un comentario
"""
Este es un comentario multilinea
"""
if 4 > 3:  # Probando identación
    if 5 > 3:
        print("5 es mayor a 3")

    print("4 es mayor a 3")


### Clase Variables

x, y, z = "Manzana", "Naranaja", "Banana"
print(x, y, z)

a = b = c = "Mandarina"

print(a, b, c)

print("Mi fruta favorita es " + x)
print(a + " " + z)

# 14
try:
    numero = 10 / 0

except ZeroDivisionError:
    print("No se puede dividir por cero")

try:
    print(x)
except NameError:
    print("Esta variable no ha sido definida")
finally:
    print("Esto se ejecuta independientemente de error o no")
