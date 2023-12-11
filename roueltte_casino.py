import random
credits = 100
plafond_augmentation_mise = 130
plafond_max = 200
nb_parties = 240
ok = 0 
pas_ok = 0
palier1 = 0
palier2 = 0
palier3 = 0

save = 0
max_atteint = credits

def lancer_roulette(mise) :

    nombre = random.randint(0, 36)

    if nombre >= 0 and nombre <= 24 :
        gain = mise * 36
    else :
        gain = 0

    return(gain)


for i in range(0, nb_parties) :
    print("partie : ", i+1, " credits : ", credits)
    if credits > max_atteint : max_atteint = credits
    credit_prec = credits
    if credits >= 12.5 and credits < plafond_augmentation_mise :
        palier1 += 1
        credits -= 12.5
        credits += lancer_roulette(0.5)
    elif credits >= plafond_augmentation_mise and credits < plafond_augmentation_mise*2 :
        palier2 += 1
        credits -= 25
        credits += lancer_roulette(1)
    elif credits >= plafond_augmentation_mise*2 and credits < plafond_max :
        palier3 += 1
        credits -= 50
        credits += lancer_roulette(2)
    elif credits >= plafond_max :
        save += credits - 50
        credits = 50
    if lancer_roulette(0.5) > 0 :
        ok += 1 
    else :
        pas_ok += 1


    
print("lancer gagnant : ", ok, " lancer perdant : ", pas_ok, " pourcentage : ", ok/(ok+pas_ok)*100, "%")
print("credits restant : ", credits) 
print("palier 1 : ", palier1, " palier 2 : ", palier2, " palier 3 : ", palier3)
print("credits sauvegardés : ", save)
print("max atteint : ", max_atteint)




for i in range(0, 10) :
    cash = 100
    for i in range(0, nb_parties) :
        if cash >= 25 :
            cash -= 25
            cash += lancer_roulette(1)
        #print("partie ", i+1, "cash :", cash)
    print("cash restant : ", cash)