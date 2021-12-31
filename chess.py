from board import Board
from pieces import *

check = {"[♙]": "Black", "[♖]": "Black", "[♘]": "Black", "[♗]": "Black", "[♔]": "Black", "[♕]": "Black",
         "[♟]": "White", "[♜]": "White", "[♞]": "White", "[♝]": "White", "[♚]": "White", "[♛]": "White"}

blackIcons = {"Pawn": "♙", "Rook": "♖", "Knight": "♘", "Bishop": "♗", "King": "♔", "Queen": "♕"}
whiteIcons = {"Pawn": "♟", "Rook": "♜", "Knight": "♞", "Bishop": "♝", "King": "♚", "Queen": "♛"}


class Chess:
    def __init__(self):
        self.board = Board()
        self.currentPlayer = "White"

    def swapPlayers(self):
        if self.currentPlayer == "White":
            self.currentPlayer = "Black"
        else:
            self.currentPlayer = "White"

    def isStringValidMove(self, moveStr):
        if check.get(self.board.getPiece(moveStr)) != self.currentPlayer:
            return False
        else:

            return True

    def play(self):
        while True:
            self.board.displayBoard()
            print("{} turn. Enter a move: ".format(self.currentPlayer))
            submit = input()
            answer = submit.split()

            if submit == "EXIT":
                break
            else:
                if not self.isStringValidMove(answer[0]) or not self.board.makeMove(answer[0], answer[1],
                                                                                    self.currentPlayer):
                    print("Wrong input")
                    while True:
                        submit = input()
                        answer = submit.split()
                        if self.isStringValidMove(answer[0]) and self.board.makeMove(answer[0], answer[1],
                                                                                     self.currentPlayer):
                            break
                        else:
                            print("Wrong input")
                if answer[1][0] == "A" or answer[1][0] == "H":
                    while True:
                        prompt = input("Choose piece between : Bishop : Queen : Knight : Rook :  ")
                        print()
                        if prompt == "Bishop" or prompt == "Queen" or prompt == "Knight" or prompt == "Rook":
                            if self.currentPlayer == "White":
                                self.board.setPiece(answer[1], "{}".format(whiteIcons.get(prompt)))
                                break
                            elif self.currentPlayer == "Black":
                                self.board.setPiece(answer[1], "{}".format(blackIcons.get(prompt)))
                                break
                self.swapPlayers()



if __name__ == "__main__":
    game = Chess()
    game.play()
