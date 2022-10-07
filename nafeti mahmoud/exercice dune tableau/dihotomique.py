def dichotomique(deb, fin, r, t):
    milieu = (deb + fin) // 2
    if r == t[milieu]:
        return True
    elif (r < t[milieu]) and (deb < milieu):
        return dichotomique(deb, milieu - 1, r, t)
    elif (r > t[milieu]) and (fin > milieu):
        return dichotomique(milieu + 1, fin, r, t)
    else:
        return False
        