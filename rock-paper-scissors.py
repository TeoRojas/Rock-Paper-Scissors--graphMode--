import random

OPTIONS = ['Rock','Paper','Scissors']

ROCK = [
        "    _______        ",
        "---'   ____)__     ",
        "        (_____)    ",
        "        (_____)    ",
        "        (____)     ",
        "---.____(___)      "
        ]

PAPER = [
        "    ________       ",
        "---'    ____)____  ",
        "           ______) ",
        "            ______)",
        "           ______) ",
        "---.___________)   "
        ]

SCISSORS = [
        "    ________       ",
        "---'    ____)____  ",
        "           ______) ",
        "         _________)",
        "        (____)     ", 
        "---.____(___)      "                                   
        ]        

if __name__ == "__main__":
    print ("""
    This is a ROCK-PAPER-SCISSORS GAME, 
    ¿¿¿Could you beat the machine???
    """)

    player_choice = 0
    
    while player_choice != 1 and player_choice != 2 and player_choice != 3:
        player_choice = int(input("""
        INSERT your choice:
        #1 for Rock
        #2 for Paper
        #3 for Scissors
        """))

        if player_choice != 1 and player_choice != 2 and player_choice != 3:
            print('WRONG CHOICE! Try writing one of the three numbers: 1-2-3.')
        else:
            break            

        print('YOU SELECTED: '+ str(player_choice))

    player_choice = OPTIONS[player_choice-1]
    machine_choice = random.choice(OPTIONS)

    print("+" + "".center(51, '-') + "+")
    print("|" + "YOU CHOSE:".center(25) + "|" + "THE MACHINE CHOSE:".center(25) + "|")
    print("|" + "vs".center(51) + "|")
    print("|" + player_choice.center(25) + "|" + machine_choice.center(25) + "|")
    print("+" + "".center(51, '-') + "+")

    for l in range(len(ROCK)):
        print((ROCK[l] + "|" + SCISSORS[l][::-1].replace(')','(')).center(53))
              