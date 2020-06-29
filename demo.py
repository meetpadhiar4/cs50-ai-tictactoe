import math

num_x = 0
num_o = 0
EMPTY = None
actions = set()

board = [["X", "O", "X"],
          ["X","O", "X"],
          ["O", "X", "O"]]

for i in range(len(board[0])):
    for j in range(len(board[i])):
        if board[i][j] == "X":
            num_x += 1
        else:
            num_o += 1


for i in range(len(board[0])):
    for j in range(len(board[i])):
        if board[i][j] == EMPTY:
            actions.add((i, j))

print([[EMPTY] * 3] * 3)

# if board[0][0] == board[0][1] == board[0][2] != None:
#     if board[0][0] == "X":
#         print("X")
#     else:
#         print("O")
# elif board[1][0] == board[1][1] == board[1][2] != None:
#     if board[1][0] == "X":
#         print("X")
#     else:
#         print("O")
# elif board[2][0] == board[2][1] == board[2][2] != None:
#     if board[2][0] == "X":
#         print("X")
#     else:
#         print("O")
# elif board[0][0] == board[1][0] == board[2][0] != None:
#     if board[0][0] == "X":
#         print("X")
#     else:
#         print("O")
# elif board[0][1] == board[1][1] == board[2][1] != None:
#     if board[0][1] == "X":
#         print("X")
#     else:
#         print("O")
# elif board[0][2] == board[1][2] == board[2][2] != None:
#     if board[0][2] == "X":
#         print("X")
#     else:
#         print("O")
# elif board[0][0] == board[1][1] == board[2][2] != None:
#     if board[0][0] == "X":
#         print("X")
#     else:
#         print("O")
# else:
#     print("None")

print(math.inf > 9)