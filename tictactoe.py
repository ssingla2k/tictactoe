"""
Tic Tac Toe Player
"""

import math
import logging

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
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] is EMPTY:
                actionset.append((i,j))
    return actionset


def result(board, action,p):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #print(action)
    board[action[0]][action[1]] = p
    return board


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
            #logging.debug("test %s",e)
            if e is None:
                #logging.debug(e)
                return False
    #print(board)
    #logging.debug("did not find a empty cell in board")
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #logging.debug("in utility")
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
        #logging.debug("returning from utility %d",1)
        return 1
    elif isWinner(board,O):
        #logging.debug("returning from utility %d",-1)
        return -1
    else:
        #logging.debug("returning from utility %d",0)
        return 0
    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    logging.debug("calling minimax with board %s",board)
    def minmax_int(board,isMaximize,depth):
        if terminal(board):
            return (utility(board),None)
        board_temp = board.copy()
        if isMaximize:
            bestval = -100
            a=None
            for action in actions(board_temp):
                board_temp = result(board_temp,action,player(board_temp))
                value = minmax_int(board_temp,False,depth+1)[0]
                if bestval < value:
                    bestval=value
                    a = action
            return (bestval,a)
        else:
            bestval=100
            a=None
            for action in actions(board_temp):
                board_temp = result(board_temp,action,player(board_temp))
                value = minmax_int(board_temp,True,depth+1)[0]
                if bestval > value:
                    bestval=value
                    a = action
            return (bestval,a)

    if player(board) == X:
        r = minmax_int(board, True,0)
        logging.debug("minmax_int result for X %s",r)
        return r[1]
    else:
        r = minmax_int(board, False,0)
        logging.debug("minmax_int result for O %s",r)
        return r[1]
