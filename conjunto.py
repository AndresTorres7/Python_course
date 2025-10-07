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
