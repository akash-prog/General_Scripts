import random
import time

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("rolling the dice ...")
    time.sleep(1)

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    print("the dice values are:")
    print("dice1 :",dice1, "\ndice2 :",dice2)

    if dice1==dice2:
        print("you got a double !")
    else:
        print("keep trying")

        roll_again = input("\nroll the dice again ? (y/n)")





