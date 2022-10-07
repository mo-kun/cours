from saisir_réel import saisir_réel
from numpy import array


def saisir_tableau(n):
    t[0] = saisir_réel()
    for i in range(1, n):
        t[i] = saisir_réel()

        while t[i] < t[i - 1]:

            t[i] = saisir_réel()
    return t


t = array([float()] * 10)
