import tkinter as tk
import copy
import random

root = tk.Tk()

root.geometry('800x700')
root.title("New world")

#putting label or first header
label = tk.Label(root, text="Play 2048\nUse the arrow keys to combine tiles", font= ('Times New Roman', 15))
label.pack(padx=20, pady=20)


#making a frame for the button
buttonframe = tk.Frame(root)

score = 0
board = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]

def color(number: int) -> str:
    """
    Returns a color for each tile based on its value.

    Args:
        number (int):   The value of the tile; must be a power of 2 or 0.

    Returns:
        str:            The color for the tile.

    Examples:
        color(0)
        #>>> "white"

        color(2)
        #>>> "#3ca6a7

        color(4)
        #>>> #3c88a7
    """
    # teal, turquoise, denim blue, navy, plum, purple, mauve, magenta
    colors = ["#3ca6a7", "#3c88a7", "#234e9f", "dark slate blue", "#713ca7", "#913ca7", "#a73c78", "plum"]
    
    if number == 0:
        return "white"
             
    if number > 2048:
        return colors[-1]
             
    if number > 64:
        return colors[-2]
             
    for i in range(6):
        if 2 ** (i + 1) == number:
            return colors[i]

def left_move(board: list) -> tuple:
    """
    Returns the board and score change after the left arrow has been pushed.

    Args:
        board (list):               a 4 x 4 array of integers in which each
                                    element is either a positive power of 2 or a 0.

    Returns:

        final_board (list):         the board after the move is complete.

        score_change (int):         how many points the user scored from the
                                    move.

    Examples:

        left([[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 2],
              [0, 0, 0, 0]])
        #>>> ([[0, 0, 0, 0],
              [0, 0, 0, 0],
              [2, 0, 0, 0],
              [0, 0, 0, 0]], 0)

        left([[4, 8, 8, 16],
              [8, 64, 4, 2],
              [2, 2, 4, 4],
              [8, 8, 8, 8]])
        #>>> ([[4, 16, 16, 0],
              [8, 64, 4, 2],
              [4, 8, 0, 0],
              [16, 16, 0, 0]], 60)
    """
    score_change = 0

    #to avoid altering the initial board in conditional checks
    initial_board = copy.deepcopy(board)

    for ele in initial_board:

        i = 0

        for i in range(4):

            #same value only 1 index apart
            combine1 = i < 3 and ele[i] != 0 and ele[i] == ele[i + 1]

            #same value 2 indices apart
            combine2_1 = i < 2 and ele[i] != 0
            #0s in between
            combine2_2 = i < 2 and ele[i + 1] == 0 and ele[i] == ele [i + 2]
            combine2 = combine2_1 and combine2_2

            #same value 3 indices apart
            combine3_1 = i < 1 and ele[i] == ele [i + 3] and ele[i] != 0
            #0s in between
            combine3_2 = i < 1 and ele[i + 1] == 0 and ele[i + 2] == 0
            combine3 = combine3_1 and combine3_2

            if combine1 or combine2 or combine3:
                ele[i] = ele[i] * 2
                score_change += ele[i]
                ele[i + 1] = 0

            if combine2 or combine3:
                ele[i + 2] = 0

            if combine3:
                ele[i + 3] = 0

        k = 0

        #minimum number to cycle through 3 times (3 possible 0s before a no.)

        for i in range(12):

            if k != 3 and ele[k] == 0:
                del ele[k]
                ele += [0]

            k += 1

            if k == 3:
                k = 0

    final_board = initial_board

    return final_board, score_change

