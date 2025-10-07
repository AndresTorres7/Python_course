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
