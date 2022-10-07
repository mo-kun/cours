# programme de saisie un nombre entier n

def saisir_entier():
    n = int(input("entier = "))
    if n <= 10 and n >= 5:
        return n

    else:
        return saisir_entier()
