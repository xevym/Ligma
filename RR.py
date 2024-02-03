import random
import time
shots = random.randint(4,8)
twoje = 0
healthyou = 3
healthenemy = 3
healthlose = 0
enemypick = 0

print("-------------------------------------------")
print("-WELCOME TO R.R.-")
print("-------------------------------------------")
time.sleep(1)
while True:
    print("-There are", shots, "chambers loaded.-")
    print("Your health:", healthyou)
    print("Enemy health:", healthenemy)
    time.sleep(1)
    twoje = input("Do you wish to fire? Y/N")
    print("-------------------------------------------")
#If you say yes
    if (twoje == 'Y'):
        shots = shots-1
        healthlose = random.randint(1,shots)
        if (healthlose == 1 and twoje == "Y"):
            print("You lost 1 health point.")
            print("-------------------------------------------")
            healthyou = healthyou-1
        else:
            print("You successfully avoided losing a health point!")
            print("-------------------------------------------")
            time.sleep(1)
#If you say no  
    if (twoje == 'N'):
        enemypick = random.randint(1,2)
        if (enemypick == 1):
            shots = shots-1
            healthlose = random.randint(1,shots)
            if (healthlose == 1 and twoje == "N"):
                print("Your enemy lost 1 health point!")
                print("-------------------------------------------")
                healthenemy = healthenemy-1
            else:
                print("Your enemy successfully avoided losing a health point!")
                print("-------------------------------------------")
                time.sleep(1)
        if (enemypick == 2):
            print("Your enemy passes you the weapon...")
            shots = shots-1
            healthlose = random.randint(1,shots)
            if (healthlose == 1 and twoje == "Y"):
                print("You lost 1 health point.")
                print("-------------------------------------------")
                healthyou = healthyou-1
            else:
                print("You successfully avoided losing a health point!")
                print("-------------------------------------------")
                time.sleep(1)
#If anwser is invalid
    else:
        print("Invalid anwser.")
#Reloading
    if shots<2:
        print("Reloading...")
        print("-------------------------------------------")
        time.sleep(3)
        shots = random.randint(4,10)
#Player loses
    if (healthyou<1):
        print("You lost.")
        break
#Enemy loses
    if (healthenemy<1):
        print("You win!")
        break
