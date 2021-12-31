blackIcons = {"Pawn": "♙", "Rook": "♖", "Knight": "♘", "Bishop": "♗", "King": "♔", "Queen": "♕"}
whiteIcons = {"Pawn": "♟", "Rook": "♜", "Knight": "♞", "Bishop": "♝", "King": "♚", "Queen": "♛"}


class Piece:

    def __init__(self, color, board, position):
        self._color = color
        self._position = position
        self._board = board

    @property
    def color(self):
        return self._color

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if len(value[0]) == 1 and len(str(value[1])) == 1 and value[0].isalpha() and value[0].isupper() and str(
                value[1]).isdigit():
            if 65 <= ord(value[0]) <= 72 and 1 <= int(value[1]) <= 8:
                self._position = value
        else:
            raise ValueError("Something was indicated wrong")

    def checkMove(self, dest):
        return False

    def move(self, dest):
        return False

    def getName(self):
        return "Class Name -> {}".format(self.__class__.__name__)

    def getIcon(self):
        if self.color == "White":
            return whiteIcons
        elif self.color == "Black":
            return blackIcons
        else:
            return None


class Knight(Piece):

    def __init__(self, color, board, position):
        super().__init__(color, board, position)

    def getName(self):
        return "{}".format(self.__class__.__name__)

    def checkMove(self, dest):
        if self.color == "Black":
            if 1 <= int(dest[1]) <= 8 and 65 <= ord(dest[0]) <= 72:
                check = False
                if abs(ord(dest[0]) - ord(self.position[0])) == 2 and abs(int(dest[1]) - int(self.position[1])) == 1:
                    check = True
                elif abs(ord(dest[0]) - ord(self.position[0])) == 1 and abs(int(dest[1]) - int(self.position[1])) == 2:
                    check = True
                else:
                    check = False

                if check:
                    for key, value in blackIcons.items():
                        if "[{}]".format(blackIcons[key]) == self._board.getPiece(dest):
                            return False
                    for key, value in whiteIcons.items():
                        if "[{}]".format(whiteIcons[key]) == self._board.getPiece(dest):
                            return True
                    return True
                else:
                    return False
            else:
                return False
        elif self.color == "White":
            if 1 <= int(dest[1]) <= 8 and 65 <= ord(dest[0]) <= 72:
                check = False
                if abs(ord(dest[0]) - ord(self.position[0])) == 2 and abs(int(dest[1]) - int(self.position[1])) == 1:
                    check = True
                elif abs(ord(dest[0]) - ord(self.position[0])) == 1 and abs(int(dest[1]) - int(self.position[1])) == 2:
                    check = True
                else:
                    check = False

                if check:
                    for key, value in blackIcons.items():
                        if "[{}]".format(blackIcons[key]) == self._board.getPiece(dest):
                            return True
                    for key, value in whiteIcons.items():
                        if "[{}]".format(whiteIcons[key]) == self._board.getPiece(dest):
                            return False
                    return True
                else:
                    return False
        else:
            return False

    def move(self, dest):
        if self.checkMove(dest):
            if self._board.getPiece(dest) == "[♚]" or self._board.getPiece(dest) == "[♔]":
                return False
            else:
                return True
        else:
            return False


