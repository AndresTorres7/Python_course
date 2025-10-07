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
