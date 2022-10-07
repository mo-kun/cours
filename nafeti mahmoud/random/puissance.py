# puissance d'une nombre x et y

def puissance(a, b):
    if b == 0:
        return 1
    elif b > 0:
        return a * puissance(a, b - 1)
    else:
        return 1 / puissance(a, -b)


# P.P

a = int(input("Donner a : "))
b = int(input("Donner b : "))

print(f"La puissance de {a}**{b} = {puissance(a,b)}")
