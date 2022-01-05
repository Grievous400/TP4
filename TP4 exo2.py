# Demande le nombre d'étudiants à l'utilisateur
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0;
# déclaration d’une liste vide qui va contenir autant de notes que d'étudiants
notes = []
ecart=0



for i in range(nombreEtudiants):
    x = float(input(f"Note étudiant {i}:"))
    while 0>x or x>20:
        print("Valeur incorrecte")
        x=float(input(f"Note étudiant {i}:"))
    notes.append(x)

moyenne=sum(notes)/nombreEtudiants
print("Moyenne de classe",moyenne)

print("Numéro de l’Etudiant | note | ecart a la moyenne")

for i in range(nombreEtudiants):
    ecart=notes[i]-moyenne
    print(f"{notes[i]} | {round(moyenne,2)} | {round(ecart,2)}")

