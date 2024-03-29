#!/bin/python3
from random import randrange
board=[1,2,3],[4,"X",6],[7,8,9,]

def display_board(board):
    solid=("+-------+-------+-------+")
    spaces=("|       |       |       |")
    print(solid,spaces,sep="\n")
    print("|   {}   |   {}   |   {}   |".format(board[0][0],board[0][1],board[0][2]))
    print(spaces,solid,spaces,sep="\n")
    print("|   {}   |   {}   |   {}   |".format(board[1][0],board[1][1],board[1][2]))
    print(spaces,solid,spaces,sep="\n")
    print("|   {}   |   {}   |   {}   |".format(board[2][0],board[2][1],board[2][2]))
    print(spaces,solid,sep="\n")
    
def your_move(board):
    move=int(input("Choose your move location: "))
    if move<1 or move>9:
        your_move(board)
    else:
        if board[(move-1)//3][(move-1)%3] not in ("X","O"):
            board[(move-1)//3][(move-1)%3]="O"
        else:
            print("Space not available")

def AI_move(board):
    move=randrange(1,10)
    if board[(move-1)//3][(move-1)%3] not in ("X","O"):
        board[(move-1)//3][(move-1)%3]="X"
    else:AI_move(board)

def victory_for(board):
    if board[0][0]==board[0][1]==board[0][2]:
        display_board(board)
        print(board[0][0]," WINS!")
        quit()
    if board[1][0]==board[1][1]==board[1][2]:
        display_board(board)
        print(board[1][0]," WINS!")
        quit()
    if board[2][0]==board[2][1]==board[2][2]:
        display_board(board)
        print(board[2][0]," WINS!")
        quit()
    if board[0][0]==board[1][1]==board[2][2]:
        display_board(board)
        print(board[0][0]," WINS!")
        quit()
    if board[0][2]==board[1][1]==board[2][0]:
        display_board(board)
        print(board[2][0]," WINS!")
        quit()
    if board[0][0]==board[1][0]==board[2][0]:
        display_board(board)
        print(board[2][0]," WINS!")
        quit()
    if board[0][1]==board[1][1]==board[2][1]:
        display_board(board)
        print(board[0][1]," WINS!")
        quit()
    if board[2][0]==board[1][2]==board[2][2]:
        display_board(board)
        print(board[2][0]," WINS!")
        quit()
    if (''.join(map(str,(sum(board,[]))))).isalpha():
        display_board(board)
        print("TIE!")
        quit()

while True:
    display_board(board)
    your_move(board)
    AI_move(board)
    victory_for(board)