class Rook(Piece):

    def __init__(self, color, board, position):
        super().__init__(color, board, position)

    def getName(self):
        return "{}".format(self.__class__.__name__)

    def checkMove(self, dest):

        if self.color == "White":
            if 1 <= int(dest[1]) and 65 <= ord(dest[0]) <= 72:
                check = False
                if int(dest[1]) == int(self.position[1]):
                    if ord(dest[0]) > ord(self.position[0]):  # Deapth low
                        for number in range(ord(self.position[0]) + 1, ord(dest[0])):
                            if self._board.getPiece((chr(number), dest[1])) is not None:
                                check = False
                                break
                        else:
                            check = True
                    elif ord(dest[0]) < ord(self.position[0]):  # Deapth high
                        for number in range(ord(dest[0])+1,ord(self.position[0])):
                            if self._board.getPiece((chr(number),dest[1])) is not None:
                                check = False
                                break
                        else:
                            check = True
                elif ord(dest[0]) == ord(self.position[0]):
                    if int(dest[1]) < int(self.position[1]):  # breadth left
                        for number in range(int(dest[1]) + 1, int(self.position[1])):
                            if self._board.getPiece((dest[0], str(number))) is not None:
                                check = False
                                break

                        else:
                            check = True

                    elif int(dest[1]) > int(self.position[1]):
                        for number in range(int(self.position[1]) + 1, int(dest[1])):
                            if self._board.getPiece((dest[0], str(number))) is not None:
                                check = False
                                break
                        else:
                            check = True
                else:
                    check = False
                if check:
                    for key, value in blackIcons.items():
                        if "[{}]".format(blackIcons[key]) == self._board.getPiece(dest):
                            return True
                    for key, value in whiteIcons.items():
                        if "[{}]".format(whiteIcons[key]) == self._board.getPiece(dest):
                            return False
                    return True
                else:
                    return False
        elif self.color == "Black":
            if 1 <= int(dest[1]) and 65 <= ord(dest[0]) <= 72:
                check = False
                if int(dest[1]) == int(self.position[1]):
                    if ord(dest[0]) > ord(self.position[0]):  # Deapth low
                        for number in range(ord(self.position[0]) + 1, ord(dest[0])):
                            if self._board.getPiece((chr(number), dest[1])) is not None:
                                check = False
                                break
                        else:
                            check = True
                    elif ord(dest[0]) < ord(self.position[0]):  # Deapth high
                        for number in range(ord(dest[0]) + 1, ord(self.position[0])):
                            if self._board.getPiece((chr(number), dest[1])) is not None:
                                check = False
                                break
                        else:
                            check = True
                elif ord(dest[0]) == ord(self.position[0]):
                    if int(dest[1]) < int(self.position[1]):  # breadth left
                        for number in range(int(dest[1]) + 1, int(self.position[1])):
                            if self._board.getPiece((dest[0], str(number))) is not None:
                                check = False
                                break

                        else:
                            check = True

                    elif int(dest[1]) > int(self.position[1]):
                        for number in range(int(self.position[1]) + 1, int(dest[1])):
                            if self._board.getPiece((dest[0], str(number))) is not None:
                                check = False
                                break
                        else:
                            check = True
                else:
                    check = False
                if check:
                    for key, value in blackIcons.items():
                        if "[{}]".format(blackIcons[key]) == self._board.getPiece(dest):
                            return False
                    for key, value in whiteIcons.items():
                        if "[{}]".format(whiteIcons[key]) == self._board.getPiece(dest):
                            return True
                    return True
                else:
                    return False

    def move(self, dest):
        if self.checkMove(dest):
            if self._board.getPiece(dest) == "[♚]" or self._board.getPiece(dest) == "[♔]":
                return False
            else:
                return True
        else:
            return False


