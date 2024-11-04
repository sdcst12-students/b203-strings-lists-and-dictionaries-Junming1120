#!python3
"""
##### Task 5
create a dictionary for an inventory of items in a game.  Ask the user for input, and if the item they choose to 'get item', add that item to their inventory.  If they choose to drop item' remove that item from that invenory.  If they choose 'show inventory' give them a list of the items that they have. You will need to use the string.split() method to separate the command from the item.

Possible extensions:
* nicer format for displaying inventory
* use shortened/abbreviated names for items (recognizing first few characters or spelling errors)

possible items:
food
water
rope
torch
sack
wood
iron
steel
ginger
garlic
fish
stone
wool

example:
>get food
>get water
>get water
>get iron
>get 3 wood
>inventory
You have:
 1 food
 2 water
 1 iron
 3 wood
 >
"""
inventory = {"food":0,"water":0,"rope":0,"torch":0,"sack":0,"wood":0,"iron":0,"steel":0,"ginger":0,"Garlic":0,"fish":0,"stone":0,"wood":0}


while True:
    x=input()
    xList=x.split(" ")
    if xList[0]=="get":
        if xList[1].isdigit():
            inventory[xList[2]]+=int(xList[1])
        else:
            inventory[xList[1]]+=1
    elif xList[0]=="remove":
        if xList[1].isdigit():
            inventory[xList[2]]-=int(xList[1])
        else:
            inventory[xList[1]]-=1
    elif xList[0]=="show":
        for i in range(len(inventory)):
            print(str(list(inventory.values())[i]))
            print(str(list(inventory.keys())[i]))

