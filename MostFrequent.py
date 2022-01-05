liste = [2, 7, 5, 6, 6,6,7, 1, 6, 2, 1, 7, 6]
max=liste[0]
for i in range (1,len(liste)):
    if liste[i]>max:
        max=liste[i]
print("La valeur maximal est",max)
varmax=0
max=0
for i in liste:
    count=0
    for j in liste:
        if i==j:
            count+=1
    if count>max:
        max=count
        varmax=i

print("Nombre le plus fréquents et son nombre de répititions",varmax,max)




