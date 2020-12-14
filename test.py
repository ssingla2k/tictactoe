import tictactoe as t

board = t.initial_state()

board[0][2] = t.X
board[1][1] = t.X
board[2][0] = t.X

print(t.utility(board))
print(t.terminal(board))
print(board)
for row in board:
	print(row.count(t.O))
print (t.player(board))
