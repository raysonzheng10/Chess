#This file will contain all the legal moves for different kinds of pieces
import copy
from helper.constants import ROWS, COLS
        
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
        board[self.row][self.col].piece = Queen(self.row, self.col, color)


    def legal_moves(self, board, moves):
        legal_moves = []
        for row in range(ROWS):
            for col in range(COLS):
                tile = board[row][col]
                # Check if ally king is checked
                if type(tile.piece).__name__ == "King" and tile.piece.color == self.color:
                    for move in moves:
                        # create a deep copy of the board and emulate the move
                        copy_board = copy.deepcopy(board)
                        copy_board[move[0]][move[1]].piece = copy_board[self.row][self.col].piece
                        copy_board[self.row][self.col].piece = None
                        copy_board[move[0]][move[1]].piece.row = move[0]
                        copy_board[move[0]][move[1]].piece.col = move[1]
                        # if after the emulated move, king is not checked, we can play that move
                        if not tile.piece.is_checked(copy_board):
                            legal_moves.append(move)
        return legal_moves


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
    
    def legal_moves(self, board, moves):
        legal_moves = []
        for row in range(ROWS):
            for col in range(COLS):
                tile = board[row][col]
                # Check if ally king is checked
                if type(tile.piece).__name__ == "King" and tile.piece.color == self.color:
                    for move in moves:
                        # create a deep copy of the board and emulate the move
                        copy_board = copy.deepcopy(board)
                        copy_board[move[0]][move[1]].piece = copy_board[self.row][self.col].piece
                        copy_board[self.row][self.col].piece = None
                        copy_board[move[0]][move[1]].piece.row = move[0]
                        copy_board[move[0]][move[1]].piece.col = move[1]
                        # if after the emulated move, king is not checked, we can play that move
                        if not tile.piece.is_checked(copy_board):
                            legal_moves.append(move)
        return legal_moves


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

    def legal_moves(self, board, moves):
        legal_moves = []
        for row in range(ROWS):
            for col in range(COLS):
                tile = board[row][col]
                # Check if ally king is checked
                if type(tile.piece).__name__ == "King" and tile.piece.color == self.color:
                    for move in moves:
                        # create a deep copy of the board and emulate the move
                        copy_board = copy.deepcopy(board)
                        copy_board[move[0]][move[1]].piece = copy_board[self.row][self.col].piece
                        copy_board[self.row][self.col].piece = None
                        copy_board[move[0]][move[1]].piece.row = move[0]
                        copy_board[move[0]][move[1]].piece.col = move[1]
                        # if after the emulated move, king is not checked, we can play that move
                        if not tile.piece.is_checked(copy_board):
                            legal_moves.append(move)
        return legal_moves
                        

class Rook:
    def __init__(self, row, col, color):
        self.value = 5
        self.row = row
        self.col = col
        self.color = color
        self.castle = True
    
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

    def legal_moves(self, board, moves):
        legal_moves = []
        for row in range(ROWS):
            for col in range(COLS):
                tile = board[row][col]
                # Check if ally king is checked
                if type(tile.piece).__name__ == "King" and tile.piece.color == self.color:
                    for move in moves:
                        # create a deep copy of the board and emulate the move
                        copy_board = copy.deepcopy(board)
                        copy_board[move[0]][move[1]].piece = copy_board[self.row][self.col].piece
                        copy_board[self.row][self.col].piece = None
                        copy_board[move[0]][move[1]].piece.row = move[0]
                        copy_board[move[0]][move[1]].piece.col = move[1]
                        # if after the emulated move, king is not checked, we can play that move
                        if not tile.piece.is_checked(copy_board):
                            legal_moves.append(move)
        return legal_moves
                        




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


    def legal_moves(self, board, moves):
        legal_moves = []
        for row in range(ROWS):
            for col in range(COLS):
                tile = board[row][col]
                # Check if ally king is checked
                if type(tile.piece).__name__ == "King" and tile.piece.color == self.color:
                    for move in moves:
                        # create a deep copy of the board and emulate the move
                        copy_board = copy.deepcopy(board)
                        copy_board[move[0]][move[1]].piece = copy_board[self.row][self.col].piece
                        copy_board[self.row][self.col].piece = None
                        copy_board[move[0]][move[1]].piece.row = move[0]
                        copy_board[move[0]][move[1]].piece.col = move[1]
                        # if after the emulated move, king is not checked, we can play that move
                        if not tile.piece.is_checked(copy_board):
                            legal_moves.append(move)
        return legal_moves


