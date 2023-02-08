gameboard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

restart = True
x_wins = False
y_wins = False
wave = 1

print("Welcome to Tic Tac Toe")
player_1 = input("Player 1, please enter your name:\n")
player_2 = input("Player 2, please enter your name:\n")
print("Below is the gameboard, each cell is represented by a number, the gameboard has 9 cells")

while restart:
    print(f"{gameboard[0]}\n{gameboard[1]}\n{gameboard[2]}")

    if wave % 2:
        try:
            choice_1 = int(input(f"{player_1}'s turn, please choose a cell"))
        except:
            ValueError
            print("Please enter a number within the limits of the cell")
        else:
            if choice_1 in gameboard[0] or choice_1 in gameboard[1] or choice_1 in gameboard[2]:
                if choice_1 in gameboard[0]:
                    position = gameboard[0].index(choice_1)
                    gameboard[0][position] = "X"
                    wave += 1
                elif choice_1 in gameboard[1]:
                    position = gameboard[1].index(choice_1)
                    gameboard[1][position] = "X"
                    wave += 1
                elif choice_1 in gameboard[2]:
                    position = gameboard[2].index(choice_1)
                    gameboard[2][position] = "X"
                    wave += 1

            else:
                print("This cell is occupied, try another")

    elif not wave % 2:
        try:
            choice_2 = int(input(f"{player_2}'s turn, please choose a cell"))
        except:
            ValueError
        else:
            if choice_2 in gameboard[0]:
                position = int(gameboard[0].index(choice_2))
                gameboard[0][position] = "O"
                wave += 1
            elif choice_2 in gameboard[1]:
                position = gameboard[1].index(choice_2)
                gameboard[1][position] = "O"
                wave += 1
            elif choice_2 in gameboard[2]:
                position = gameboard[2].index(choice_2)
                gameboard[2][position] = "O"
                wave += 1
            else:
                print("This cell is occupied, try another")

    if gameboard[0][0] == "X" and gameboard[1][0] == "X" and gameboard[2][0] == "X":
        x_wins = True
    if gameboard[0][1] == "X" and gameboard[1][1] == "X" and gameboard[2][1] == "X":
        x_wins = True
    if gameboard[0][2] == "X" and gameboard[1][2] == "X" and gameboard[2][2] == "X":
        x_wins = True
    if gameboard[0][0] == "X" and gameboard[0][1] == "X" and gameboard[0][2] == "X":
        x_wins = True
    if gameboard[1][0] == "X" and gameboard[1][1] == "X" and gameboard[1][2] == "X":
        x_wins = True
    if gameboard[2][0] == "X" and gameboard[2][1] == "X" and gameboard[2][2] == "X":
        x_wins = True
    if gameboard[0][0] == "X" and gameboard[1][1] == "X" and gameboard[2][2] == "X":
        x_wins = True
    if gameboard[0][2] == "X" and gameboard[1][1] == "X" and gameboard[2][0] == "X":
        x_wins = True

    if gameboard[0][0] == "O" and gameboard[1][0] == "O" and gameboard[2][0] == "O" or \
            gameboard[0][1] == "O" and gameboard[1][1] == "O" and gameboard[2][1] == "O" or \
            gameboard[0][2] == "O" and gameboard[1][2] == "O" and gameboard[2][2] == "O" or \
            gameboard[0][0] == "O" and gameboard[0][1] == "O" and gameboard[0][2] == "O" or \
            gameboard[1][0] == "O" and gameboard[1][1] == "O" and gameboard[1][2] == "O" or \
            gameboard[2][0] == "O" and gameboard[2][1] == "O" and gameboard[2][2] == "O" or \
            gameboard[0][0] == "O" and gameboard[1][1] == "O" and gameboard[2][2] == "O" or \
            gameboard[0][2] == "O" and gameboard[1][1] == "O" and gameboard[2][0] == "O":
        y_wins = True

    if 1 not in gameboard[0] and 2 not in gameboard[0] and 3 not in gameboard[0] and x_wins == False and y_wins == False and 4 not in gameboard[1] and 5 not in gameboard[1] and 6 not in gameboard[1] and 7 not in gameboard[2] and 8 not in gameboard[2] and 9 not in gameboard[2]:
        print(f"its a tie")
        again_loop = True
        while again_loop:
            again = input("Do you want to play again (Y or N?)").upper()
            if again == "Y":
                wave = 1
                gameboard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                x_wins = False
                y_wins = False
                again_loop = False
            elif again == "N":
                print("Goodbye")
                restart = False
                again_loop = False
            else:
                print("Please choose a valid argument")
    if x_wins:
        print(f"{player_1} Won")
        again_loop = True
        while again_loop:
            again = input("Do you want to play again (Y or N?)").upper()
            if again == "Y":
                wave = 1
                gameboard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                x_wins = False
                y_wins = False
                again_loop = False
            elif again == "N":
                print("Goodbye")
                restart = False
                again_loop = False
            else:
                print("Please choose a valid argument")

    elif y_wins:
        print(f"{player_2} Won")
        again_loop = True
        while again_loop:
            again = input("Do you want to play again (Y or N?)").upper()
            if again == "Y":
                gameboard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                x_wins = False
                y_wins = False
                again_loop = False
            elif again == "N":
                print("Goodbye")
                restart = False
                again_loop = False
            else:
                print("Please choose a valid argument")








