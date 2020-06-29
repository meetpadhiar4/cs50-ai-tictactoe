"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_x = 0
    num_o = 0
    for i in range(len(board[0])):
        for j in range(len(board[i])):
            if board[i][j] == X:
                num_x += 1
            elif board[i][j] == O:
                num_o += 1
    if num_x > num_o:
        return O
    elif not terminal(board) and num_x == num_o:
        return X
    else:
        return None


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(len(board[0])):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError('Invalid action')
    p = player(board)
    board_copy = copy.deepcopy(board)
    (i, j) = action
    board_copy[i][j] = p
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] == board[0][2] != None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[1][0] == board[1][1] == board[1][2] != None:
        if board[1][0] == X:
            return X
        else:
            return O
    elif board[2][0] == board[2][1] == board[2][2] != None:
        if board[2][0] == X:
            return X
        else:
            return O
    elif board[0][0] == board[1][0] == board[2][0] != None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[0][1] == board[1][1] == board[2][1] != None:
        if board[0][1] == X:
            return X
        else:
            return O
    elif board[0][2] == board[1][2] == board[2][2] != None:
        if board[0][2] == X:
            return X
        else:
            return O
    elif board[0][0] == board[1][1] == board[2][2] != None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[0][2] == board[1][1] == board[2][0] != None:
        if board[0][2] == X:
            return X
        else:
            return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    for i in range(len(board[0])):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    p = player(board)
    alpha = -math.inf
    beta = math.inf
    if board == [[EMPTY] * 3] * 3:
        return (0, 0)
    if p == X:
        v = -math.inf
        best_move = None
        for action in actions(board):
            min_val = minValue(result(board, action), alpha, beta)
            alpha = max(v, min_val)
            if min_val > v:
                v = min_val
                best_move = action
    elif p == O:
        v = math.inf
        best_move = None
        for action in actions(board):
            max_val = maxValue(result(board, action), alpha, beta)
            beta = min(v, max_val)
            if max_val < v:
                v = max_val
                best_move = action
    return best_move


def maxValue(board, alpha, beta):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, minValue(result(board, action), alpha, beta))
        alpha = max(v, alpha)
        if alpha >= beta:
            break
    return v


def minValue(board, alpha, beta):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, maxValue(result(board, action), alpha, beta))
        beta = min(v, beta)
        if alpha >= beta:
            break
    return v
