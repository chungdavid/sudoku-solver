board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(board):
    for i in range(len(board)):
        #print horizontal line after every third row
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
            
        #print vertical line after every third column
        for j in range(len(board[0])):
            if j % 3 == 0 and j !=0:
                print("| ", end="")
            
            if j == 8: #start new line if num is last in row
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

#returns (row, column) of an empty space on the board (denoted by 0)
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] ==  0:
                return (i, j)

    return None #return None if no blank squares

#check if inputted num is valid
def valid(board, num, pos):

    #check if row is valid
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    #check if column is valid
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    #check if box is valid
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True

#solve board with backtracking
def solve(board):
    find = find_empty(board)
    if not find: #return True (board is solved) if no empty spaces
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(board, i, (row, col)): #if a num is valid, add to empty space
            board[row][col] = i

            if solve(board): #continue solving board with new values added, return True if solved
                return True

            board[row][col] = 0 #if cannot continue solve (returns False), backtrack to last value and reset to 0

    return False

print("Unsolved sudoku board:")
print_board(board)
solve(board)
print("\nSolved sudoku board:")
print_board(board)
