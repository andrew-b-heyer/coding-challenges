def printBoard(board):
    # Helper function to debug and print the board
    for row in board:
        print(row)
    print()


def drawCounter(board, counter, position_current):
    # Variables to be used for calulcating in the following if
    top_of_board = 0
    bottom_of_board = len(board)-1 
    start_of_board = 0
    end_of_board = len(board)-1

    next_x = position_current.get('x') + 1
    next_y = position_current.get('y') - 1

    # Checks to see if our next x coordinate will be our of bounds
    if next_x > end_of_board:
        next_x = start_of_board

    if next_y < top_of_board:
        next_y = bottom_of_board

    # Checks to see if the next x coordinate already has been written on, if so draw "1 under" the current position
    if board[next_y][next_x] != 0:
        
        # The next position we will draw onto will be 1 below our current position
        board[next_y-1][next_x] = counter
        position_current["y"] = next_y-1
        position_current["x"] = next_x

    else:

        # The next position we will draw onto is 1 above, and 1 to the right of our current position
        board[next_y][next_x] = counter
        position_current["y"] = next_y
        position_current["x"] = next_x


def magicSquare(size):

    board = [ [0] * size for _ in range(size)]

    # The position in the 2d array we are in, starting at the middle top most location on the "board"
    middle_x = int(size/2)
    position_current = {'x' : middle_x, 'y' : 0}

    # Our counter should not exceed this value
    total_count = size*size

    # draw our initial starting point
    board[position_current.get("y")][position_current.get("x")] = 1
    
    # "counter" is also the current value we want to draw onto the board
    for counter in range(2,total_count+1):
        drawCounter(board, counter, position_current)
        # printBoard(board)
    printBoard(board)



if __name__ == "__main__":
    
    size = 3
    magicSquare(size)