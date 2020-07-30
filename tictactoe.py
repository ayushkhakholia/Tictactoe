print("\t\t\t\tWELCOME TO TICTACTOE GAME")
theBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,'4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }


def printBoard(board):
    print("",end="\t\t\t\t")
    print(board['1'] + '  |  ' + board['2'] + '  |  ' + board['3'])
    print("",end="\t\t\t\t")
    print('------------')
    print("",end="\t\t\t\t")
    print(board['4'] + '  |  ' + board['5'] + '  |  ' + board['6'])
    print("",end="\t\t\t\t")
    print('------------')
    print("",end="\t\t\t\t")
    print(board['7'] + '  |  ' + board['8'] + '  |  ' + board['9'])


def game():

   
    turn = 'X'
    count = 0
    name1=input("Please enter the name of first player")
    name2=input("Please enter the name of second player")
    name=name1


    for i in range(40):
        printBoard(theBoard)
        print("It's your turn," + name + ".Move to which place?")
        try:
            move = input()   
        

            if theBoard[move] == ' ':
                theBoard[move] = turn
                count += 1
            else:
                print("That place is already filled.\nMove to which place?")
                continue
        except:
            print("Please enter a valid spot")
            continue
       
        if count >= 5:
            if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print("Congrats" +name+ " you won")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print("Congrats" +name+ " you won")
                break
            elif theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print("Congrats" +name+ " you won")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print("Congrats" +name+ " you won")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print("Congrats" +name+ " you won")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print("Congrats" +name+ " you won")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print("Congrats" +name+ " you won")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")      
                print("Congrats" +name+ " you won")            
                break 

       
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        if turn =='X':
            turn = 'O'
            name=name2
            
        else:
            turn = 'X'     
            name=name1  
    

game()
