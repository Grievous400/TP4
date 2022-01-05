Liste=[]


x=input("Donnez une date :")
Liste.append(x)
jour=int(x[0:2])
mois=int(x[2:4])
annee=int(x[4:8])
if jour > 31:
    print("Jour impossible")
    x = (input("Date incorrecte : Redonnez une date :"))
if mois > 12:
    print("mois impossible")
    x = (input("Date incorrecte : Redonnez une date :"))

while (len(str(x[0:8])))!=8 or jour>31 or mois>12 :
    x =(input("Date incorrecte : Redonnez une date :"))

    jour = int(x[0:2])
    mois = int(x[2:4])
    annee = int(x[4:8])
    Liste.append(x)

    if (len(str(x[0:8])))==8:
        break
if x[0:4] = 2902 :
    print("L'année est bissextile")

if annee%4==0 and annee %100!=0:
    print("L'année est bissextile")
elif annee%400==0:
    print("L'année est bissextile")
else:
    print("L'année n'est pas bissextile")
if annee%4==0 and annee %100!=0 and annee%400==0:
    print("l'année possède 366 jour et février a 29 jours ")
else:
    print("l'année possède 365 jour, c'est une année commune ")