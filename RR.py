import random
import time
shots = random.randint(4,8)
twoje = 0
healthyou = 3
healthenemy = 3
healthlose = 0
enemypick = 0
round = 0
playername = 0
enemyname = 0

print("-------------------------------------------")
print("-WELCOME TO R.R.-")
print("-------------------------------------------")
playername = input("What is your name?")
enemyname = input("What is your enemies name?")
time.sleep(1)
while True:
        if round == 0:
                round = 0
                print("-There are", shots, "chambers loaded.-")
                print("-It's your turn.-")
                print(playername,"'s health:", healthyou)
                print(enemyname,"'s health:", healthenemy)
                print("-------------------------------------------")
                time.sleep(1)
                twoje = input("Do you wish to fire the gun at (Y)ourself or your (O)pponent? Y/O")
                print("-------------------------------------------")
#If you say yes
        if (twoje == 'Y'):
            shots = shots-1
            healthlose = random.randint(1,shots)
            if (healthlose == 1 and twoje == "Y"):
                time.sleep(1)
                print("BOOM!")
                time.sleep(3)
                print("You lost 1 health point.")
                print("-------------------------------------------")
                healthyou = healthyou-1
                round = 1
            else:
                time.sleep(1)
                print("You successfully avoided losing a health point!")
                print("-------------------------------------------")
                time.sleep(1)
                round = 1
#If you say no  
        if (twoje == 'O'):
            enemypick = random.randint(1,4)
            if (enemypick == 1 or enemypick == 2 or enemypick == 3 ):
                shots = shots-1
                healthlose = random.randint(1,shots)
                if (healthlose == 1 and twoje == "N"):
                    time.sleep(1)
                    print("BOOM!")
                    time.sleep(3)
                    print(enemyname, " lost 1 health point!")
                    print("-------------------------------------------")
                    healthenemy = healthenemy-1
                    round = 1
                else:
                    print(enemyname, "successfully avoided losing a health point!")
                    print("-------------------------------------------")
                    time.sleep(1)
                    round = 1
            if (enemypick == 4):
                print(enemyname, "passes you the weapon...")
                shots = shots-1
                healthlose = random.randint(1,shots)
                if (healthlose == 1 and twoje == "Y"):
                    time.sleep(1)
                    print("BOOM!")
                    time.sleep(3)
                    print("You lost 1 health point.")
                    print("-------------------------------------------")
                    round = 1
                    healthyou = healthyou-1
                else:
                    print("You successfully avoided losing a health point!")
                    print("-------------------------------------------")
                    time.sleep(1)
                    round = 1
        if shots<2:
            print("Reloading...")
            print("-------------------------------------------")
            time.sleep(3)
            shots = random.randint(4,10)
#bots turn
        if round == 1:
            print("-There are", shots, "chambers loaded.-")
            print("-It's your enemies turn.-")
            print(playername,"'s health:", healthyou)
            print(enemyname,"'s health:", healthenemy)
            print("-------------------------------------------")
            time.sleep(1)
            enemypick = random.randint(1,2)
            if (enemypick == 1):
                shots = shots-1
                healthlose = random.randint(1,shots)
                if (healthlose == 1 and twoje == "N"):
                    time.sleep(1)
                    print("BOOM!")
                    time.sleep(3)
                    print(enemyname, " lost 1 health point!")
                    print("-------------------------------------------")
                    healthenemy = healthenemy-1
                    round = 0
                else:
                    print(enemyname, " successfully avoided losing a health point.")
                    print("-------------------------------------------")
                    time.sleep(1)
                    round = 0
            if (enemypick == 2):
                print(enemyname, "passes you the weapon...")
                shots = shots-1
                healthlose = random.randint(1,shots)
                if (healthlose == 1 and twoje == "Y"):
                    time.sleep(1)
                    print("BOOM!")
                    time.sleep(3)
                    print("You lost 1 health point.")
                    print("-------------------------------------------")
                    healthyou = healthyou-1
                    round = 0
                else:
                    print("You successfully avoided losing a health point!")
                    print("-------------------------------------------")
                    time.sleep(1)
                    round = 0
            if shots<2:
                print("Reloading...")
                print("-------------------------------------------")
                time.sleep(3)
                shots = random.randint(4,10)
        else:
            print("Don't think you're so smart boy!")
#Reloading
        if shots<2:
            print("Reloading...")
            print("-------------------------------------------")
            time.sleep(3)
            shots = random.randint(4,10)
#Player loses
        if (healthyou<1):
            print("You lost...")
            for i in range(999):
                print("YoU lOsT1")
                print("yOu LoSt!")
            break
#Enemy loses
        if (healthenemy<1):
            print("You win!")
            break
#Tie
        if (healthenemy and healthyou<1):
            print("It's a tie.")
            break