def right_move(board: list) -> tuple:
    """
   Returns the board and score change after the right arrow has been pushed.

   Args:
       board (list):               a 4 x 4 array of integers in which each
                                   element is either a positive power of 2 or a 0.

   Returns:

       final_board (list):         the board after the move is complete.

       score_change (int):         how many points the user scored from the
                                   move.

   Examples:

       right([[0, 0, 0, 0],
             [0, 0, 0, 0],
             [2, 0, 0, 0],
             [0, 0, 0, 0]])
       #>>> ([[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 2],
             [0, 0, 0, 0]], 0)

       right([[4, 8, 8, 16],
             [8, 64, 4, 2],
             [2, 2, 4, 4],
             [8, 8, 8, 8]])
       #>>> ([[0, 4, 16, 16],
             [8, 64, 4, 2],
             [0, 0, 4, 8],
             [0, 0, 16, 16]], 60)
   """
    score_change = 0

    # to avoid altering the initial board in conditional checks
    initial_board = copy.deepcopy(board)

    for ele in initial_board:
        ele[0], ele[1], ele[2], ele[3] = ele[3], ele[2], ele[1], ele[0]

        i = 0

        for i in range(4):

            # same value only 1 index apart
            combine1 = i < 3 and ele[i] != 0 and ele[i] == ele[i + 1]

            # same value 2 indices apart
            combine2_1 = i < 2 and ele[i] != 0
            # 0s in between
            combine2_2 = i < 2 and ele[i + 1] == 0 and ele[i] == ele[i + 2]
            combine2 = combine2_1 and combine2_2

            # same value 3 indices apart
            combine3_1 = i < 1 and ele[i] == ele[i + 3] and ele[i] != 0
            # 0s in between
            combine3_2 = i < 1 and ele[i + 1] == 0 and ele[i + 2] == 0
            combine3 = combine3_1 and combine3_2

            if combine1 or combine2 or combine3:
                ele[i] = ele[i] * 2
                score_change += ele[i]
                ele[i + 1] = 0

            if combine2 or combine3:
                ele[i + 2] = 0

            if combine3:
                ele[i + 3] = 0

        k = 0

        # minimum number to cycle through 3 times (3 possible 0s before a no.)

        for i in range(12):

            if k != 3 and ele[k] == 0:
                del ele[k]
                ele += [0]

            k += 1

            if k == 3:
                k = 0

        ele[0], ele[1], ele[2], ele[3] = ele[3], ele[2], ele[1], ele[0]

    final_board = initial_board

    return final_board, score_change

def up_move(board: list) -> tuple:
    """
    Returns the board and score change after the up arrow has been pushed.

    Args:
        board (list):               a 4 x 4 array of integers in which each
                                    element is either a positive power of 2 or a 0.

    Returns:

        final_board (list):         the board after the move is complete.

        score_change (int):         how many points the user scored from the
                                    move.

    Examples:

        up([[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 2],
              [0, 0, 0, 0]])
        #>>> ([[0, 0, 0, 2],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]], 0)

        up([[4, 8, 8, 16],
              [8, 64, 4, 16],
              [2, 2, 4, 4],
              [8, 8, 8, 8]])
        #>>> ([[4, 8, 8, 32],
              [8, 64, 8, 4],
              [2, 2, 8, 8],
              [8, 8, 0, 0]], 40)
    """
    score_change = 0

    # to avoid altering the initial board in conditional checks
    initial_board = copy.deepcopy(board)
    final_board = copy.deepcopy(board)

    for i in range(4):
        for j in range(4):
            initial_board[i][j] = board[j][i]

    for ele in initial_board:

        i = 0

        for i in range(4):

            # same value only 1 index apart
            combine1 = i < 3 and ele[i] != 0 and ele[i] == ele[i + 1]

            # same value 2 indices apart
            combine2_1 = i < 2 and ele[i] != 0
            # 0s in between
            combine2_2 = i < 2 and ele[i + 1] == 0 and ele[i] == ele[i + 2]
            combine2 = combine2_1 and combine2_2

            # same value 3 indices apart
            combine3_1 = i < 1 and ele[i] == ele[i + 3] and ele[i] != 0
            # 0s in between
            combine3_2 = i < 1 and ele[i + 1] == 0 and ele[i + 2] == 0
            combine3 = combine3_1 and combine3_2

            if combine1 or combine2 or combine3:
                ele[i] = ele[i] * 2
                score_change += ele[i]
                ele[i + 1] = 0

            if combine2 or combine3:
                ele[i + 2] = 0

            if combine3:
                ele[i + 3] = 0

        k = 0

        # minimum number to cycle through 3 times (3 possible 0s before a no.)

        for i in range(12):

            if k != 3 and ele[k] == 0:
                del ele[k]
                ele += [0]

            k += 1

            if k == 3:
                k = 0

    for i in range(4):
        for j in range(4):
            final_board[i][j] = initial_board[j][i]

    return final_board, score_change

