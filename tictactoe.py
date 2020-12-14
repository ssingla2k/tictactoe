"""
Tic Tac Toe Player
"""

import math

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
    countX=0
    countO=0
    for row in board:
        countX = countX + row.count(X)
        countO = countO + row.count(O)
    # print("x %d"%countX)
    # print("o %d"%countO)
    if countX > countO:
        return O
    else:
        return X
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionset=[]
    for i in range(0,2):
        for j in range(0,2):
            if board[i][j] is EMPTY:
                actionset.append((i,j))
    return actionset


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if terminal(board):
        if utility(board) == 1:
            return X
        elif utility(board) == -1:
            return O
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if utility(board) in [1,-1]:
        return True
    for row in board:
        for e in row:
            if e is not EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    def isWinner(board,player):
        #check row win
        for i in range(0,3):
            count=0
            for j in range(0,3):
                if board[i][j] == player:
                    count = count+1
                else:
                    break
            if count == 3:
                return True
        #check column win
        for j in range(0,3):
            count=0
            for i in range(0,3):
                if board[i][j] == player:
                    count=count+1
                else:
                    break
            if count==3:
                return True
        #check diagnal win
        count=0
        for i in range(0,3):
            if board[i][i] == player:
                count=count+1
            else:
                break
        if count==3:
            return True
        count=0
        for i in range(0,3):
            if board[i][2-i] == player:
                count=count+1
            else:
                break
        if count==3:
            return True
        return False
    if isWinner(board,X):
        return 1
    elif isWinner(board,O):
        return -1
    else:
        return 0
    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
