from aoctools import *
aocd = AOCD(2022, 3)
puzzle_input = aocd.slist



#puzzle_input = ["vJrwpWtwJgWrhcsFMMfFFhFp","jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL","PmmdzqPrVvPwwTWBwg","wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn","ttgJtRGJQctTZtZT","CrZsJsPPZsGzwwsLwLmpwMDw"]
#print(puzzle_input)
#puzzle_input = ["vJrwpWtwJgWrhcsFMMfFFhFp"]
solution = 0
for sac in puzzle_input :

    item1 = sac[len(sac) // 2:]
    item2 = sac[:len(sac) // 2]

    for lettre1 in item1 :
        for lettre2 in item2 :
            if lettre2 == lettre1 :
                if ord(lettre1) <= ord("Z") :
                    clé = ord(lettre1)
                    solution += (ord(lettre1) - 38)
                    break
                else :
                    clé = ord(lettre1)
                    solution += (ord(lettre1) - 96)
                    break
                    
        if lettre1 == lettre2 : 
            break


solution2 = 0
for i in range(0,len(puzzle_input),3) :
    item1 = puzzle_input[i]
    item2 = puzzle_input[i+1]
    item3 = puzzle_input[i+2]

    for l1 in item1 :
        for l2 in item2 :
            for l3 in item3 :
                if l3 == l1 and l3 == l2 :
                    if ord(l3) <= ord("Z") :
                        solution2 += (ord(l3) - 38)
                        break
                    else :
                        solution2 += (ord(l3) - 96)
                        break
                    
            if l3 == l1 and l3 ==l2 : break
        if l3 == l1 and l3 ==l2 : 
            
            break
        


aocd.p1(solution)   
aocd.p2(solution2)      

#dernier_mot = puzzle_input[-1] 
#print(puzzle_input[-1])

#print(dernier_mot[len(dernier_mot) // 2:])
#print(dernier_mot[: len(dernier_mot) //2])
#print(dernier_mot[0:24], "  ici   ")
#print(dernier_mot[25:42], " la ")
#print(clé)


#print(ord("a"), " --> ", ord("z"))
#print(ord("A"), " --> ", ord("Z"))
#print(ord("a")-96)

#print(ord("L") -38)

#print(ord("L"))