class Bishop(Piece):

    def __init__(self, color, board, position):
        super().__init__(color, board, position)

    def getName(self):
        return "{}".format(self.__class__.__name__)

    def checkMove(self, dest):
        x = ord(dest[0]) - 1
        y = x

        x1 = ord(dest[0]) + 1
        y1 = x1

        x2 = ord(self.position[0]) + 1
        y2 = x2

        z = ord(self.position[0]) - 1

        if self.color == "White":
            if 1 <= int(dest[1]) <= 8 and 65 <= ord(dest[0]) <= 72:
                check = False
                if abs(int(dest[1]) - int(self.position[1])) == abs(ord(dest[0]) - ord(self.position[0])):
                    check = True
                    if int(self.position[1]) > int(dest[1]) and ord(self.position[0]) < ord(dest[0]):  # Down Left +
                        for number in range(int(dest[1]) + 1, int(self.position[1])):
                            if self._board.getPiece((chr(y), number)) is not None:
                                check = False
                                break
                            y -= 1
                        else:
                            check = True
                    elif int(self.position[1]) > int(dest[1]) and ord(self.position[0]) > ord(dest[0]):  # Up Left +
                        for number in range(int(dest[1]) + 1, int(self.position[1])):
                            if self._board.getPiece((chr(y1), number)) is not None:
                                check = False
                                break
                            y1 += 1
                        else:
                            check = True
                    elif int(self.position[1]) < int(dest[1]) and ord(self.position[0]) < ord(dest[0]):  # Down right +
                        for number in range(int(self.position[1]) + 1, int(dest[1])):
                            if self._board.getPiece((chr(y2), number)) is not None:
                                check = False
                                break
                            y2 += 1
                        else:
                            check = True
                    elif int(self.position[1]) < int(dest[1]) and ord(self.position[0]) > ord(dest[0]):  # Up Right +
                        for number in range(int(self.position[1]) + 1, int(dest[1])):
                            if self._board.getPiece((chr(z), number)) is not None:
                                check = False
                                break
                            z -= 1
                        else:
                            check = True
                else:
                    check = False
                if check:
                    for key, value in blackIcons.items():
                        if "[{}]".format(blackIcons[key]) == self._board.getPiece(dest):
                            return True
                    for key, value in whiteIcons.items():
                        if "[{}]".format(whiteIcons[key]) == self._board.getPiece(dest):
                            return False
                    return True
                else:
                    return False
            else:
                return False

        elif self.color == "Black":
            if 1 <= int(dest[1]) <= 8 and 65 <= ord(dest[0]) <= 72:
                check = False
                if abs(int(dest[1]) - int(self.position[1])) == abs(ord(dest[0]) - ord(self.position[0])):
                    check = True
                    if int(self.position[1]) > int(dest[1]) and ord(self.position[0]) < ord(dest[0]):  # Down Left +
                        for number in range(int(dest[1]) + 1, int(self.position[1])):
                            if self._board.getPiece((chr(y), number)) is not None:
                                check = False
                                break
                            y -= 1
                        else:
                            check = True
                    elif int(self.position[1]) > int(dest[1]) and ord(self.position[0]) > ord(dest[0]):  # Up Left +
                        for number in range(int(dest[1]) + 1, int(self.position[1])):
                            if self._board.getPiece((chr(y1), number)) is not None:
                                check = False
                                break
                            y1 += 1
                        else:
                            check = True
                    elif int(self.position[1]) < int(dest[1]) and ord(self.position[0]) < ord(dest[0]):  # Down right +
                        for number in range(int(self.position[1]) + 1, int(dest[1])):
                            if self._board.getPiece((chr(y2), number)) is not None:
                                check = False
                                break
                            y2 += 1
                        else:
                            check = True
                    elif int(self.position[1]) < int(dest[1]) and ord(self.position[0]) > ord(dest[0]):  # Up Right +
                        for number in range(int(self.position[1]) + 1, int(dest[1])):
                            if self._board.getPiece((chr(y1), number)) is not None:
                                check = False
                                break
                            z -= 1
                        else:
                            check = True
                else:
                    check = False
                if check:
                    for key, value in blackIcons.items():
                        if "[{}]".format(blackIcons[key]) == self._board.getPiece(dest):
                            return False
                    for key, value in whiteIcons.items():
                        if "[{}]".format(whiteIcons[key]) == self._board.getPiece(dest):
                            return True
                    return True
                else:
                    return False
            else:
                return False

    def move(self, dest):
        if self.checkMove(dest):
            if self._board.getPiece(dest) == "[♚]" or self._board.getPiece(dest) == "[♔]":
                return False
            else:
                return True
        else:
            return False


