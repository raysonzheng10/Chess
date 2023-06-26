#This file will contain all the legal moves for different kinds of pieces
class Pawn:
    def __init__(self, row, col, color):
        self.value = 1
        self.row = row
        self.col = col
        self.color = color
    
    def move(self, board):
        moves = []
        return moves


class Knight:
    def __init__(self, row, col, color):
        self.value = 3
        self.row = row
        self.col = col
        self.color = color

    def move(self, board):
        moves = []
        return moves


class Bishop:
    def __init__(self, row, col, color):
        self.value = 3
        self.row = row
        self.col = col
        self.color = color

    def move(self, board):
        moves = []
        #upright movement
        for col in range(self.col + 1, 8):
            if self.row - col + self.col < 0:
                break
            tile = board[self.row - col + self.col][col]
            if tile.piece != None and tile.piece.color == self.color:
                break
            moves.append([self.row - col + self.col, col])
            if tile.piece != None:
                break
        #upleft movement
        for col in range(self.col - 1, -1, -1):
            if self.row + col - self.col < 0:
                break
            tile = board[self.row + col - self.col][col]
            if tile.piece != None and tile.piece.color == self.color:
                break
            moves.append([self.row + col - self.col, col])
            if tile.piece != None:
                break
        #downright movement
        for col in range(self.col + 1, 8):
            if self.row + col - self.col < 0:
                break
            tile = board[self.row + col - self.col][col]
            if tile.piece != None and tile.piece.color == self.color:
                break
            moves.append([self.row + col - self.col, col])
            if tile.piece != None:
                break
        #downleft movement
        for col in range(self.col - 1, -1, -1):
            if self.row - col + self.col < 0:
                break
            tile = board[self.row - col + self.col][col]
            if tile.piece != None and tile.piece.color == self.color:
                break
            moves.append([self.row - col + self.col, col])
            if tile.piece != None:
                break
        return moves

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

    def move(self, board):
        moves = []
        return moves


class King:
    def __init__(self, row, col, color):
        self.value = 100
        self.row = row
        self.col = col
        self.color = color

    def move(self, board):
        moves = []
        return moves
