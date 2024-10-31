note1 = float(input("Entrez la première note : "))
if note1 > 20:
    print("Intervalle de note eronné la note doit etre sur 20")
else:
    note2 = float(input("Entrez la deuxième note: "))
    note3 = float(input("Entrez la troisième note: "))
    note4 =float(input("Entrez la quatrième note: "))
    note5 = float(input("Entrez la cinquième note: "))
    somme = note1 + note2 + note3 + note4 + note5
    moyenne = (somme) / 5
    print("Moyenne : ", moyenne)
    if moyenne >= 18:
        print("Élève Excellent")
    elif moyenne >= 16 and moyenne < 18:
        print("Élève Très bien")
    elif moyenne >= 14 and moyenne < 16:
        print("Élève Bien")
    elif moyenne >= 12 and moyenne < 14:
        print("Élève Assez bien")
    elif moyenne >= 10 and moyenne < 12:
        print("Élève Moyen")
    else :
        print("Élève Faible")