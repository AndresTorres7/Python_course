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
