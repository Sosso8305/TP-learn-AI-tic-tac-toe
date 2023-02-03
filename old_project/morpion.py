TAILLE_GRILLE=3
CDT_VICTOIRE=3
SYMBOLE=["O","X"]
joueur=False

def initialiserGrille(taille):
    grille=[]
    for x in range(taille):
        ligne=[]
        for y in range(taille):
            ligne.append(" ")
            grille.append(ligne)
    return grille

def afficheGrille(grille, taille):
    soluce="┌"+"───┬"*(taille-1)+"───┐"
    for y in range(taille):
        soluce=soluce+"\n│ "
        for x in range(taille):
            soluce=soluce+grille[x][y]+" │ "
            if y!=taille-1:
                soluce=soluce+"\n├"+"───┼"*(taille-1)+"───┤"
            else:
                soluce=soluce+"\n└"+"───┴"*(taille-1)+"───┘"
    print(soluce)


def estLibre(grille,x,y):
    if 0<=x<TAILLE_GRILLE and 0<=y<TAILLE_GRILLE :
        return grille[x][y]==" "
    else:
        return False

def grillePleine(grille, taille):
    for x in range(taille):
        for y in range(taille):
            if estLibre(grille,x,y):
                return False
    print("C'est plein")
    return True

def placerPion(symbole,grille):
    x=int(input("Entrée la coordonées en x"))
    y=int(input("Entrée la coordonées en y"))
    while not estLibre(grille, x, y):
        x=int(input("Rentrée la coordonées en x"))
        y=int(input("Rentrée la coordonées en y"))
    grille[x][y]=symbole
    return x,y

def coupGagantHori(grille,x,y,symbole):
    somme=1
    k=x-1
    while k>=0 and grille[k][y]==symbole:
        somme+=1
        k-=1
    k=x+1
    while k<TAILLE_GRILLE and grille[k][y]==symbole:
        somme+=1
        k+=1
    if somme==CDT_VICTOIRE:
        return True
    else:
        return False

def coupGagantVert(grille,x,y,symbole):
    somme=1
    k=y-1
    while k>=0 and grille[x][k]==symbole:
        somme+=1
        k-=1
    k=y+1
    while k<TAILLE_GRILLE and grille[x][k]==symbole:
        somme+=1
        k+=1
    if somme==CDT_VICTOIRE:
        return True
    else:
        return False

def coupGagantDia1(grille,x,y,symbole):
    somme=1
    k=1
    while x-k>=0 and y-k>=0 and grille[x-k][y-k]==symbole:
        somme+=1
        k+=1
    k=1
    while x+k<TAILLE_GRILLE and y+k<TAILLE_GRILLE and grille[x+k][y+k]==symbole:
        somme+=1
        k+=1
    if somme==CDT_VICTOIRE:
        return True
    else:
        return False

def coupGagantDia2(grille,x,y,symbole):
    somme=1
    k=1
    while x-k>=0 and y+k<TAILLE_GRILLE and grille[x-k][y+k]==symbole:
        somme+=1
        k+=1
    k=1
    while x+k<TAILLE_GRILLE and y-k>=0 and grille[x+k][y-k]==symbole:
        somme+=1
        k+=1
    if somme==CDT_VICTOIRE:
        return True
    else:
        return False

def coupGagant(grille,x,y,symbole):
    return (coupGagantDia2(grille,x,y,symbole) or coupGagantDia1(grille,x,y,symbole) or coupGagantVert(grille,x,y,symbole) or coupGagantHori(grille,x,y,symbole))





grille=initialiserGrille(TAILLE_GRILLE)
afficheGrille(grille, TAILLE_GRILLE)
x,y=placerPion(SYMBOLE[joueur], grille)
while (not grillePleine(grille, TAILLE_GRILLE)) and (not coupGagant(grille,x, y, SYMBOLE[joueur])):
    joueur=not joueur
    afficheGrille(grille, TAILLE_GRILLE)
    x,y=placerPion(SYMBOLE[joueur], grille)

if joueur and coupGagant(grille, x, y, SYMBOLE[joueur]):
    print("Le deuxième joueur a gagner")
elif coupGagant(grille, x, y, SYMBOLE[joueur]):
    print("Le premier joueur a gagner")
