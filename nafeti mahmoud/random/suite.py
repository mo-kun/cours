# suite definie par : 0! = 1 et n! = n * (n-1)! = n * (n-1) * … * 3 * 2 * 1 pour tout entier n > 0

def suite(p):
    if p == 1 or p == 2:

        return 1
    elif p > 2:
        return suite(p - 1) + suite(p - 2)


# P.P

x = 5
print(f" U{x} = {suite(x)}")