class Queen(Piece):

    def __init__(self, color, board, position):
        super().__init__(color, board, position)

    def getName(self):
        return "{}".format(self.__class__.__name__)

    def checkMove(self, dest):
        x = ord(dest[0]) - 1
        y = x

        x1 = ord(dest[0]) + 1
        y1 = x1

        x2 = ord(self.position[0]) + 1
        y2 = x2

        z = ord(self.position[0]) - 1

        if self.color == "Black":
            if 1 <= int(dest[1]) <= 8 and 65 <= ord(dest[0]) <= 72:
                check = False
                if abs(ord(dest[0]) - ord(self.position[0])) == 2 and abs(
                        int(dest[1]) - int(self.position[1])) == 1:
                    return False
                elif abs(ord(dest[0]) - ord(self.position[0])) == 1 and abs(
                        int(dest[1]) - int(self.position[1])) == 2:
                    return False
                elif abs(int(dest[1]) - int(self.position[1])) == abs(ord(dest[0]) - ord(self.position[0])):
                    check = False
                    if int(self.position[1]) > int(dest[1]) and ord(self.position[0]) < ord(dest[0]):  # Down Left +
                        for number in range(int(dest[1]) + 1, int(self.position[1])):
                            if self._board.getPiece((chr(y), number)) is not None:
                                check = False
                                break
                            y -= 1
                        else:
                            check = True
                    elif int(self.position[1]) > int(dest[1]) and ord(self.position[0]) > ord(dest[0]):  # Up Left +
                        for number in range(int(dest[1]) + 1, int(self.position[1])):
                            if self._board.getPiece((chr(y1), number)) is not None:
                                check = False
                                break
                            y1 += 1
                        else:
                            check = True
                    elif int(self.position[1]) < int(dest[1]) and ord(self.position[0]) < ord(
                            dest[0]):  # Down right +
                        for number in range(int(self.position[1]) + 1, int(dest[1])):
                            if self._board.getPiece((chr(y2), number)) is not None:
                                check = False
                                break
                            y2 += 1
                        else:
                            check = True
                    elif int(self.position[1]) < int(dest[1]) and ord(self.position[0]) > ord(
                            dest[0]):  # Up Right +
                        for number in range(int(self.position[1]) + 1, int(dest[1])):
                            if self._board.getPiece((chr(z), number)) is not None:
                                check = False
                                break
                            z -= 1
                        else:
                            check = True
                elif int(dest[1]) == int(self.position[1]) or ord(dest[0]) == ord(self.position[0]):
                    check = False
                    if int(dest[1]) < int(self.position[1]) and ord(dest[0]) == ord(self.position[0]):  # breadth left
                        for number in range(int(dest[1]) + 1, int(self.position[1])):
                            if self._board.getPiece((dest[0], number)) is not None:
                                check = False
                                break
                        else:
                            check = True
                    elif int(dest[1]) > int(self.position[1]) and ord(dest[0]) == ord(
                            self.position[0]):  # breadth right:
                        for number in range(int(self.position[1]) + 1, int(dest[1])):
                            if self._board.getPiece((dest[0], number)) is not None:
                                check = False
                                break
                        else:
                            check = True
                    elif int(dest[1]) == int(self.position[1]) and ord(dest[0]) < ord(self.position[0]):  # Deapth high
                        for number in range(ord(dest[0]) + 1, ord(self.position[0])):
                            if self._board.getPiece((chr(number), dest[1])) is not None:
                                check = False
                                break
                        else:
                            check = True
                    elif int(dest[1]) == int(self.position[1]) and ord(dest[0]) > ord(self.position[0]):  # Deapth low
                        for number in range(ord(self.position[0]) + 1, ord(dest[0])):
                            if self._board.getPiece((chr(number), dest[1])) is not None:
                                check = False
                                break
                        else:
                            check = True
                if check:
                    for key, value in blackIcons.items():
                        if "[{}]".format(blackIcons[key]) == self._board.getPiece(dest) and self._board.getPiece(
                                dest) != "[♚]":
                            return False
                    for key, value in whiteIcons.items():
                        if "[{}]".format(whiteIcons[key]) == self._board.getPiece(dest):
                            return True
                    return True
                else:
                    return False
            else:
                return False

        elif self.color == "White":
            if 1 <= int(dest[1]) <= 8 and 65 <= ord(dest[0]) <= 72:
                check = False
                if abs(ord(dest[0]) - ord(self.position[0])) == 2 and abs(
                        int(dest[1]) - int(self.position[1])) == 1:
                    return False
                elif abs(ord(dest[0]) - ord(self.position[0])) == 1 and abs(
                        int(dest[1]) - int(self.position[1])) == 2:
                    return False
                elif abs(int(dest[1]) - int(self.position[1])) == abs(ord(dest[0]) - ord(self.position[0])):
                    check = False
                    if int(self.position[1]) > int(dest[1]) and ord(self.position[0]) < ord(dest[0]):  # Down Left +
                        for number in range(int(dest[1]) + 1, int(self.position[1])):
                            if self._board.getPiece((chr(y), number)) is not None:
                                check = False
                                break
                            y -= 1
                        else:
                            check = True
                    elif int(self.position[1]) > int(dest[1]) and ord(self.position[0]) > ord(dest[0]):  # Up Left +
                        for number in range(int(dest[1]) + 1, int(self.position[1])):
                            if self._board.getPiece((chr(y1), number)) is not None:
                                check = False
                                break
                            y1 += 1
                        else:
                            check = True
                    elif int(self.position[1]) < int(dest[1]) and ord(self.position[0]) < ord(dest[0]):  # Down right +
                        for number in range(int(self.position[1]) + 1, int(dest[1])):
                            if self._board.getPiece((chr(y2), number)) is not None:
                                check = False
                                break
                            y2 += 1
                        else:
                            check = True
                    elif int(self.position[1]) < int(dest[1]) and ord(self.position[0]) > ord(dest[0]):  # Up Right +
                        for number in range(int(self.position[1]) + 1, int(dest[1])):
                            if self._board.getPiece((chr(z), number)) is not None:
                                check = False
                                break
                            z -= 1
                        else:
                            check = True
                elif int(dest[1]) == int(self.position[1]) or ord(dest[0]) == ord(self.position[0]):
                    check = False
                    if int(dest[1]) < int(self.position[1]) and ord(dest[0]) == ord(self.position[0]):  # breadth left
                        for number in range(int(dest[1]) + 1, int(self.position[1])):
                            if self._board.getPiece((dest[0], number)) is not None:
                                check = False
                                break
                        else:
                            check = True
                    elif int(dest[1]) > int(self.position[1]) and ord(dest[0]) == ord(
                            self.position[0]):  # breadth right:
                        for number in range(int(self.position[1]) + 1, int(dest[1])):
                            if self._board.getPiece((dest[0], number)) is not None:
                                check = False
                                break
                        else:
                            check = True
                    elif int(dest[1]) == int(self.position[1]) and ord(dest[0]) < ord(self.position[0]):  # Deapth high
                        for number in range(ord(dest[0]) + 1, ord(self.position[0])):
                            if self._board.getPiece((chr(number), dest[1])) is not None:
                                check = False
                                break
                        else:
                            check = True
                    elif int(dest[1]) == int(self.position[1]) and ord(dest[0]) > ord(self.position[0]):  # Deapth low
                        for number in range(ord(self.position[0]) + 1, ord(dest[0])):
                            if self._board.getPiece((chr(number), dest[1])) is not None:
                                check = False
                                break
                        else:
                            check = True
                if check:
                    for key, value in blackIcons.items():
                        if "[{}]".format(blackIcons[key]) == self._board.getPiece(dest):
                            return True
                    for key, value in whiteIcons.items():
                        if "[{}]".format(whiteIcons[key]) == self._board.getPiece(dest):
                            return False
                    return True
                else:
                    return False
            else:
                return False

    def move(self, dest):
        if self.checkMove(dest):
            if self._board.getPiece(dest) == "[♚]" or self._board.getPiece(dest) == "[♔]":
                return False
            else:
                return True
        else:
            return False


