# suite definie par : U0 = 1 et Un = (-2)**n / Un-1 pour tout entier > 0
def suite(n):
    if n == 0:
        return 1
    elif n > 0:
        return (-2)**n / suite(n - 1)


# pp
n = int(input("N = "))
print(suite(n))
