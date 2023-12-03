alphabet_minuscule = [chr(i) for i in range(97, 123)]
alphabet_majuscule = [chr(i) for i in range(65, 91)]


print(alphabet_minuscule)



solution = 0
clé = ""
clé2 = ""
for mot in puzzle :
    for caractere in mot :
        if not caractere.isdigit() :
            clé += caractere 
        match clé:
            case "one":
                clé2 += "1"
                clé = ""
            case "two":
                clé2 += "2"
                clé = ""
            case "three":
                clé2 += "3"
                clé = ""
            case "four":
                clé2 += "4"
                clé = ""
            case "five":
                clé2 += "5"
                clé = ""
            case "six":
                clé2 += "6"
                clé = ""
            case "seven":
                clé2 += "7"
                clé = ""
            case "eight":
                clé2 += "8"
                clé = ""
            case "nine":
                clé2 += "9"
                clé = ""
            case "zero":
                clé2 += "0"
                clé = ""
            case _:
                clé2 += ""
                #expression_par_defaut
    if len(clé2) > 1 :
        solution += int(clé2)
        clé2 = ""
    else : solution = 0#solution += int(clé2[0] + clé2[-1])



#aocd.p1(solution)

print(solution)