class King(Piece):

    def __init__(self, color, board, position):
        super().__init__(color, board, position)

    def getName(self):
        return "{}".format(self.__class__.__name__)

    def checkMove(self, dest):
        if self.color == "White":
            if 1 <= int(dest[1]) <= 8 and 65 <= ord(dest[0]) <= 72:
                check = False
                if abs(ord(self._position[0]) - ord(dest[0])) == 0 and abs(int(dest[1]) - int(self.position[1])) == 1:
                    check = True
                elif abs(int(dest[1]) - int(self.position[1])) == 0 and abs(ord(dest[0]) - ord(self.position[0])) == 1:
                    check = True
                elif abs(int(self.position[1]) - int(dest[1])) == 1 and abs(ord(dest[0]) - ord(self.position[0])) == 1:
                    check = True

                if check:
                    for key, value in blackIcons.items():
                        if "[{}]".format(blackIcons[key]) == self._board.getPiece(dest):
                            return True
                    for key, value in whiteIcons.items():
                        if "[{}]".format(whiteIcons[key]) == self._board.getPiece(dest):
                            return False
                    return True
                else:
                    return False
            else:
                return False

        elif self.color == "Black":
            if 1 <= int(dest[1]) <= 8 and 65 <= ord(dest[0]) <= 72:
                check = False
                if self._position[0] == dest[0] and abs(int(dest[1]) - int(self.position[1])) == 1:
                    check = True
                elif self._position[1] == dest[1] and abs(ord(dest[0]) - ord(self.position[0])) == 1:
                    check = True
                elif abs(int(self.position[1]) - int(dest[1])) == 1 and abs(
                        ord(dest[0]) - ord(self.position[0])) == 1:
                    check = True
                else:
                    check = False

                if check:
                    for key, value in blackIcons.items():
                        if "[{}]".format(blackIcons[key]) == self._board.getPiece(dest):
                            return False
                    for key, value in whiteIcons.items():
                        if "[{}]".format(whiteIcons[key]) == self._board.getPiece(dest):
                            return True
                    return True
                else:
                    return False
            else:
                return False

    def move(self, dest):
        if self.checkMove(dest):
            if self._board.getPiece(dest) == "[♚]" or self._board.getPiece(dest) == "[♔]":
                return False
            else:
                return True
        else:
            return False


