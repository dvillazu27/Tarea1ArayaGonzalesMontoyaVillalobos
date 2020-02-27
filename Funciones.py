def Min_May(entrada):
    nuevaPalabra = ""

    if (type(entrada) == str):
        for i in entrada:
            if i in ("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"):
                return "ERROR: HAY LETRAS MAYÚSCULAS"

            elif i in ("abcdefghijklmnñopqrstuvwxyz"):
                i = chr(ord(i) - 32)

            nuevaPalabra = nuevaPalabra + i

        return nuevaPalabra

    else:
        return "ERROR: LAS ENTRADA NO ES DE TIPO STRING"


def findW(entrada):
    if (type(entrada) == str):

        if "w" in entrada:
            return "Se encontró la letra w"

        else:
            return "No fue posible hallar la letra w"

    else:
        return "ERROR: LA ENTRADA NO ERA UN STRING"


def resta(num1, num2):

    resta = 0
    if (type(num1) == int) & (type(num2) == int):

        if (num1 >= 0) & (num2 >= 0):
            resta = num1 - num2

            if (resta >= 0):
                return resta
            else:
                return "ERROR: LA RESTA DE LOS NÚMEROS ES NEGATIVA"
        else:
            return "ERROR: ALGÚN NUMERO INGRESADO ES NEGATIVO"

    else:
        return "ERROR: LAS ENTRADAS NO ERAN NUMEROS ENTEROS"
