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
        print("Player 1 is winner and selected " + p1)

    else:
        print("Player 2 is winner and selected " + p2)


if __name__ == '__main__':
    # player1 = input("Select Rock Or Paper Or Scissor for player 1 = ")
    # player2 = input("Select Rock Or Paper Or Scissor for player 2 = ")

    player1 = ls_options[random.randint(0, 2)]
    player2 = ls_options[random.randint(0, 2)]

    try:
        if player1 != player2:
            print("Player 1 selected = " + player1)
            print("Player 2 selected = " + player2)
            getWinner(player1, player2)

        elif player1 == player2:
            print("Player 1 selected = " + player1)
            print("Player 2 selected = " + player2)
            print("Both players selected the same!! No winner for this round!")

        else:
            raise Exception

    except Exception:
        print("Please Select the valid option")
