import sys
import math
game = [0,0,0,
        0,0,0,
        0,0,0]

#Printing box of game
def tic_tac_toe ():

 print ('|' ,game[0],'|',game[1] ,'|', game[2],'|')



 print ('|' ,game[3],'|',game[4] ,'|', game[5],'|')



 print ('|' ,game[6],'|',game[7] ,'|', game[8],'|')

#Player1 input
def game1():
    print("Player 1’s chance")
    print("Enter the position and number to be entered: ")

    x1 = int(input())                #Taking position
    x2 = int(input())                #Taking number

    if x1 < 9:
        game[x1-1] = x2

        tic_tac_toe()
        game2()
    else:
        print("invalid number")

#player2 input
def game2():
    print("Player 1’s chance")
    print("Enter the position and number to be entered: ")

    x1 = int(input())  # Taking position
    x2 = int(input())  # Taking number

    if x1 < 9:
        game[x1 - 1] = x2

        tic_tac_toe()
        game1()
    else:
        print("invalid number")



print("Welcome to the Game!")

game1()






tic_tac_toe()

while (true):

    turn(B)

    p1(x1)
    break
