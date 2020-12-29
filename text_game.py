import time
import random

print("Hello")
print("Welcome to the game")
time.sleep(1)
name = input("What is your name? \n")

print("Hello " + name)
time.sleep(1)

escape = False
while escape == False:
    try:
        fav_num = int(input("What is your favorite number? \n"))
        escape = True
    except:
        print("Please enter an integer")

escape = False
while escape == False:
    try:
        age = int(input("How old are you? \n"))
        if age > 100:
            print("You are too old to play this game. Lie and pretend you are younger!")
        elif age < 0:
            print("You can't have a negative age unless you are Merlin...")
        else:
            escape = True
    except:
        print("Please enter an integer")


if fav_num <age:
    print("\nyou will have bad luck...")
    time.sleep(1)
else:
    print("\nyou will have pretty good luck")

escape = False
while escape == False:
    weapon_choice = input("Select your weapon: s = sword, b = bow, h = hammer \n")
    if weapon_choice == 's':
        print("You have chosen the sword for your weapon")
        weapon = {
            "attack": 15,
            "defense": 15
            }
        escape = True
    elif weapon_choice == 'b':
        print("You have chosen the bow for your weapon")
        weapon = {
            "attack": 10,
            "defense": 20
            }
        escape = True
    elif weapon_choice == 'h':
        print("You have chosen the hammer for your weapon")
        weapon = {
            "attack": 30,
            "defense": 5
            }
        escape = True
    else:
        print("You must enter a valid weapon character: s, b, or h")

random.seed(fav_num)
hp = round(10 * float(age) * (0.5 + random.random()),0)

print("Your hp is " + str(hp))
time.sleep(2)
print("Uh-oh...")
time.sleep(1)
print("A goblin appeared!")

goblin = {
    "hp": 90,
    "attack": 7,
    "defense": 5
    }

while goblin["hp"] > 0:
    escape = False
    while escape == False:
        action = input("What will you do? a: attack, d: defend \n")
        if action == "a":
            hp_drop = int(weapon["attack"] - goblin["defense"] / 10 * random.random())
            print("You attacked the goblin!")
            print("Your attack did " + str(hp_drop) + " damage!")
            goblin["hp"] -= hp_drop
            time.sleep(1)
            if goblin["hp"] <0:
                goblin["hp"] = 0
            print("The goblin's hp dropped to " + str(goblin["hp"]))
            time.sleep(1)
            if goblin["hp"] > 0:
                print("The goblin attacked you!")
                hp_drop = int(goblin["attack"] - weapon["defense"] / 10 * random.random())
                print("The goblin's attack did " + str(hp_drop) + " damage to you!")
                hp -= hp_drop
                print("Your hp fell to " + str(hp))
            escape = True
        elif action == "d":
            print("The goblin attacked you!")
            hp_drop = int(goblin["attack"] - weapon["defense"] / 10 * random.random())
            print("The goblin's attack did " + str(hp_drop) + " damage to you!")
            hp -= hp_drop
            print("Your hp fell to " + str(hp))
            escape = True
        else:
            print("You must make a choice!")

print("You defeated the goblin!")
time.sleep(1)
print("You won the game! Good job. Bye!")








