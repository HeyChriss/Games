
#This is an assigment for week number 2 and it was create by Christian Mijangos 2022

# This is the board where I am creating a dictionary and 
#creating values, when the user types the key automatically we will append the value (x or o)

Board =     {'1': ' ' , '2': ' ' , '3': ' ',
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

keys = []

for key in Board:
    keys.append(key)

# I created this function to print the board and put is as one variable so it is easy to print it 
# this is attached with the value of the Board so every change in the game will show up whenever it prints.  

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

# This is the main funtion
def main():

    turn = 'X'  #as default X will be turn 
    count = 0   #this is going to help us out to count the moves and determine 
                #if it is a tie in the future


    for i in range(10):
        printBoard(Board)
        print(f"It's your turn, {turn} turn to choose a square (1-9):")

        move = input()        

        if Board[move] == ' ':
            Board[move] = turn
            count += 1
        else:
            print("That place is already filled.")
            continue

        # Now we will check what player will win according to the location  
        if count >= 5:
            if Board['7'] == Board['8'] == Board['9'] != ' ': 
                printBoard(Board)             
                print(f'Game Over, {turn} won the game')                
                break
            elif Board['4'] == Board['5'] == Board['6'] != ' ': 
                printBoard(Board)               
                print(f'Game Over, {turn} won the game')
                break
            elif Board['1'] == Board['2'] == Board['3'] != ' ': 
                printBoard(Board)               
                print(f'Game Over, {turn} won the game')
                break
            elif Board['1'] == Board['4'] == Board['7'] != ' ': 
                printBoard(Board)             
                print(f'Game Over, {turn} won the game')
                break
            elif Board['2'] == Board['5'] == Board['8'] != ' ': 
                printBoard(Board)
                print(f'Game Over, {turn} won the game')
                break
            elif Board['3'] == Board['6'] == Board['9'] != ' ': 
                printBoard(Board)               
                print(f'Game Over, {turn} won the game')
                break 
            elif Board['7'] == Board['5'] == Board['3'] != ' ': 
                printBoard(Board)                
                print(f'Game Over, {turn} won the game')
                break
            elif Board['1'] == Board['5'] == Board['9'] != ' ': 
                printBoard(Board)                
                print(f'Game Over, {turn} won the game')
                break 

        # we'll declare the result as 'tie' if no one wins 
        if count == 9:               
            print("It's a Tie!")

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)").capitalize
    if restart == "Y":  
        for key in keys:
            Board[key] = " "
    else:
        print('Thank you for playing')
        main()

if __name__ == "__main__":
    main()