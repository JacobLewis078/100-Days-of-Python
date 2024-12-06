#Adventure cmd  line game
#items
import random
sword = False
princess = False
treasure = False
shield = False
fuzzy_socks = False
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Hey Bros *or lady bros*, we are about to embark on a totaly epic adventure in search for treasure.")
print("Make the right choices and you may just end up with some booty..")
print("and some treasure")

#FIRST CHOICE
beginning_choice = input("\nYour adventure begins here, grab your sneakers and cap and lets go! First decision: Left or Right? \n")

if beginning_choice.upper() == "LEFT":

    #SECONDCHOICE
    print("\nWoah! check out this totally wicked castle! There is totally some treasure in here! Let's get to it!")

    print("\nYou've walked into the castle and you notice there is a hallway on your left, another hallway on your right, and a staircase infront of you.")
    second_choice = input("Which way do you want to go bro-tato chip? type L R or M : \n")
    #LEFT HALLWAY - SHIELD
    if second_choice.upper() == "L":
        print("\nThere is something on the back wall. It seems shiny.")
        #SEE IF EXPLORER WANTS TO EXPLORE THE SHINY
        see_shiny_thing = input("What to go see what it is? Yes or No? \n")
        if see_shiny_thing.lower() == "yes":
            print("\nNot afraid of anything are we brave wanderer? EPIC! \n You found a shield! That may come in use later.")
            shield = True
            print("\nLet's continue through the doorway at the back of room. Onward explorers!")
        else:
            print("\nAlright, I see. Playing safe brochachu. Respect that. Go ahead and wanter down that other doorway and lets see what else we find.")
    #RIGHT HALLWAY - NOTHING
    elif second_choice.upper() == "R":
        print("\nThere doesn't appear to be anything in here.. bummer.. Looks like you keep exploring through a back door.")
    #STAIRCASE
    else:
        print("\nUp the stairs.. What a bold choice epic explorer dude")
        print("Can't wait to see what is up here!")

    #BOTTOM FLOOR BACK ROOM
    if second_choice.upper() == "R" or second_choice.upper() == "L":
        print("\nWicked back creepy room.. Looks like there are 2 chests. Something tells me you'll only get to peek inside one")
        chest_choice = input("Which check you choosing, wanderer? 1 or 2? \n")
        if chest_choice == "1":
            print("\nA sword! Heck yeah! with a sword and shield, what could stop you! ")
            sword = True
            print("\nSeems to be some more stairs in the back. Let's go up, slayer!")
        else:
            print("\nIt's something small? Round? Fuzzy? O Snap! Fuzzy Socks! No clue what you will use these for, but who doesn't love some fuzz for their footsies.")
            fuzzy_socks = True
            print("\nSeems to be some more stairs in the back. Let's go up, cuddles!")

    #UP THE STAIRS - check for socks
    if fuzzy_socks == True:
        print("\nBro-tien shake.. I know you see this huge slippery floor...")
        slipping_on_socks = input("You slipping on those socks to scoot around? Yes or No? \n")
        if slipping_on_socks.upper() == "YES":
                print("\nMaybe that wasn't a great idea... You slipped slide so wickedly hard that you fell down the stairs and died.. what a bummer.")
                print("Game Over")
        else:
            print("Propbably the smart idea. We are busy hunting for treasure")
    
    print("\nYou see those three doors? I think we need to choose one.")
    picked_door = input("Which one we going in? 1, 2, or 3? ")

    #DOOR PICKAGE
    if picked_door == "1":
        print("*Intense love music plays*\n Woah.. You found a princess! I think you are in love. Let's grab her and keep searching fella!")
        princess = True
    elif picked_door == "2":
        print("Looks like some more stairs, lets keep going!")
    else:
        print("Looks like some more stairs. Let's keep going!")
    
    #Final Chapter
    print("This is it.. The final chamber.. Bro-rrito, this should be where the treasure is..")
    print("\n\n\nThere it is! I see it in the back of the room! You just have to get back that big scary dragon and the treasure is all yours!")
    input("\nYou ready for this final chapter?")
    if sword == True and shield == True:
        print("\nThank goodness you found that sword and shield! With no training but those sick weapons, you got this!")
        if princess == True:
            print("\nYou made it through this epic adventure! You slayed a dragon, got a sick sword and shield, got the treasure and escaped with the princess! I knew you could do it Bro-ski!")
            print("You WIN!")
        else:
            print("\nYou made it through this adventure and found the treasure! Way to go!")
            print("You WIN! But my code is telling me that there were unfound treasures to be had..")
    if sword == True or shield == True:
        print("\nThis doesn't look promising.. You atleast have something to fight with. Let's roll the dice and see if you can get that treasure!")
        number = random.randint(1,100)
        if number % 2 == 0 and princess == True:
            print("\nYou made it through this epic adventure! You slayed a dragon, got a sick sword and shield, got the treasure and escaped with the princess! I knew you could do it Bro-ski!")
            print("You WIN!")
        elif number % 2 == 0 and princess == False:
            print("\nYou made it through this adventure and found the treasure! Way to go!")
            print("You WIN! But my code is telling me that there were unfound treasures to be had..")
        else:
            print("\nNOOOO! you died.. sometimes that happens on these epic adventures..")
            print("Game Over.")
    if sword == False and shield == False and princess == True:
        print("\nThis doesn't look good. You have nothing to fight with. You have 2 choices. Either sacrifice yourself so the princess can escape")
        print("Or..... you can throw the princess at the dragon and grab some loot and bail...")
        sacrifice_choice = input("Who is taking the fall? 1: yourself or 2: the princess")
        if sacrifice_choice == "1":
            print("\n*Salute* Selfless bro. Selfless. You saved the lass but sadly met your fate.")
            print("Game Over")
        else:
            print("\nYou throw the princess at the dragon as a distraction.")
            print("You make out with some loot. But are you really a winner?")
            print("Game Over.")
    else:
        if fuzzy_socks == True:
            print("\nWell bro, maybe he would trade the treasure for those fuzzy socks you got?")
            print("\n\n\nWait.. what? He forreal is trading the treasure for the fuzzies? What a steal!")
            print("You WIN!")
        else:
            print("\nWell this is bad. Good adventuring with you Bruder! But this looks like the end.")
            print("Game Over.")

else:
    print("\nDang bro.. that adventure was totally lame. Going right led you straight to rundown Taco Bell that gave you food poisoning. Go home and heal up. Maybe try again once it.. passess...")
    print("Game Over")
