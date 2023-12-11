from aoctools import *
aocd = AOCD(2023, 3)
puzzle = aocd.as_str

liste_puzzle = puzzle.split("\n")

print(liste_puzzle)

nombre = ""
for i,ligne in enumerate(liste_puzzle) :
    for j,caractere in enumerate(ligne) :
        if caractere.isnumeric() :
            nombre += caractere
            #diag_haut_gauche = ligne[i-1][j-1]
            if ligne[i-1][j-1] != "." and not ligne[i-1][j-1].isnumeric() or ligne[i-1][j] != "." and not ligne[i-1][j].isnumeric() :
                print("ok")
            if ligne[j+1].isnumeric() :
                nombre+= caractere
                j += 1
                if ligne[j+2].isnumeric() :
                    nombre += caractere
                    j+=2
            match len(nombre) :
                case 1 :
                    if liste_puzzle[i-1][j] != "."  and not liste_puzzle[i-1][j].isnumeric() :
                        print("ok")
            #print(caractere)
            
        
       # if ligne[i+1][j ] == "*" :
            #print(caractere)

def recherche_valideur(position, taille_nombre) :
    for i in range(-1, taille_nombre+1) :
        if i :
            print("ok")

