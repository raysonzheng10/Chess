#This file will contain all the legal moves for different kinds of pieces
class Pawn:
    def __init__(self, row, col, color):
        self.value = 1
        self.row = row
        self.col = col
        self.color = color
    
    def move(self, board):
        moves = []
        #black pawn
        if self.color == "b":
            # Promotion
            if self.row == 7:
                self.promotion(board, "b")
            # From starting pos, get 2 steps
            elif self.row == 1:
                for row in range(2, 4):
                    tile = board[row][self.col]
                    if tile.piece != None:
                        break
                    moves.append([row, self.col])
            # 1 step elsewhere
            else:
                if board[self.row + 1][self.col].piece == None:
                    moves.append([self.row + 1, self.col])

            # add potential to do diagonal attacks
            # downright diagonal
            if self.col + 1 < 8 and self.row != 7:
                if board[self.row + 1][self.col + 1].piece != None and board[self.row + 1][self.col + 1].piece.color != self.color:
                    moves.append([self.row + 1, self.col + 1])
            # downleft diagonal
            if self.col - 1 > -1 and self.row !=7:
                if board[self.row + 1][self.col - 1].piece != None and board[self.row + 1][self.col - 1].piece.color != self.color:
                    moves.append([self.row + 1, self.col - 1])
            
            # En passant

        # white pawn
        else:
            if self.row == 0:
                self.promotion(board, "w")
            elif self.row == 6:
                for row in range(5, 3, -1):
                    tile = board[row][self.col]
                    if tile.piece != None:
                        break
                    moves.append([row, self.col])
            else:
                if board[self.row - 1][self.col].piece == None:
                    moves.append([self.row - 1, self.col])

            if self.col + 1 < 8 and self.row != 0:
                if board[self.row - 1][self.col + 1].piece != None and board[self.row - 1][self.col + 1].piece.color != self.color:
                    moves.append([self.row - 1, self.col + 1])
            if self.col - 1 > -1 and self.row != 0:
                if board[self.row - 1][self.col - 1].piece != None and board[self.row - 1][self.col - 1].piece.color != self.color:
                    moves.append([self.row - 1, self.col - 1])
        return moves
    
    
    def promotion(self, board, color):
        board[self.row][self.col].piece = Rook(self.row, self.col, "b")
        pass


class Knight:
    def __init__(self, row, col, color):
        self.value = 3
        self.row = row
        self.col = col
        self.color = color

    def move(self, board):
        moves = []
        row = self.row
        col = self.col

        #left moves
        if col - 2 > -1 and row + 1 < 8:
            if board[row + 1][col - 2].piece == None or board[row + 1][col - 2].piece.color != self.color:
                moves.append([row + 1, col - 2])
        if col - 2 > -1 and row - 1 > -1:
            if board[row - 1][col - 2].piece == None or board[row - 1][col - 2].piece.color != self.color:
                moves.append([row - 1, col - 2])
        #right moves
        if col + 2 < 8 and row + 1 < 8:
            if board[row + 1][col + 2].piece == None or board[row + 1][col + 2].piece.color != self.color:
                moves.append([row + 1, col + 2])
        if col + 2 < 8 and row - 1 > -1:
            if board[row - 1][col + 2].piece == None or board[row - 1][col + 2].piece.color != self.color:
                moves.append([row - 1, col + 2])
        #up moves
        if row - 2 > -1 and col + 1 < 8:
            if board[row - 2][col + 1].piece == None or board[row - 2][col + 1].piece.color != self.color:
                moves.append([row - 2, col + 1])
        if row - 2 > -1 and col - 1 > -1:
            if board[row - 2][col - 1].piece == None or board[row - 2][col - 1].piece.color != self.color:
                moves.append([row - 2, col - 1])
        #down moves
        if row + 2 < 8 and col + 1 < 8:
            if board[row + 2][col + 1].piece == None or board[row + 2][col + 1].piece.color != self.color:
                moves.append([row + 2, col + 1])
        if row + 2 < 8 and col - 1 > -1:
            if board[row + 2][col - 1].piece == None or board[row + 2][col - 1].piece.color != self.color:
                moves.append([row + 2, col - 1])
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
            if self.row + col - self.col > 7:
                break
            tile = board[self.row + col - self.col][col]
            if tile.piece != None and tile.piece.color == self.color:
                break
            moves.append([self.row + col - self.col, col])
            if tile.piece != None:
                break
        #downleft movement
        for col in range(self.col - 1, -1, -1):
            if self.row - col + self.col > 7:
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
        # diagonal movements
        for col in range(self.col + 1, 8):
            if self.row - col + self.col < 0:
                break
            tile = board[self.row - col + self.col][col]
            if tile.piece != None and tile.piece.color == self.color:
                break
            moves.append([self.row - col + self.col, col])
            if tile.piece != None:
                break
        for col in range(self.col - 1, -1, -1):
            if self.row + col - self.col < 0:
                break
            tile = board[self.row + col - self.col][col]
            if tile.piece != None and tile.piece.color == self.color:
                break
            moves.append([self.row + col - self.col, col])
            if tile.piece != None:
                break
        for col in range(self.col + 1, 8):
            if self.row + col - self.col > 7:
                break
            tile = board[self.row + col - self.col][col]
            if tile.piece != None and tile.piece.color == self.color:
                break
            moves.append([self.row + col - self.col, col])
            if tile.piece != None:
                break
        for col in range(self.col - 1, -1, -1):
            if self.row - col + self.col > 7:
                break
            tile = board[self.row - col + self.col][col]
            if tile.piece != None and tile.piece.color == self.color:
                break
            moves.append([self.row - col + self.col, col])
            if tile.piece != None:
                break
        for row in range(self.row - 1, -1, -1):
            tile = board[row][self.col]
            if tile.piece != None and tile.piece.color == self.color:
                break
            moves.append([row, self.col])
            if tile.piece != None:
                break

        # rook movements
        for row in range(self.row + 1, 8):
            tile = board[row][self.col]
            if tile.piece != None and tile.piece.color == self.color:
                break
            moves.append([row, self.col])
            if tile.piece != None:
                break
        for col in range(self.col - 1, -1, -1):
            tile = board[self.row][col]
            if tile.piece != None and tile.piece.color == self.color:
                break
            moves.append([self.row, col])
            if tile.piece != None:
                break
        for col in range(self.col + 1, 8):
            tile = board[self.row][col]
            if tile.piece != None and tile.piece.color == self.color:
                break
            moves.append([self.row, col])
            if tile.piece != None:
                break



        return moves


class King:
    def __init__(self, row, col, color):
        self.value = 100
        self.row = row
        self.col = col
        self.color = color
        self.check = False

    def move(self, board):
        moves = []
        row = self.row
        col = self.col

        #up,left,down,right


        return moves
