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
