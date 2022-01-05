x=float(input(("Vous cherchez la table de multiplication de quel nombre ?")))

for i in range(0,10):
    liste=[i,x,round(i*x,2)]
    print(f"{x}","x",f"{i}=",liste[2])