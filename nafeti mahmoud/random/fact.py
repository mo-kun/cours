# factoriell d'une nombre x
def fact(p):
    if p == 1 or p == 0:

        return 1
    elif p > 1:
        return p * fact(p - 1)


# P.P

x = 500

print(f"factoriel du {x} = {fact(x)}")
