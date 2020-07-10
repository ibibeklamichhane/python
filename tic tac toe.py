theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys=[]
for key in theBoard:
    board_key.append(key)        
            

#making board to play
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])



#playing games by players
def game():
    turn='x' #for turn x only
    count = 0 #initially played 0 times




    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?")

        move=input()


        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1

        else:
            print("that place is already taken.move other place,")
            continue



        #checking rows winner for every count above five
        if count >=5:
            if theBoard['7'] == theBoard['8'] == theBoard['9']!='':
                print("game over")
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break



            elif theBoard['4'] == theBoard['5'] == theBoard['6']!='':
                print("game over")
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****") 
                break   
                

            elif theBoard['1'] == theBoard['2'] == theBoard['3']!='':
                print("game over")
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
        
        #checking columns for winner 
            elif theBoard['1'] == theBoard['4'] == theBoard['7']!='':
                print("game over")
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break

            elif theBoard['2'] == theBoard['5'] == theBoard['8']!='':
                print("game over")
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break

            elif theBoard['3'] == theBoard['6'] == theBoard['9']!='':
                print("game over")
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break

            #checking for diagonal
            elif theBoard['7'] == theBoard['5'] == theBoard['3']!='':
                print("game over")
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break

            elif theBoard['9'] == theBoard['5'] == theBoard['1']!='':
                print("game over")
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break



            #if more than nine counts and still no result
            if count == 9:

                print("\nGame Over.\n")                
                print("It's a Tie!!")


            if turn =='X':
                turn = 'O'
            else:
                turn = 'X' 
game()    

                                    
