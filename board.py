from pieces import *

usable = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}

blackIcons = {"Pawn": "♙", "Rook": "♖", "Knight": "♘", "Bishop": "♗", "King": "♔", "Queen": "♕"}
whiteIcons = {"Pawn": "♟", "Rook": "♜", "Knight": "♞", "Bishop": "♝", "King": "♚", "Queen": "♛"}

use = ("A", "B", "C", "D", "E", "F", "G", "G")


class Board:

    def __init__(self):
        self.board = []
        self.placePieces()

    def placePieces(self):
        self.board = [[" ", "  (1)", " (2)", " (3)", " (4)", " (5)", "(6)", " (7)", " (8)"],
                      ["(A)", "[♖]", "[♘]", "[♗]", "[♕]", "[♔]", "[♗]", "[♘]", "[♖]"],
                      ["(B)", "[♙]", "[♙]", "[♙]", "[♙]", "[♙]", "[♙]", "[♙]", "[♙]"],
                      ["(C)", "[ ]", "[  ]", "[  ]", "[  ]", "[ ]", "[  ]", "[ ]", "[  ]"],
                      ["(D)", "[ ]", "[  ]", "[  ]", "[  ]", "[ ]", "[  ]", "[ ]", "[  ]"],
                      ["(E)", "[ ]", "[  ]", "[  ]", "[  ]", "[ ]", "[  ]", "[ ]", "[  ]"],
                      ["(F)", "[ ]", "[  ]", "[  ]", "[  ]", "[ ]", "[  ]", "[ ]", "[  ]"],
                      ["(G)", "[♟]", "[♟]", "[♟]", "[♟]", "[♟]", "[♟]", "[♟]", "[♟]"],
                      ["(H)", "[♜]", "[♞]", "[♝]", "[♛]", "[♚]", "[♝]", "[♞]", "[♜]"]]

    def setPiece(self, position, piece):
        if 65 <= ord(position[0]) <= 72 and 1 <= int(position[1]) <= 8:
            if piece == "[  ]" or piece == "[ ]":
                self.board[usable.get(position[0])][int(position[1])] = piece
            else:
                self.board[usable.get(position[0])][int(position[1])] = "[{}]".format(piece)

    def getPiece(self, position):
        if 65 <= ord(position[0]) <= 72 and 1 <= int(position[1]) <= 8:
            if self.board[usable.get(position[0])][int(position[1])] != "[ ]" and self.board[usable.get(position[0])][
                int(position[1])] != "[  ]":
                return self.board[usable.get(position[0])][int(position[1])]
            else:
                return None

    def makeMove(self, startPosition, endPosition, player):
        joke = Pawn(player, self, startPosition)
        cry = King(player, self, startPosition)
        mooon = Knight(player, self, startPosition)
        rook = Rook(player, self, startPosition)
        bish = Bishop(player, self, startPosition)
        queen = Queen(player, self, startPosition)
        if player == "Black":
            if self.getPiece(startPosition) == "[♙]":
                if joke.move(endPosition):
                    self.setPiece(endPosition, "♙")
                    if int(startPosition[1]) == 2 or int(startPosition[1]) == 3 or int(
                            startPosition[1]) == 6 or int(
                        startPosition[1]) == 8:
                        self.setPiece(startPosition, "[  ]")
                    else:
                        self.setPiece(startPosition, "[ ]")
                    joke.position = endPosition
                    return True
                else:
                    return False



            elif self.getPiece(startPosition) == "[♖]":
                if rook.move(endPosition):
                    self.setPiece(endPosition, "♖")
                    if int(startPosition[1]) == 2 or int(startPosition[1]) == 3 or int(
                            startPosition[1]) == 6 or int(
                        startPosition[1]) == 8:
                        self.setPiece(startPosition, "[  ]")
                    else:
                        self.setPiece(startPosition, "[ ]")
                    joke.position = endPosition
                    return True
                else:
                    return False


            elif self.getPiece(startPosition) == "[♘]":
                if mooon.move(endPosition):
                    self.setPiece(endPosition, "♘")
                    if int(startPosition[1]) == 2 or int(startPosition[1]) == 3 or int(
                            startPosition[1]) == 6 or int(
                        startPosition[1]) == 8:
                        self.setPiece(startPosition, "[  ]")
                    else:
                        self.setPiece(startPosition, "[ ]")
                    joke.position = endPosition
                    return True
                else:
                    return False


            elif self.getPiece(startPosition) == "[♗]":
                if bish.move(endPosition):
                    self.setPiece(endPosition, "♗")
                    if int(startPosition[1]) == 2 or int(startPosition[1]) == 3 or int(
                            startPosition[1]) == 6 or int(
                        startPosition[1]) == 8:
                        self.setPiece(startPosition, "[  ]")
                    else:
                        self.setPiece(startPosition, "[ ]")
                    joke.position = endPosition
                    return True
                else:
                    return False


            elif self.getPiece(startPosition) == "[♔]":
                if cry.move(endPosition):
                    self.setPiece(endPosition, "♔")
                    if int(startPosition[1]) == 2 or int(startPosition[1]) == 3 or int(
                            startPosition[1]) == 6 or int(
                        startPosition[1]) == 8:
                        self.setPiece(startPosition, "[  ]")
                    else:
                        self.setPiece(startPosition, "[ ]")
                    joke.position = endPosition
                    return True
                else:
                    return False


            elif self.getPiece(startPosition) == "[♕]":
                if queen.move(endPosition):
                    self.setPiece(endPosition, "♕")
                    if int(startPosition[1]) == 2 or int(startPosition[1]) == 3 or int(
                            startPosition[1]) == 6 or int(
                        startPosition[1]) == 8:
                        self.setPiece(startPosition, "[  ]")
                    else:
                        self.setPiece(startPosition, "[ ]")
                    joke.position = endPosition
                    return True
                else:
                    return False

        if player == "White":
            if self.getPiece(startPosition) == "[♟]":
                if joke.move(endPosition):
                    self.setPiece(endPosition, "♟")
                    if int(startPosition[1]) == 2 or int(startPosition[1]) == 3 or int(
                            startPosition[1]) == 6 or int(
                        startPosition[1]) == 8:
                        self.setPiece(startPosition, "[  ]")
                    else:
                        self.setPiece(startPosition, "[ ]")
                    joke.position = endPosition
                    return True
                else:
                    return False


            elif self.getPiece(startPosition) == "[♜]":
                if rook.move(endPosition):
                    self.setPiece(endPosition, "♜")
                    if int(startPosition[1]) == 2 or int(startPosition[1]) == 3 or int(
                            startPosition[1]) == 6 or int(
                        startPosition[1]) == 8:
                        self.setPiece(startPosition, "[  ]")
                    else:
                        self.setPiece(startPosition, "[ ]")
                    joke.position = endPosition
                    return True
                else:
                    return False

            elif self.getPiece(startPosition) == "[♞]":
                if mooon.move(endPosition):
                    self.setPiece(endPosition, "♞")
                    if int(startPosition[1]) == 2 or int(startPosition[1]) == 3 or int(
                            startPosition[1]) == 6 or int(
                        startPosition[1]) == 8:
                        self.setPiece(startPosition, "[  ]")
                    else:
                        self.setPiece(startPosition, "[ ]")
                    joke.position = endPosition
                    return True
                else:
                    return False

            elif self.getPiece(startPosition) == "[♝]":
                if bish.move(endPosition):
                    self.setPiece(endPosition, "♝")
                    if int(startPosition[1]) == 2 or int(startPosition[1]) == 3 or int(
                            startPosition[1]) == 6 or int(
                        startPosition[1]) == 8:
                        self.setPiece(startPosition, "[  ]")
                    else:
                        self.setPiece(startPosition, "[ ]")
                    joke.position = endPosition
                    return True
                else:
                    return False

            elif self.getPiece(startPosition) == "[♚]":
                if cry.move(endPosition):
                    self.setPiece(endPosition, "♚")
                    if int(startPosition[1]) == 2 or int(startPosition[1]) == 3 or int(
                            startPosition[1]) == 6 or int(
                        startPosition[1]) == 8:
                        self.setPiece(startPosition, "[  ]")
                    else:
                        self.setPiece(startPosition, "[ ]")
                    joke.position = endPosition
                    return True
                else:
                    return False

            elif self.getPiece(startPosition) == "[♛]":
                if queen.move(endPosition):
                    self.setPiece(endPosition, "♛")
                    if int(startPosition[1]) == 2 or int(startPosition[1]) == 3 or int(
                            startPosition[1]) == 6 or int(
                        startPosition[1]) == 8:
                        self.setPiece(startPosition, "[  ]")
                    else:
                        self.setPiece(startPosition, "[ ]")
                    joke.position = endPosition
                    return True
                else:
                    return False

    def displayBoard(self):
        for r in self.board:
            for c in r:
                print(c, end="")
            print()