class Pawn(Piece):

    def __init__(self, color, board, position):
        super().__init__(color, board, position)

    def getName(self):
        return "{}".format(self.__class__.__name__)

    def checkMove(self, dest):
        if self.color == "White":
            if 1 <= int(dest[1]) <= 8 and 65 <= ord(dest[0]) <= 72:
                if self.position[0] == "G":
                    if (int(dest[1]) - int(self.position[1]) == 0 and (
                            ord(dest[0]) - ord(self.position[0])) == -1):
                        for key, value in blackIcons.items():
                            if "[{}]".format(blackIcons[key]) == self._board.getPiece(dest):
                                return False
                        for key, value in whiteIcons.items():
                            if "[{}]".format(whiteIcons[key]) == self._board.getPiece(dest):
                                return False
                        return True
                    elif int(dest[1]) - int(self.position[1]) == 0 and (ord(dest[0]) - ord(self.position[0])) == -2:
                        if self._board.getPiece(("F{}".format(int(dest[1])))) is not None:
                            return False
                        else:
                            for key, value in blackIcons.items():
                                if "[{}]".format(blackIcons[key]) == self._board.getPiece(dest):
                                    return False
                            for key, value in whiteIcons.items():
                                if "[{}]".format(whiteIcons[key]) == self._board.getPiece(dest):
                                    return False
                            return True

                    elif abs(int(self.position[1]) - int(dest[1])) == 1 and (
                            ord(dest[0]) - ord(self.position[0])) == -1:
                        for key, value in blackIcons.items():
                            if "[{}]".format(blackIcons[key]) == self._board.getPiece(dest):
                                return True
                        for key, value in whiteIcons.items():
                            if "[{}]".format(whiteIcons[key]) == self._board.getPiece(dest):
                                return False
                        return False
                    else:
                        return False
                elif self.position[0] != "G":
                    if (int(dest[1]) - int(self.position[1]) == 0 and (
                            ord(dest[0]) - ord(self.position[0])) == -1):
                        for key, value in blackIcons.items():
                            if "[{}]".format(blackIcons[key]) == self._board.getPiece(dest):
                                return False
                        for key, value in whiteIcons.items():
                            if "[{}]".format(whiteIcons[key]) == self._board.getPiece(dest):
                                return False
                        return True
                    elif abs(int(self.position[1]) - int(dest[1])) == 1 and (
                            ord(dest[0]) - ord(self.position[0])) == -1:
                        for key, value in blackIcons.items():
                            if "[{}]".format(blackIcons[key]) == self._board.getPiece(dest):
                                return True
                        for key, value in whiteIcons.items():
                            if "[{}]".format(whiteIcons[key]) == self._board.getPiece(dest):
                                return False
                        return False
                    else:
                        return False

            else:
                return False

        elif self.color == "Black":
            if 1 <= int(dest[1]) <= 8 and 65 <= ord(dest[0]) <= 72:
                if self.position[0] == "B":
                    if (int(dest[1]) - int(self.position[1]) == 0 and (
                            ord(dest[0]) - ord(self.position[0])) == 1):
                        for key, value in blackIcons.items():
                            if "[{}]".format(blackIcons[key]) == self._board.getPiece(dest):
                                return False
                        for key, value in whiteIcons.items():
                            if "[{}]".format(whiteIcons[key]) == self._board.getPiece(dest):
                                return False
                        return True
                    elif int(dest[1]) - int(self.position[1]) == 0 and (ord(dest[0]) - ord(self.position[0])) == 2:
                        if self._board.getPiece("C{}".format(int(dest[1]))) is not None:
                            return False
                        else:
                            for key, value in blackIcons.items():
                                if "[{}]".format(blackIcons[key]) == self._board.getPiece(dest):
                                    return False
                            for key, value in whiteIcons.items():
                                if "[{}]".format(whiteIcons[key]) == self._board.getPiece(dest):
                                    return False
                            return True

                    elif abs(int(self.position[1]) - int(dest[1])) == 1 and (
                            ord(dest[0]) - ord(self.position[0])) == 1:
                        for key, value in blackIcons.items():
                            if "[{}]".format(blackIcons[key]) == self._board.getPiece(dest):
                                return False
                        for key, value in whiteIcons.items():
                            if "[{}]".format(whiteIcons[key]) == self._board.getPiece(dest):
                                return True
                        return False
                    else:
                        return False
                elif self.position[0] != "B":
                    if (int(dest[1]) - int(self.position[1]) == 0 and (
                            ord(dest[0]) - ord(self.position[0])) == 1):
                        for key, value in blackIcons.items():
                            if "[{}]".format(blackIcons[key]) == self._board.getPiece(dest):
                                return False
                        for key, value in whiteIcons.items():
                            if "[{}]".format(whiteIcons[key]) == self._board.getPiece(dest):
                                return False
                        return True
                    elif abs(int(self.position[1]) - int(dest[1])) == 1 and (
                            ord(dest[0]) - ord(self.position[0])) == 1:
                        for key, value in blackIcons.items():
                            if "[{}]".format(blackIcons[key]) == self._board.getPiece(dest):
                                return False
                        for key, value in whiteIcons.items():
                            if "[{}]".format(whiteIcons[key]) == self._board.getPiece(dest):
                                return True
                        return False
                    else:
                        return False
            else:
                return False

    def move(self, dest):
        if self.checkMove(dest):
            if self._board.getPiece(dest) == "[♚]" or self._board.getPiece(dest) == "[♔]":
                return False
            else:
                return True
        else:
            return False
