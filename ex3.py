nbj = float(input("Donner Les Nombre Des Jours de travaille :"))
cj = float(input("Donner Le Coût Horraire en DH :"))
sb = nbj * cj
anc = sb*(5/100)
sbrut = sb + anc
print("Salaire brut est  :  ",sbrut)
if sbrut < 3000 :
    print("Pas de prime")
elif sbrut >= 3000 and sbrut < 4000 :
    print("Accorde Prime")
else:
    print("Intervalle du prime non valide")
