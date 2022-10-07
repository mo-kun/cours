# programme de saisie un nombre réel r

def saisir_réel():
    r = float(input("réel = "))
    if r >= 0 and r <= 20:
        return r

    else:
        return saisir_réel()
