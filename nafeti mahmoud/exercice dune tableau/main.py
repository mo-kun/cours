# PP
from saisir_entier import saisir_entier
from dihotomique import dichotomique

from saisir_tab import saisir_tableau

n = saisir_entier()
print("Saisie des n réels :")
t = saisir_tableau(n)

r = float(input("Donner le nombre réel à chercher : "))

if dichotomique(0, n - 1, r, t):
    print(r, "existe dans la liste de", n, "réels.")
else:
    print(r, "n'existe pas dans la liste de", n, "réels.")
