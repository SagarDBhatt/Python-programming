import random

ls_options = ['rock', 'paper', 'scissor']


def getWinner(p1, p2):
    p1_winner_flag = False

    if p1 == 'rock':
        if p2 == 'scissor':
            p1_winner_flag = True
    elif p1 == 'paper':
        if p2 == 'rock':
            p1_winner_flag = True
    else:
        if p2 == 'paper':
            p1_winner_flag = True

    if p1_winner_flag:
        print("Computer is winner and selected " + p1)

    else:
        print("You are a winner and selected " + p2)


if __name__ == '__main__':
    # computer = input("Select Rock Or Paper Or Scissor for player 1 = ")
    # player2 = input("Select Rock Or Paper Or Scissor for player 2 = ")

    computer = ls_options[random.randint(0, 2)]
    player2 = ls_options[int(input("Please select Rock (0), Paper(1) or Scissor(2) = \n"))]

    try:
        if computer != player2:
            print("Computer selected = " + computer)
            print("You selected = " + player2)
            getWinner(computer, player2)

        elif computer == player2:
            print("Computer selected = " + computer)
            print("You selected = " + player2)
            print("Both computer and you selected the same!! No winner for this round!")

        else:
            raise Exception

    except Exception:
        print("Please Select the valid option")
