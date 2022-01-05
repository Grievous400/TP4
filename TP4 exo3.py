n=int(input("Quellle est la taille de vos vecteurs :"))
nMax=3
v1=[]
v2=[]
while n<1 or n>nMax:
    n = int(input("Quellle est la taille de vos vecteurs :"))


print("Saisie du premier vecteur :")

for i in range(n):
    x1=int(input(f"v1[{i}]="))
    v1.append(x1)

print("Saisie du second vecteur :")

for i in range(n):

    x2 = float(input(f"v2[{i}]="))
    v2.append(x2)


scal=0
for i in range(n):
    scal=v1[i]*v2[i]+scal
print("Le produit scalaire de v1 et v2 :",scal)