import random

def set_board():
    #used to create and then reset the board
    global board
    board = [[1,2,3],[4,5,6],[7,8,9]]

def intro():
    print("Hello and welcome to endless Tic-Tac-Toe!")
    display()
    input("I assume you know how to play. I'll go first. Ready? (Enter to Continue) ")

def display():
    #displays the board based on current board
    counter = 1
    box = 1
    row=0
    while counter <= 13:
        if counter in [1,5,9,13]:
            print("+",7*"-","+",7*"-","+",7*"-","+",sep="", end="") # creates cross hatch lines
        elif counter in [2,4,6,8,10,12]:
            print("""|       |       |       |""", end="") # creates border on lines without numbers
        else:
            print("|", end="")
            for i in [0,1,2]:
                print("""  """, board[row][i], """  |""", end="") # creates the lines with board condition
            row +=1
        print("")
        counter +=1



def change_board(pick, y = "o"):
    for m in range(3):
        for n in range(3):
            if board[m][n] == pick:
                board[m][n] = y
                return



def game_over():
    # Checks rows to see who won
    col = 1
    for i in [0, 1, 2]:
        c = []
        for m in board:
            c.append(m[i])
        if c[0] == c[1] == c[2]:
            if c[0] == 'x':
                print("The computer wins by completing column: ", col)
                global.comp_wins +=1
            else:
                print("Congrats you won by complete column: ", col)
                global.user_wins +=1
            return False
        col += 1
    #Checks to see if anyone won a column
    c1, c2, c3 = [], [], []
    for n in [0, 1, 2]:
        c1.append(board[0][n])
        c2.append(board[1][n])
        c3.append(board[2][n])
    if c1[0] == c1[1] == c1[2]:
        if c1[0] == "x":
            print("The computer has won by completing row 1")
            comp_wins +=1
        else:
            print("The user has won by completing row 1")
            user_wins += 1
        return False
    if c2[0] == c2[1] == c2[2]:
        if c1[0] == "x":
            print("The computer has won by completing row 2")
            comp_wins +=1
        else:
            print("The user has won by completing row 2")
            user_wins +=1
        return False
    if c3[0] == c3[1] == c3[2]:
        if c1[0] == "x":
            print("The computer has won by completing row 3")
            comp_wins +=1
        else:
            print("The user has won by completing row 3")
            user_wins +=1
        return False
    #Checks diagnals
    if board[0][0] == board[1][1] == board[2][2] or board[2][0] == board[1][1] == board[0][2]:
        if board[1][1] == "x":
            print("The computer has won by completing row 3")
            comp_wins += 1
        else:
            print("The user has won by completing row 3")
            user_wins += 1
        return False
    return True


def spot_check(c):
    #Checks if a spot is available
    for m in board:
        for n in m:
            if n == c:
                return False
    return True

def play():
    run = True
    turn = 0
    while run:
        if turn == 0:
            change_board(5,"x")
            print("Computer picks the middle square, 5")
        elif turn % 2 == 0:
            prompt = True
            while prompt:
                r = random.randrange(1,10)
                prompt = spot_check(r)
            print("Computer picks", r)
            change_board(r,"x")
        else:
            prompt = True
            while prompt:
                c = int(input("What is your move? "))
                prompt = spot_check(c)
                if prompt:
                    print("Sorry that is not a valid pick")
            change_board(c, "o")
        turn += 1
        run = game_over()
        if turn == 9 and run == True:
            print("All spaces have been chosen without a winner. Game Over")
            run = False
            continue
        display()



if __name__ == '__main__':
    global user_wins, comp_wins
    user_wins, comp_wins = 0, 0
    run = True
    set_board()
    intro()
    while run:
        play()
        print("The current score is computer",comp_wins,"vs", user_wins,"user wins")
        check = True
        while check:
            run = False
            replay = input("Do you want to play again?[y/n] ")
            if replay == "y" or replay == "Y":
                set_board()
                check = False
                run = True
                continue
            elif replay == "n" or replay == "N":
                check = False
                replay = False
                run = False
                continue
            else:
                print("Please select a valid response")


#### done but could definetly be prettier. maybe check dataframes in python for easier checking



