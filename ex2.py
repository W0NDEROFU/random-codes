nbj = int(input("Donner Les Nombre Des Jours de travaille :"))
ch = int(input("Donner Le Coût Horraire en DH :"))
salaire_base = nbj * ch
anciennete = salaire_base*(5/100)
salaire_brut = salaire_base + anciennete
print("Salaire de base : ", salaire_base)
if nbj >= (365*2)+1 :
    anciennete = salaire_base*(5/100)
    salaire_brut = salaire_base + anciennete
    print("Salaire Brut : ", salaire_brut)
elif nbj >= (365*5) and nbj < (365*3) :
    anciennete = salaire_base*(10/100)
    salaire_brut = salaire_base + anciennete
    print("Salaire Brut : ", salaire_brut)
elif nbj >= (365*15) and nbj < (365*5) :
    anciennete = salaire_base*(15/100)
    salaire_brut = salaire_base + anciennete
    print("Salaire Brut : ", salaire_brut)
elif nbj >= (365*20) and nbj < (365*15) :
    anciennete = salaire_base*(20/100)
    salaire_brut = salaire_base + anciennete
    print("Salaire Brut : ", salaire_brut)
else :
    anciennete = salaire_base
    print("Salaire Brut : ", salaire_brut)

