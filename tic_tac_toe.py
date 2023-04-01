import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    clear_screen()
    print('     |     |')
    print('  {}  |  {}  |  {}'.format(board[0], board[1], board[2]))
    print('_____|_____|_____')
    print('     |     |')
    print('  {}  |  {}  |  {}'.format(board[3], board[4], board[5]))
    print('_____|_____|_____')
    print('     |     |')
    print('  {}  |  {}  |  {}'.format(board[6], board[7], board[8]))
    print('     |     |')

def get_move(board, player):
    while True:
        move = input('Player {}, please enter your move (1-9): '.format(player))
        if move.isdigit() and int(move) in range(1, 10):
            move = int(move) - 1
            if board[move] == ' ':
                return move
        print('Invalid move, please try again.')

def check_win(board):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return board[combo[0]]
    if ' ' not in board:
        return 'tie'

def tic_tac_toe():
    board = [' '] * 9
    players = ['X', 'O']
    current_player = 0

    while True:
        print_board(board)
        move = get_move(board, players[current_player])
        board[move] = players[current_player]
        winner = check_win(board)
        if winner:
            print_board(board)
            if winner == 'tie':
                print('The game is a tie.')
            else:
                print('Player {} wins!'.format(winner))
            break
        current_player = (current_player + 1) % 2

if __name__ == '__main__':
    tic_tac_toe()
