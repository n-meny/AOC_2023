from aoctools import *
aocd = AOCD(2023, 2)
puzzle = aocd.dict_split_at(":")
b = "blue"
r = "red"
g = "green"
nb_bleu = 0
nb_rouge = 0
nb_verte = 0

# 12 rouge, 13 vert, 14 bleu
valide = False
s1 = 0
for game in puzzle :
    tentatives = puzzle[game].split(";")
    for j  in range(0, len(tentatives)) :
        tentative = tentatives[j].split(",")
        for choix in tentative :
            tirage = choix.split(" ")
            match tirage[2] :
                case "blue" :
                    nb_bleu = int(tirage[1])
                case "red" :
                    nb_rouge = int(tirage[1])
                case "green" :
                    nb_verte = int(tirage[1])
            if nb_bleu <= 14 and nb_rouge <= 12 and nb_verte <= 13 :
                valide = True
            else : 
                valide = False
                break
        if not valide : 
            nb_bleu = 0
            nb_rouge = 0
            nb_verte = 0
            break
    if valide : 
        s1 += int(game[5:])
        valide = False

print(s1) 
aocd.p1(s1)

## le maximum de 1 tentative multiplié ensemble puis additionné



max_blue = 0
max_rouge = 0
max_vert = 0
s2 = 0
for game in puzzle :
  #  print(puzzle[game])
    tentatives = puzzle[game].split(";")
    for j  in range(0, len(tentatives)) :
        tentative = tentatives[j].split(",")
        for choix in tentative :
            tirage = choix.split(" ")
            match tirage[2] :
                case "blue" :
                    nb_bleu = int(tirage[1])
                    if nb_bleu > max_blue : max_blue = nb_bleu
                case "red" :
                    nb_rouge = int(tirage[1])
                    if nb_rouge > max_rouge : max_rouge = nb_rouge
                case "green" :
                    nb_verte = int(tirage[1])
                    if nb_verte > max_vert : max_vert = nb_verte
           # print("max blue : ", max_blue, " max red : ", max_rouge, " max vert : ", max_vert)
    s2 += (max_blue*max_rouge*max_vert)
    max_blue = 0
    max_rouge = 0
    max_vert = 0

#print(s2)
aocd.p2(s2)