def down_move(board: list) -> tuple:
    """
    Returns the board and score change after the up arrow has been pushed.

    Args:
        board (list):               a 4 x 4 array of integers in which each
                                    element is either a positive power of 2 or a 0.

    Returns:

        final_board (list):         the board after the move is complete.

        score_change (int):         how many points the user scored from the
                                    move.

    Examples:

        down([[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 2],
              [0, 0, 0, 0]])
        #>>> ([[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 2]], 0)

        down([[4, 8, 8, 16],
              [8, 64, 4, 16],
              [2, 2, 4, 4],
              [8, 8, 8, 8]])
        #>>> ([[4, 8, 0, 0],
              [8, 64, 8, 32],
              [2, 2, 8, 4],
              [8, 8, 8, 8]], 40)
    """
    score_change = 0

    # to avoid altering the initial board in conditional checks
    initial_board = copy.deepcopy(board)
    final_board = copy.deepcopy(board)

    for i in range(4):
        for j in range(4):
            initial_board[i][j] = board[j][i]

    for ele in initial_board:

        ele[0], ele[1], ele[2], ele[3] = ele[3], ele[2], ele[1], ele[0]

        i = 0

        for i in range(4):

            # same value only 1 index apart
            combine1 = i < 3 and ele[i] != 0 and ele[i] == ele[i + 1]

            # same value 2 indices apart
            combine2_1 = i < 2 and ele[i] != 0
            # 0s in between
            combine2_2 = i < 2 and ele[i + 1] == 0 and ele[i] == ele[i + 2]
            combine2 = combine2_1 and combine2_2

            # same value 3 indices apart
            combine3_1 = i < 1 and ele[i] == ele[i + 3] and ele[i] != 0
            # 0s in between
            combine3_2 = i < 1 and ele[i + 1] == 0 and ele[i + 2] == 0
            combine3 = combine3_1 and combine3_2

            if combine1 or combine2 or combine3:
                ele[i] = ele[i] * 2
                score_change += ele[i]
                ele[i + 1] = 0

            if combine2 or combine3:
                ele[i + 2] = 0

            if combine3:
                ele[i + 3] = 0

        k = 0

        # minimum number to cycle through 3 times (3 possible 0s before a no.)

        for i in range(12):

            if k != 3 and ele[k] == 0:
                del ele[k]
                ele += [0]

            k += 1

            if k == 3:
                k = 0

        ele[0], ele[1], ele[2], ele[3] = ele[3], ele[2], ele[1], ele[0]

    for i in range(4):
        for j in range(4):
            final_board[i][j] = initial_board[j][i]

    return final_board, score_change

def left(event) -> None:

    """
    Prints the board and score after the left arrow has been pushed.

    Args:
        event (tkinter.Event):      the tkinter event; left() is bound to the left arrow.

    Returns:

        None
    """
    global score
    global board
    initial_board = copy.deepcopy(board)
    score += left_move(board)[1]
    board = left_move(board)[0]

    if initial_board != board:
        new_tile(board)
    print_board()

def up(event) -> None:
    """
    Prints the board and score after the up arrow has been pushed.

    Args:
        event (tkinter.Event):      the tkinter event; up() is bound to the up arrow.

    Returns:

        None
    """
    global score
    global board
    initial_board = copy.deepcopy(board)
    score += up_move(board)[1]
    board = up_move(board)[0]

    if initial_board != board:
        new_tile(board)
    print_board()

