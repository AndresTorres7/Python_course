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
