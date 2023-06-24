import pygame
from helper.constants import gray_surface, green_surface, whiteH_surface, blackH_surface, LIGHT_GREEN, GRAY, GREEN_MOVE, GRAY_MOVE, MOVE_CIRCLE_SIZE, ATTACK_CIRCLE_SIZE, INSIDE_CIRCLE, ROWS, COLS
from pieces.pieces import white_pawn, white_bishop, white_king, white_knight, white_queen, white_rook, black_pawn, black_bishop, black_king, black_knight,black_queen, black_rook
from helper.movement import Pawn, Knight, Bishop, Rook, Queen, King

class Tile:
    def __init__(self, row, col, piece):
        self.piece = piece
        self.row = row
        self.col = col
        
        # if color == 0, white tile, if color == 1, black tile
        self.color = (row + col) % 2

        # true means put movement circle, else no movement circle
        self.movable = False
        self.attacked = False


    
    # Function to get the movement circle/attack to pop up
    def draw_move(self, screen):
        if self.attacked == True:
            if self.color == 0:
                pygame.draw.circle(screen, GRAY_MOVE, (100 * self.col + 50, 100 * self.row + 50), ATTACK_CIRCLE_SIZE)
                pygame.draw.circle(screen, GRAY, (100 * self.col + 50, 100 * self.row + 50), INSIDE_CIRCLE)
            else:
                pygame.draw.circle(screen, GREEN_MOVE, (100 * self.col + 50, 100 * self.row + 50), ATTACK_CIRCLE_SIZE)
                pygame.draw.circle(screen, LIGHT_GREEN, (100 * self.col + 50, 100 * self.row + 50), INSIDE_CIRCLE)
        elif self.movable == True:
            if self.color == 0:
                pygame.draw.circle(screen, GRAY_MOVE, (100 * self.col + 50, 100 * self.row + 50), MOVE_CIRCLE_SIZE)
            else:
                pygame.draw.circle(screen, GREEN_MOVE, (100 * self.col + 50, 100 * self.row + 50), MOVE_CIRCLE_SIZE)
        
        # reset the movable attribute when you click on something else
        self.movable = False
        self.attacked = False


class Board:
    def __init__(self):
        # .board is the matrix to index into
        self.board = []

        # represents the row/col of the selected tile if any
        self.select_col = None
        self.select_row = None


        self.create_board()
    
    # function to draw the board, input takes in the screen 
    def draw_all(self, screen):

        # iterate through the board and draw the tiles
        for row in range(ROWS):
            for col in range(COLS):
                tile = self.board[row][col]
        
                if tile.color == 1:
                    screen.blit(green_surface, (100 * col, 100 * row))

                else:
                    screen.blit(gray_surface, (100 * col, 100 * row))
                tile.draw_move(screen)

                

        # Check if a valid piece has been selected
        if (self.select_col  or self.select_row != None) and (self.board[self.select_row][self.select_col].piece) != None:
            if self.board[self.select_row][self.select_col].color == 1:
                screen.blit(blackH_surface, (100 * self.select_col, 100 * self.select_row))
            else:
                screen.blit(whiteH_surface, (100 * self.select_col, 100 * self.select_row))

        
        
        # put in all the piece surfaces
        for row in range(ROWS):
            for col in range(COLS):
                tile = self.board[row][col]
                input = type(tile.piece).__name__
                match input:
                    case "Pawn": #white pawns
                        if tile.piece.color == "w":
                            screen.blit(white_pawn, (100 * col, 100 * row))
                        else:
                            screen.blit(black_pawn, (100 * col, 100 * row))
                    case "Bishop":
                        if tile.piece.color == "w":
                            screen.blit(white_bishop, (100 * col, 100 * row))
                        else:
                            screen.blit(black_bishop, (100 * col, 100 * row))
                    case "Knight":
                        if tile.piece.color == "w":
                            screen.blit(white_knight, (100 * col, 100 * row))
                        else:
                            screen.blit(black_knight, (100 * col, 100 * row))
                    case "Rook":
                        if tile.piece.color == "w":
                            screen.blit(white_rook, (100 * col, 100 * row))
                        else:
                            screen.blit(black_rook, (100 * col, 100 * row))
                    case "Queen":
                        if tile.piece.color == "w":
                            screen.blit(white_queen, (100 * col, 100 * row))
                        else:
                            screen.blit(black_queen, (100 * col, 100 * row))
                    case "King":
                        if tile.piece.color == "w":
                            screen.blit(white_king, (100 * col, 100 * row))
                        else:
                            screen.blit(black_king, (100 * col, 100 * row))

          
    def create_board(self):
        #Create 8x8 empty matrix
        for row in range(ROWS):
            holder = []
            for col in range(COLS):
                holder.append(Tile(row, col, None))
            self.board.append(holder)

        white_str = "PPPPPPPPRNBQKBNR"
        black_str = "rnbqkbnrpppppppp"
        # Adding white pieces
        for row in range(6, 8):
            for col in range(COLS):
                input = white_str[(col) + (row - 6) * 8]
                match input:
                    case "P":
                        self.board[row][col].piece = Pawn(row, col, "w")
                    case "N": 
                        self.board[row][col].piece = Knight(row, col, "w")
                    case "B":
                        self.board[row][col].piece = Bishop(row, col, "w")
                    case "R":
                        self.board[row][col].piece = Rook(row, col, "w")
                    case "Q":
                        self.board[row][col].piece = Queen(row, col, "w")
                    case "K":
                        self.board[row][col].piece = King(row, col, "w")


        # Adding black pawns
        for row in range(0, 2):
            for col in range(COLS):
                input = black_str[col + row * 8]
                match input:
                    case "p":
                        self.board[row][col].piece = Pawn(row, col, "b")
                    case "n": 
                        self.board[row][col].piece = Knight(row, col, "b")
                    case "b":
                        self.board[row][col].piece = Bishop(row, col, "b")
                    case "r":
                        self.board[row][col].piece = Rook(row, col, "b")
                    case "q":
                        self.board[row][col].piece = Queen(row, col, "b")
                    case "k":
                        self.board[row][col].piece = King(row, col, "b")
        #testing
        self.board[3][4].piece = Rook(3, 4, "w")
        # self.board[2][4].piece = Pawn(2, 4, "w")



    def update_movement(self):
        possible_moves = []
        if (self.select_col or self.select_row != None):
            x = self.select_col
            y = self.select_row
            tile = self.board[y][x]


            #change this to a case match thing
            if type(tile.piece).__name__ == "Rook":
                possible_moves = tile.piece.move(self.board)

        for move in possible_moves:
            self.board[move[0]][move[1]].movable = True
            if self.board[move[0]][move[1]].piece != None:
                self.board[move[0]][move[1]].attacked = True
        
    

