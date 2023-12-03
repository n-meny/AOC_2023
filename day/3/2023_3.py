from aoctools import *
aocd = AOCD(2023, 3)
puzzle = aocd.as_str

liste_puzzle = puzzle.split("\n")




for i,ligne in enumerate(liste_puzzle) :
    for j,caractere in enumerate(ligne) :

        if ligne[i+1][j] == "*" :
            print(caractere)