def right(event) -> None:
    """
    Prints the board and score after the right arrow has been pushed.

    Args:
        event (tkinter.Event):      the tkinter event; right() is bound to the right arrow.

    Returns:

        None
    """
    global score
    global board
         
    initial_board = copy.deepcopy(board)
    score += right_move(board)[1]
    board = right_move(board)[0]

    if initial_board != board:
        new_tile(board)
    print_board()

def down(event) -> None:
    """
    Prints the board and score after the down arrow has been pushed.

    Args:
        event (tkinter.Event):      the tkinter event; down() is bound to the down arrow.

    Returns:

        None
    """

    global score
    global board
    
    #to avoid altering the initial board in conditional checks
    initial_board = copy.deepcopy(board)
    score += down_move(board)[1]
    board = down_move(board)[0]

    if initial_board != board:
        new_tile(board)
    print_board()

def new_tile(board: list) -> list:
    """
    Adds a new tile with value of 2 to a 2048 board, provided that a new tile can be added.

    Args:
        board (list):               a 4 x 4 array of integers in which each
                                    element is either a positive power of 2 or a 0.

    Returns:

        final_board (list):         the board after a new tile is added in a
                                    randomly selected spot that was previously empty. If tile was previously empty, the board is returned unchanged.

    Examples:
        new_tile([[4, 4, 4, 4],
                  [8, 0, 8, 8],
                  [4, 4, 4, 4],
                  [4, 4, 4, 4]])
        #>>> [[4, 4, 4, 4],
             [8, 2, 8, 8],
             [4, 4, 4, 4],
             [4, 4, 4, 4]]

        new_tile([[4, 4, 4, 4],
                  [8, 2, 8, 8],
                  [4, 4, 4, 4],
                  [4, 4, 4, 4]])
       # >>> [[4, 4, 4, 4],
             [8, 2, 8, 8],
             [4, 4, 4, 4],
             [4, 4, 4, 4]]
    """

    needs_new = False
    new_inserted = False

    for ele in board:
        if 0 in ele:
            needs_new = True

    while needs_new and new_inserted == False:
        column = random.randint(0, 3)
        row = random.randint(0, 3)

        if board[row][column] == 0:
            board[row][column] = 2
            new_inserted = True

    final_board = board

    return final_board

def print_board() -> None:
    """Prints the board (variable "board").

    Args:
        None

    Returns:
        None
    """
    for i in range(4):
        ele = board[i]
        for j in range(4):
            item = ele[j]
            tilelabel = tk.Label(buttonframe, text=f"{item}", font =("Times New Roman", 20), width = 10, height = 5, bg = color(item), relief = tk.SOLID, borderwidth = 1, fg = "white")
            tilelabel.grid(row=i, column=j)
                 
    global scorelabel
         
    if done() == True and 'scorelabel' in globals():
        scorelabel.destroy()
        scorelabel = tk.Label(root, text=f"Game over! Your score was: {score}", font=('Times New Roman', 15))
        scorelabel.pack(padx=20, pady=20)
             
    else:
        if 'scorelabel' in globals():
            scorelabel.destroy()
        scorelabel = tk.Label(root, text=f"Your score is: {score}", font=('Times New Roman', 15))
        scorelabel.pack(padx=20, pady=20)
             
    buttonframe.pack(padx = 20, pady = 20)

def done() -> bool:
    """
    Returns True if the game has been over, False otherwise.

    Args:
        None

    Returns:
        bool:   True if the game has been over, False otherwise.
    """
    return board == left_move(board)[0] == up_move(board)[0] == down_move(board)[0] == right_move(board)[0]

board = new_tile(board)
board = new_tile(board)
print_board()

root.bind("<Up>", up)
root.bind("<Down>", down)
root.bind("<Left>", left)
root.bind("<Right>", right)

root.mainloop()
