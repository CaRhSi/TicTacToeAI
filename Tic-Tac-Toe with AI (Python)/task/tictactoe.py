import random
import sys
import math

sys.setrecursionlimit(10000)


def print_board():
    print('---------')
    print(f'| {board[0][2]} {board[1][2]} {board[2][2]} |')
    print(f'| {board[3][2]} {board[4][2]} {board[5][2]} |')
    print(f'| {board[6][2]} {board[7][2]} {board[8][2]} |')
    print('---------')


def player_turn(turn):
    allowed = [1, 2, 3]
    check = True
    while check:
        try:
            print('Enter the coordinates: ')
            x, y = input().split()
            x = int(x)
            y = int(y)
        except:
            print('You should enter numbers!')
            continue
        if x not in allowed or y not in allowed:
            print('Coordinates should be from 1 to 3!')
            continue
        for i in range(0, 9):
            if board[i][0] == x and board[i][1] == y and ('X' in board[i][2] or 'O' in board[i][2]):
                print('This cell is occupied! Choose another one!')
                break
            elif board[i][0] == x and board[i][1] == y and ' ' in board[i][2]:
                board[i][2] = turn
                check = False
    return


def AI_move(turn):
    move = False
    while not move:
        # Pick random coordinates
        x = random.randint(1, 3)
        y = random.randint(1, 3)

        # Place the move into those co-ordinates
        for i in range(0, 9):
            if board[i][0] == x and board[i][1] == y and ('X' in board[i][2] or 'O' in board[i][2]):
                break
            elif board[i][0] == x and board[i][1] == y and ' ' in board[i][2]:

                board[i][2] = turn
                move = True
    return


def turn_switch(turn):
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    return turn


def best_move(turn):
    bestScore = -math.inf if turn == 'X' else math.inf
    move = None
    for i in range(9):
        if board[i][2] == ' ':
            board[i][2] = turn
            score = minimax('O' if turn == 'X' else 'X', board, 0)
            board[i][2] = ' '
            if (turn == 'X' and score > bestScore) or (turn == 'O' and score < bestScore):
                bestScore = score
                move = i
    return move


ends = {1: 1, 2: -1, 3: 0}


def minimax(turny, board, depth):
    result = win_check(turny)
    if result is not None:
        return ends[result]

    if turny == 'X':
        bestScore = -math.inf
        for i in range(9):
            if board[i][2] == ' ':
                board[i][2] = 'X'
                score = minimax('O', board, depth + 1)
                board[i][2] = ' '
                bestScore = max(score, bestScore)
        return bestScore

    elif turny == 'O':
        bestScore = math.inf
        for i in range(9):
            if board[i][2] == ' ':
                board[i][2] = 'O'
                score = minimax('X', board, depth + 1)
                board[i][2] = ' '
                bestScore = min(score, bestScore)
        return bestScore




def med_AI_move(turn):
    # Update the win progression
    update_wins()
    # Check if a row or diagonal has 2 of on symbol and a blank space
    for i in range(0, 8):
        almost_win = wins[i]
        X_test = 0
        O_test = 0
        blank_test = 0
        can_win = False
        can_block = False
        # Check if the almost win variable contains 2 symbols and a blank
        for x in range(len(almost_win)):
            if almost_win[x] == 'X':
                X_test += 1
            elif almost_win[x] == 'O':
                O_test += 1
            elif almost_win[x] == ' ':
                blank_test += 1
            if (X_test == 2 and blank_test == 1 and turn == 'X') or (O_test == 2 and blank_test == 1 and turn == 'O'):
                can_win = True
                break
            elif (X_test == 2 and blank_test == 1 and turn == 'O') or (O_test == 2 and blank_test == 1 and turn == 'X'):
                can_block = True
                break

        # If a win or a block can be performed check on which win condition it can be done
        if can_win or can_block:
            # Based on the index of the win condition play the current move into the blank square in the Row/Col/Diag
            if i == 0:
                for i in range(0, 3):
                    if board[i][2] == ' ':
                        board[i][2] = turn
            elif i == 1:
                for i in range(3, 6):
                    if board[i][2] == ' ':
                        board[i][2] = turn
            elif i == 2:
                for i in range(6, 9):
                    if board[i][2] == ' ':
                        board[i][2] = turn
            elif i == 3:
                for i in [0, 3, 6]:
                    if board[i][2] == ' ':
                        board[i][2] = turn
            elif i == 4:
                for i in [1, 4, 7]:
                    if board[i][2] == ' ':
                        board[i][2] = turn
            elif i == 5:
                for i in [2, 5, 8]:
                    if board[i][2] == ' ':
                        board[i][2] = turn
            elif i == 6:
                for i in [0, 4, 8]:
                    if board[i][2] == ' ':
                        board[i][2] = turn
            elif i == 7:
                for i in [2, 4, 6]:
                    if board[i][2] == ' ':
                        board[i][2] = turn
            break
        # Do a standard random move if it cannot win
        if i == 7 and (not can_block and not can_win):
            AI_move(turn)
            break


