print("""Welcome to Treasure Island.
Your mission is to find the treasure.""")

step1 = input("left or right? L or R ").upper()
step2 = input("swim or wait? S or W ").upper()
step3 = input("Which door? R,B,Y ").upper()

if(step1 == 'L'):
    if(step2 == 'W'):
        if(step3 == "Y"):
            print("You win!")
        elif(step3 == "R"):
            print("""Burned by fire.
            Game Over.""")
        elif(step3 == "B"):
            print("""Eaten by beasts.
            Game Over.""")
        else:
            print("Game Over")
    else:
        print("""Attacked by trout.
        Game Over.""")
else:
    print("""Fall into a hole.
    Game Over.""")