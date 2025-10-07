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
