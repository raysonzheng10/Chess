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
    def move(self):
        moves = []
        for row in range(8):
            moves.append([row, self.col])
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