class King:
    def __init__(self, row, col, color):
        self.value = 100
        self.row = row
        self.col = col
        self.color = color
        self.check = False
        self.castle = True

    def move(self, board):
        moves = []
        row = self.row
        col = self.col

        #up,down,left, right
        if row != 0 and (board[row - 1][col].piece == None or board[row - 1][col].piece.color != self.color):
            moves.append([row - 1, col])
        if row != 7 and (board[row + 1][col].piece == None or board[row + 1][col].piece.color != self.color):
            moves.append([row + 1, col])
        if col != 0 and (board[row][col - 1].piece == None or board[row ][col - 1].piece.color != self.color):
            moves.append([row , col - 1])
        if col != 7 and (board[row][col + 1].piece == None or board[row ][col + 1].piece.color != self.color):
            moves.append([row , col + 1])

        #diagonals
        if row != 0 and col != 7 and (board[row - 1][col + 1].piece == None or board[row - 1][col + 1].piece.color != self.color):
            moves.append([row - 1, col + 1])
        if row != 7 and col != 7 and (board[row + 1][col + 1].piece == None or board[row + 1][col + 1].piece.color != self.color):
            moves.append([row + 1, col + 1])
        if row != 0 and col != 0 and (board[row - 1][col - 1].piece == None or board[row - 1][col - 1].piece.color != self.color):
            moves.append([row - 1, col - 1])
        if row != 7 and col != 0 and (board[row + 1][col - 1].piece == None or board[row + 1][col - 1].piece.color != self.color):
            moves.append([row + 1, col - 1])

        return moves
    
    def is_checked(self, board):
        for row in range(ROWS):
            for col in range(COLS):
                tile = board[row][col]
                # if it is a enemy piece
                if tile.piece != None and tile.piece.color != self.color:
                    # check if enemy piece attacks king's row and col
                    attacked = tile.piece.move(board)
                    if [self.row, self.col] in attacked:
                        return True
        return False


    def legal_moves(self, board, moves):
        legal_moves = []
        for move in moves:
            # create a deep copy of the board and emulate the move
            copy_board = copy.deepcopy(board)
            copy_board[move[0]][move[1]].piece = copy_board[self.row][self.col].piece
            copy_board[self.row][self.col].piece = None
            copy_board[move[0]][move[1]].piece.row = move[0]
            copy_board[move[0]][move[1]].piece.col = move[1]
            # if after the emulated move, king is not checked, we can play that move
            if not copy_board[move[0]][move[1]].piece.is_checked(copy_board):
                legal_moves.append(move)

        legal_moves += self.castling(board)

        return legal_moves
    

    def castling(self, board):
        castle = []

        left, right = True, True
        # check if the king has moved before
        if self.castle and not self.is_checked(board):
            # Check if left rook has moved before
            if type(board[self.row][self.col - 4].piece).__name__ == "Rook" and board[self.row][self.col - 4].piece.castle:
                # Check if there are any pieces in between king and rook
                if board[self.row][self.col - 1].piece or board[self.row][self.col - 2].piece or board[self.row][self.col - 3].piece != None:
                    left = False
                else:
                    # Check if the square in between the king and desired location is attacked
                    for row in range(ROWS):
                        for col in range(COLS):
                            tile = board[row][col]
                            if tile.piece != None and tile.piece.color != self.color and type(tile.piece).__name__ != "King":
                                attacked = tile.piece.move(board)
                                if [self.row, self.col - 1] in attacked:
                                    left = False
                                    break
                if left:
                    castle.append([self.row, self.col - 2])
            # same thing as above but with right rook
            if type(board[self.row][self.col + 3].piece).__name__ == "Rook" and board[self.row][self.col + 3].piece.castle:
                if board[self.row][self.col + 1].piece or board[self.row][self.col + 2].piece != None:
                    right = False
                else:
                    for row in range(ROWS):
                        for col in range(COLS):
                            tile = board[row][col]
                            if tile.piece != None and tile.piece.color != self.color and type(tile.piece).__name__ != "King":
                                attacked = tile.piece.move(board)
                                if [self.row, self.col + 1] in attacked:
                                    right = False
                                    break
                if right:
                    castle.append([self.row, self.col + 2])
        return castle
