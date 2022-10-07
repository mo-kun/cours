# programme de palindrome d'une mot ch

def verif(ch):
    L = len(ch)
    if L == 0 or L == 1:
        return True
    elif ch[0] == ch[L - 1]:
        ch = ch[1:L - 1]
        return verif(ch)
    else:
        return False


# pp
ch = input("Donner ch : ")
if verif(ch):
    print(ch, "palindrome")
else:
    print(ch, "nes pas palindrome")
