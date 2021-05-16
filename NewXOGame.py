board = {'t': ' ', 'y': ' ', 'u': ' ',
         'g': ' ', 'h': ' ', 'j': ' ',
         'b': ' ', 'n': ' ', 'm': ' '}
boardKeys = []
for key in board:
    boardKeys.append(key)


def PrintBoard(board):
    print(board['t'] + "|" + board['y'] + "|" + board['u'])
    print("-+-+-")
    print(board['g'] + "|" + board['h'] + "|" + board['j'])
    print("-+-+-")
    print(board['b'] + "|" + board['n'] + "|" + board['m'])


def game():
    turn = 'X'
    count = 0
    n = 100
    for i in range(n):
        PrintBoard(board)
        print("Your Turn:" + turn)
        move = input()
        if move in board:
            if board[move] == ' ':
                board[move] = turn

                count = count + 1
            else:
                print("That place is already Filled! Vera Place kudra venna")
                continue
        else:
            print("Correct position kudra mairu")

            continue
        if count >= 5:
            if board['t'] == board['y'] == board['u'] != ' ':
                PrintBoard(board)
                print("\nGame Over!\n")
                print("\nThalaivan " + turn + " Won!\n")
                break
            elif board['g'] == board['h'] == board['j'] != ' ':
                PrintBoard(board)
                print("\nGame Over!\n")
                print("\nThalaivan " + turn + " Won!\n")
                break
            elif board['b'] == board['n'] == board['m'] != ' ':
                PrintBoard(board)
                print("\nGame Over!\n")
                print("\nThalaivan " + turn + " Won!\n")
                break
            elif board['b'] == board['g'] == board['t'] != ' ':
                PrintBoard(board)
                print("\nGame Over!\n")
                print("\nThalaivan " + turn + " Won!\n")
                break
            elif board['n'] == board['h'] == board['y'] != ' ':
                PrintBoard(board)
                print("\nGame Over!\n")
                print("\nThalaivan " + turn + " Won!\n")
                break
            elif board['m'] == board['j'] == board['u'] != ' ':
                PrintBoard(board)
                print("\nGame Over!\n")
                print("\nThalaivan " + turn + " Won!\n")
                break
            elif board['b'] == board['h'] == board['u'] != ' ':
                PrintBoard(board)
                print("\nGame Over!\n")
                print("\nThalaivan " + turn + " Won!\n")
                break
            elif board['t'] == board['h'] == board['m'] != ' ':
                PrintBoard(board)
                print("\nGame Over!\n")
                print("\nThalaivan " + turn + " Won!\n")
                break
        if count == 9:
            print("\nGame Over\n")
            print("It's a Tie!!Oruthanum Jeikala")
            break
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    restart = input("Do U Want to Play Again?Marupadiyum Aarambikalama??(y/n)")
    if restart == "y" or restart == "Y":
        for key in boardKeys:
            board[key] = ' '

        game()
    else:
        print("Thanks for Playing!Mikka Nandri")



game()
