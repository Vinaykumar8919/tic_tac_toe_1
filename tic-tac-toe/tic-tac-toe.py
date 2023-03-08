import random
import sys
import time
import os
n=[x for x in range(1,10)]
board=[" " for x in range(1,10)]
def print_board():
    print("| {} | {} | {} |".format(board[0],board[1],board[2]))
    print("| {} | {} | {} |".format(board[3],board[4],board[5]))
    print("| {} | {} | {} |".format(board[6],board[7],board[8]))

    
def player_move(icon):
    if icon=="X":
        number=1;
    elif icon=="O":
        number=2
    print("Your turn Player -",number)
    choice1=int(input("Enter your move(1-9):"))
    if choice1>0 and choice1<=9:
        if board[choice1-1]==" ":
            board[choice1-1]=icon
        else:
            print()
            print("The space was taken :(")
            print()
            player_move(icon)
    else:
        print("invalid move...try again")
        player_move(icon)

def player_com(icon):
    n1=random.choice(n)
    print("computer turn..........")
    time.sleep(0.5)
    
    time.sleep(1)
    if board[n1-1]==" ":
        print(n1)
        board[n1-1]=icon
    else:
        player_com(icon)
    
def is_victory(icon):
    if (board[0]==icon and board[1]==icon and board[2]==icon) or\
        (board[3]==icon and board[4]==icon and board[5]==icon) or\
        (board[6]==icon and board[7]==icon and board[8]==icon) or\
        (board[0]==icon and board[3]==icon and board[6]==icon) or\
        (board[1]==icon and board[4]==icon and board[7]==icon) or\
        (board[2]==icon and board[5]==icon and board[8]==icon) or\
        (board[0]==icon and board[4]==icon and board[8]==icon) or\
        (board[2]==icon and board[4]==icon and board[6]==icon):
        return True
    else:
        return False
def is_draw():
    if" " in board:
        return False
    else:
        return True  



while 1:
    ch=int(input("Which mode you want to play \n 1.computer vs palyer\n  2.player vs player : "))
    if ch==1:
        while True:
            print_board()
            player_move("X")
            print_board()
            if is_victory("X"):
                print("player (X) win.... Congrulations")
                break
               
            elif is_draw():
                print("is is a draw")
                break
                
            player_com("O")
            if is_victory("O"):
                print_board()
                print("player (O) win.... Congrulations")
                break
                
            elif is_draw():
                print("is is a draw")
                break
                

    elif ch==2:
        while True:
            print_board()
            player_move("X")
            print_board()
            if is_victory("X"):
                print("player (X) win.... Congrulations")
                break
                
            elif is_draw():
                print("is is a draw")
                break
                
            player_move("O")
            if is_victory("O"):
                print_board()
                print("player (O) win.... Congrulations")
                break
                
            elif is_draw():
                print("is is a draw")
                break
               
    else:
        print("Enter again:")