def update_wins():
    global wins
    wins = [
        # Horizontal wins
        board[0][2] + board[1][2] + board[2][2],
        board[3][2] + board[4][2] + board[5][2],
        board[6][2] + board[7][2] + board[8][2],
        # Vertical wins
        board[0][2] + board[3][2] + board[6][2],
        board[1][2] + board[4][2] + board[7][2],
        board[2][2] + board[5][2] + board[8][2],
        # Diagonal wins
        board[0][2] + board[4][2] + board[8][2],
        board[2][2] + board[4][2] + board[6][2]
    ]


def win_check(turn):
    draw_check = 0
    update_wins()

    if 'XXX' in wins and turn == 'X':
        return 1
    elif 'OOO' in wins and turn == 'O':
        return 2
    for i in range(0, 9):
        if board[i][2] == ' ':
            draw_check += 1
        elif i == 8 and draw_check == 0:
            return 3


def initialize_board():
    global board
    board = [
        [1, 1, ' '], [1, 2, ' '], [1, 3, ' '],
        [2, 1, ' '], [2, 2, ' '], [2, 3, ' '],
        [3, 1, ' '], [3, 2, ' '], [3, 3, ' ']
    ]


def start_sequence():
    while True:
        input_cmd = input("Input command: ")
        if input_cmd == "exit":
            break
        elif len(input_cmd.split()) != 3 or input_cmd.split()[0] != "start":
            print("Bad parameters!")
        elif input_cmd.split()[1] not in ["user", "easy", "medium", "hard"] \
                or input_cmd.split()[2] not in ["user", "easy", "medium", "hard"]:
            print("Bad parameters!")
        else:
            player_1, player_2 = input_cmd.split()[1:]
            return player_1, player_2

def main():
    initialize_board()

    while True:
        # Initialise standard start of game conditions at the start of each round
        initialize_board()
        turn = 'X'
        turns = 0
        turn_X, turn_O = start_sequence()
        win_check(turn)
        while True:
            print_board()
            # Check which turn it is and do either set of conditions to make that move
            if turn == 'X':
                if turn_X == 'user':
                    player_turn(turn)
                elif turn_X == 'easy':
                    print('Making move level "easy"')
                    AI_move(turn)
                elif turn_X == 'medium':
                    print('Making move level "medium"')
                    med_AI_move(turn)
                elif turn_X == 'hard':
                    print('Making move level "hard"')
                    index = best_move(turn)
                    print(index)
                    board[index][2] = turn
            elif turn == 'O':
                if turn_O == 'user':
                    player_turn(turn)
                elif turn_O == 'easy':
                    print('Making move level "easy"')
                    AI_move(turn)
                elif turn_O == 'medium':
                    print('Making move level "medium"')
                    med_AI_move(turn)
                elif turn_O == 'hard':
                    print('Making move level "hard"')
                    index = best_move(turn)
                    print(index)
                    board[index][2] = 'O'
            turns += 1

            # Check for a winning condition and start again
            end = win_check(turn)
            if end == 1:
                print_board()
                print('X wins')
                break
            elif end == 2:
                print_board()
                print('O wins')
                break
            elif end == 3:
                print_board()
                print('Draw')
                break

            # At the end of each turn switch between X and O
            turn = turn_switch(turn)


if __name__ == "__main__":
    main()
