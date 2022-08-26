import random
import os
import platform 

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

def print_two_hands(left_hand, right_hand):
    # In left_hand and right_hand any of the 3 constans
    # must be inserted: ROCK, PAPER or SCISSORS
    
    for l in range(len(ROCK)):
        print((left_hand[l] + "|" + right_hand[l][::-1].replace(')','(')).center(53))

def print_game_menu(player_choice, machine_choice):   
    print("+" + "".center(51, '-') + "+")
    print("|" + "YOU CHOSE:".center(25) + "|" + "THE MACHINE CHOSE:".center(25) + "|")
    print("|" + "vs".center(51) + "|")
    print("|" + OPTIONS[player_choice].center(25) + "|" + OPTIONS[machine_choice].center(25) + "|")
    print("+" + "".center(51, '-') + "+")

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')  

def player_choice_menu():
    print (("This is a ROCK-PAPER-SCISSORS GAME,\n ¿¿¿Could you beat the machine???").center(53))

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

    return (player_choice-1)

def print_blank_line():
    print("+" + "".center(51, '-') + "+")         

def print_who_wins(player, machine, OPTIONS):
    print_blank_line()
    if player == machine:
        print("|" + "It's a TIE!!!!!".center(51) + "|")
    elif player - machine == -1:
        print("|" + "YOU LOSE!!!!".center(51) + "|")
    elif player - machine == 1:
        print("|" + "YOU WIN!!!".center(51) + "|")
    else:
        print("|" + "YOU LOSE!!!".center(51) + "|")
    print_blank_line()

if __name__ == "__main__":

    options = [ROCK, PAPER, SCISSORS]
    player_choice = player_choice_menu()
    machine_choice = random.choice(range(3))

    clear_screen()

    print_game_menu(player_choice, machine_choice)

    print_two_hands(options[player_choice], options[machine_choice])

    print_who_wins(player_choice, machine_choice, OPTIONS)
              