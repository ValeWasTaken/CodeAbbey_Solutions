# Python 2.7

player_one = 'X'
player_two = 'O'
answer = []

def has_the_moves(player, moves):
    if len(moves) <= 2:
        return None

    # Winning combinations
    win1 = (0,3,6) #[1,4,7]
    win2 = (1,4,7) #[2,5,8]
    win3 = (2,5,8) #[3,6,9]
    win4 = (0,4,8) #[1,5,9]
    win5 = (6,7,8) #[7,8,9]
    win6 = (3,4,5) #[4,5,6]
    win7 = (0,1,2) #[1,2,3]
    win8 = (6,7,8) #[7,8,9]
    winning_grids = [win1, win2, win3, win4, win5, win6, win7, win8]

    tried = [set(posibility) <= set(moves) for posibility in winning_grids]
    return player if any(tried) else None

def is_winner(board):
    # Check for winner
    player_one_moves = [i for i, x in enumerate(board) if x == player_one]
    player_two_moves = [i for i, x in enumerate(board) if x == player_two]

    player_one_won = has_the_moves(player_one, player_one_moves)
    player_two_won = has_the_moves(player_two, player_two_moves)

    if player_one_won or player_two_won:
        return True
    else:
        return None

def tic_tac_toe(games):
    for game in range(games):
        board = [str(x) for x in range(1, 10)] # Create the 3x3 Tic-Tac-Toe board.
        moves = [int(x) for x in raw_input().split()] # Logs all player moves.

        for turn, move in enumerate(moves):
            # Take turns rewriting the default board to player 1's X
            # and then player 2's O.
            board[move - 1] = player_one if turn % 2 == 0 else player_two

            if is_winner(board):
                answer.append(str(turn+1))
                break; # Stops loop each time an answer is found.
            if turn == len(moves) - 1:
                answer.append('0') # Tie game

if __name__ == '__main__':
    tic_tac_toe(input())
    print(' '.join(answer))
