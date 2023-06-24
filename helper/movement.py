#This file will contain all the legal moves for different kinds of pieces
class Pawn:
    def __init__(self, row, col, color):
        self.value = 1
        self.row = row
        self.col = col
        self.color = color


class Knight:
    def __init__(self, row, col, color):
        self.value = 3
        self.row = row
        self.col = col
        self.color = color


class Bishop:
    def __init__(self, row, col, color):
        self.value = 3
        self.row = row
        self.col = col
        self.color = color


class Rook:
    def __init__(self, row, col, color):
        self.value = 5
        self.row = row
        self.col = col
        self.color = color
    
    # All possible moves
    def move(self, board):
        moves = []
        #up movement
        for row in range(self.row - 1, -1, -1):
            tile = board[row][self.col]
            if tile.piece != None and tile.piece.color == self.color:
                break
            moves.append([row, self.col])
            if tile.piece != None:
                break
        #down movement
        for row in range(self.row + 1, 8):
            tile = board[row][self.col]
            if tile.piece != None and tile.piece.color == self.color:
                break
            moves.append([row, self.col])
            if tile.piece != None:
                break
        #left movement
        for col in range(self.col - 1, -1, -1):
            tile = board[self.row][col]
            if tile.piece != None and tile.piece.color == self.color:
                break
            moves.append([self.row, col])
            if tile.piece != None:
                break
        #right movement
        for col in range(self.col + 1, 8):
            tile = board[self.row][col]
            if tile.piece != None and tile.piece.color == self.color:
                break
            moves.append([self.row, col])
            if tile.piece != None:
                break

        return moves


class Queen:
    def __init__(self, row, col, color):
        self.value = 10
        self.row = row
        self.col = col
        self.color = color


class King:
    def __init__(self, row, col, color):
        self.value = 100
        self.row = row
        self.col = col
        self.color = color
