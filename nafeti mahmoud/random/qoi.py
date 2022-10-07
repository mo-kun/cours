# programme qui retouner le plus grande nombre
def qoi(a, b):
    if a - b >= 0:
        return a
    else:
        return(qoi(b, a))


# P.P

a = int(input("A = "))
b = int(input("B = "))

print(qoi(), "est le plus grander nombre ")
