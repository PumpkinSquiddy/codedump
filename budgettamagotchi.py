# THIS WAS CODED LIVE ON TWITCH BY @PUMPKINSQUIDDY, VTUBER WANNABE CODER
# follow me on twitter @PumpkinSquiddy, or instagram @PumpkinSquiddy, or youtube @PumpkinSquiddy... they are all the same
# anyway THIS CODE IS SEVERELY INCOMPLETE BECAUSE I REALIZED THAT YOU CAN JUST DOWNLOAD TAMAGOTCHI ON A MOBILE PHONE 
# REEEEEEEEEEEEEEEEEEEEEEEE
# anyway sorry for errors, i really cant be bothered anymore because i actually am not good at coding as you will find out

import time

#define 
pettime = 0 #the number of seconds my pet is live
pethealth = 100 #how much health pet have
pethappy = 100 #how happy the pet is
petfood = 100 #how much food the pet is
petpiss = 100 #how much the pet needs to piss
money = 1000

#shop prices define
shoplist = ["apple", "pear", "steak", "truffle", "wine", "cheese", "ramen", "water", "carrot"]
pricelist = [5, 6, 20, 100, 25, 10, 15, 1, 5]
itemquantity = [0, 0, 0, 0, 0, 0, 0, 0, 0]

#allows the user to choose their own tamagotchi name and owner name

pet = input("Please enter the name of your little pet: ")
pet = str(pet)

name = input("Who is " + pet + "'s owner? ")
name = str(name)

#function def for all the games and stuff
def feedPet():
    global pet
    global petfood
    y = 0
    for x in shoplist:
        print (y, x, itemquantity[y])
        y += 1
    consumefood = input("What do you want " + pet + " to eat? (Number only) ")
    try:
        consumefood = int(consumefood)
    except:
        quit
    if itemquantity[consumefood] > 0:
        itemquantity[consumefood] -= 1
        petfood += pricelist[consumefood]
        print("You fed", pet, "!")
        print(pet +  "'s hunger is at", petfood)
    else:
        print("You are too broke to afford good food.")

def playPet():
    print("playPet")

def healPet():
    global pethealth
    heal = input("Type 'heal' to heal your little monster. ")
    if heal == "heal":
        pethealth += 100
    print ("Pet Health: ", pethealth)

def toiletPet():
    print("toilet")

def checkPet():
    print("Health:", pethealth)
    print("Happiness:", pethappy)
    print("Hunger:", petfood)
    print("Toilet need:", petpiss)
    print("Richness:", money)

def shop():
    global money
    y = 0
    for x in shoplist:
        print(y, x, pricelist[y])
        y += 1
    order = input("What item would you like to buy? (say it by number) ")
    try:
        order = int(order)
    except:
        quit
    if money >= pricelist[order]:
        money = money - pricelist[order]
        itemquantity[order] = itemquantity[order] + 1
        print("You purchased", shoplist[order], "for", pricelist[order])
        print ("You have", itemquantity[order], shoplist[order])
        print ("Remaining money: ", money)
    else:
        print("You're too broke, earn money loser.")
        print("Money:", money)


#it starts as an egg, grows into a child, and grows into an adult + after a few real life minutes

while pethealth > 0 and pethappy > 0 and petfood > 0 and petpiss > 0:
    print("""
    What do you want your pet to do?
    [F]eed the pet, [P]lay with pet, [H]eal the pet, [T]oilet the pet, [C]heck pet's stats, Visit the [S]hop, [Q]uit the game 
    """)
    choice = input("[F]eed, [P]lay, [H]eal, [T]oilet, [C]heck, [S]hop, [Q]uit ")
    try:
        choice = str(choice)
    except: 
        continue
    if choice == "F" or choice == "f":
        feedPet()
    elif choice == "P" or choice == "p":
        playPet()
    elif choice == "H" or choice == "h":
        healPet()
    elif choice == "T" or choice == "t":
        toiletPet()
    elif choice == "C" or choice == "c":
        checkPet()
    elif choice == "S" or choice == "s":
        shop() #DONE BABYYYYY
    elif choice == "Q" or choice == "q":
        break
    else:
        continue
    pethealth -= 10
    petfood -= 20
    pethappy -= 20
    petpiss -= 20


print("Thank you for playing! Please don't ever code your own tamagotchi because it hurts. Just buy one.")
#feed, bond with, and shower with and play with the tamagotchi
#shop feature


