# sum d'une nombre x
def som(s):
    if s == 0:
        return 0

    elif s >= 1:
        return s + som(s - 1)


# s.s

s = 1

print(f"som du {s} = {som(s)}")
