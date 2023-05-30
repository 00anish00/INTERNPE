import random

def prboard(xState, zState):
    one   = 'X' if xState[1] else ('O' if zState[1] else '*')
    two   = 'X' if xState[2] else ('O' if zState[2] else '*')
    three = 'X' if xState[3] else ('O' if zState[3] else '*')
    four  = 'X' if xState[4] else ('O' if zState[4] else '*')
    five  = 'X' if xState[5] else ('O' if zState[5] else '*')
    six   = 'X' if xState[6] else ('O' if zState[6] else '*')
    seven = 'X' if xState[7] else ('O' if zState[7] else '*')
    eight = 'X' if xState[8] else ('O' if zState[8] else '*')
    nine  = 'X' if xState[9] else ('O' if zState[9] else '*')
    print("-------------")
    print(f"| {seven} | {eight} | {nine} |")
    print("| - | - | - |")
    print(f"| {four} | {five} | {six} |")
    print("| - | - | - |")
    print(f"| {one} | {two} | {three} |")
    print("-------------")

def winnerchk(xState, zState):
    # X's winning conditions
    if (
        (xState[1] == xState[2] == xState[3] == 1) or
        (xState[3] == xState[6] == xState[9] == 1) or
        (xState[9] == xState[8] == xState[7] == 1) or
        (xState[7] == xState[4] == xState[1] == 1) or
        (xState[1] == xState[5] == xState[9] == 1) or
        (xState[3] == xState[5] == xState[7] == 1) or
        (xState[2] == xState[5] == xState[8] == 1) or
        (xState[4] == xState[5] == xState[6] == 1)
    ):
        return 'WINX'

    # O's winning conditions
    elif (
        (zState[1] == zState[2] == zState[3] == 1) or
        (zState[3] == zState[6] == zState[9] == 1) or
        (zState[9] == zState[8] == zState[7] == 1) or
        (zState[7] == zState[4] == zState[1] == 1) or
        (zState[1] == zState[5] == zState[9] == 1) or
        (zState[3] == zState[5] == zState[7] == 1) or
        (zState[2] == zState[5] == zState[8] == 1) or
        (zState[4] == zState[5] == zState[6] == 1)
    ):
        return 'WINZ'

    return None



def is_board_full(xState, zState):
    return all(xState[i] or zState[i] for i in range(9))


def play_vs_human():
    xState = ['e','','','','','','','','','']
    zState = ['e','','','','','','','','','']
    turn = 1  # 1 for X and 0 for O
    print("Welcome to Tic Tac Toe (Two-Player Mode)!")
    while True:
        prboard(xState, zState)
        if turn == 1:
            print("X's turn")
        else:
            print("O's turn")
        value = int(input("Please enter a position (0-8): "))
        if value < 1 or value > 9:
            print("Invalid position! Please try again.")
            continue
        if xState[value] or zState[value]:
            print("Position already taken! Please try again.")
            continue
        if turn == 1:
            xState[value] = 1
            winner = winnerchk(xState, zState)
            if winner == 'WINX':
                prboard(xState, zState)
                print("X wins!")
                break
            turn = 0
        else:
            zState[value] = 1
            winner = winnerchk(xState, zState)
            if winner == 'WINZ':
                prboard(xState, zState)
                print("O wins!")
                break
            turn = 1
        if is_board_full(xState, zState):
            prboard(xState, zState)
            print("It's a draw!")
            break


def play_vs_computer():
    xState = ['e','','','','','','','','','']
    zState = ['e','','','','','','','','','']
    turn = 1  # 1 for X and 0 for O
    print("Welcome to Tic Tac Toe (Versus Computer Mode)!")
    while True:
        prboard(xState, zState)
        if turn == 1:
            print("Your turn (X)")
            value = int(input("Please enter a position (0-8): "))
            if value < 1 or value > 9:
                print("Invalid position! Please try again.")
                continue
            if xState[value] or zState[value]:
                print("Position already taken! Please try again.")
                continue
            xState[value] = 1
            winner = winnerchk(xState, zState)
            if winner == 'WINX':
                prboard(xState, zState)
                print("You win!")
                break
            turn = 0
        else:
            print("Computer's turn (O)")
            # Generate random move for the computer
            available_moves = [i for i in range(9) if not xState[i] and not zState[i]]
            value = random.choice(available_moves)
            zState[value] = 1
            winner = winnerchk(xState, zState)
            if winner == 'WINZ':
                prboard(xState, zState)
                print("Computer wins!")
                break
            turn = 1
        if is_board_full(xState, zState):
            prboard(xState, zState)
            print("It's a draw!")
            break


if __name__ == "__main__":
    print("Welcome to Tic Tac Toe!")
    while True:
        mode = int(input("Select a mode:\n1. Two-Player\n2. Versus Computer\n"))
        if mode == 1:
            play_vs_human()
        elif mode == 2:
            play_vs_computer()
        else:
            print("Invalid mode! Please try again.")
