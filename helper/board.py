import pygame
from helper.constants import gray_surface, green_surface, whiteH_surface, blackH_surface, GREEN_MOVE, GRAY_MOVE, MOVE_CIRCLE_SIZE, ROWS, COLS
from pieces.pieces import white_pawn, white_bishop, white_king, white_knight, white_queen, white_rook, black_pawn, black_bishop, black_king, black_knight,black_queen, black_rook


class Tile:
    def __init__(self, row, col, piece):
        self.piece = piece
        self.row = row
        self.col = col
        
        # if color == 0, white tile, if color == 1, black tile
        self.color = (row + col) % 2

        # true means put movement circle, else no movement circle
        self.movable = False
    
class Board:
    def __init__(self):
        # .board is the matrix to index into
        self.board = []

        # represents the row/col of the selected tile if any
        self.select_col = None
        self.select_row = None

        # represents if a actual piece is selected, true = yes, false = no


        self.create_board()
    
    # function to draw the board, input takes in the screen 
    def draw_all(self, screen):

        # iterate through the board and draw the tiles
        for row in range(ROWS):
            for col in range(COLS):
                tile = self.board[row][col]

                if tile.color == 1:
                    holder = green_surface
                    if tile.movable == True:
                        pygame.draw.circle(holder, GREEN_MOVE, (100 * col + 50, 100 * row - 50), MOVE_CIRCLE_SIZE)
                    screen.blit(holder, (100 * col, 100 * row))

                else:
                    holder = gray_surface
                    if tile.movable == True:
                        pygame.draw.circle(holder, GRAY_MOVE, (100 * col + 50, 100 * row + 50), MOVE_CIRCLE_SIZE)
                    screen.blit(holder, (100 * col, 100 * row))
                

                    

        # Check if a valid piece has been selected
        if (self.select_col  or self.select_row != None) and (self.board[self.select_row][self.select_col].piece) != None:
            if self.board[self.select_row][self.select_col].color == 1:
                screen.blit(blackH_surface, (100 * self.select_col, 100 * self.select_row))
            else:
                screen.blit(whiteH_surface, (100 * self.select_col, 100 * self.select_row))
        
        
        # put in all the piece surfaces
        for row in range(ROWS):
            for col in range(COLS):
                input = self.board[row][col].piece
                match input:
                    case "P": #white pawns
                        screen.blit(white_pawn, (100 * col, 100 * row))
                    case "p": #black pawns
                        screen.blit(black_pawn, (100 * col, 100 * row))
                    case "R": #white rooks
                        screen.blit(white_rook, (100 * col, 100 * row))
                    case "r": #black rooks
                        screen.blit(black_rook, (100 * col, 100 * row))
                    case "N": #white knights
                        screen.blit(white_knight, (100 * col, 100 * row))
                    case "n": #black knights
                        screen.blit(black_knight, (100 * col, 100 * row))
                    case "B": #white bishop
                        screen.blit(white_bishop, (100 * col, 100 * row))
                    case "b": #black bishop
                        screen.blit(black_bishop, (100 * col, 100 * row))
                    case "Q": #white queen
                        screen.blit(white_queen, (100 * col, 100 * row))
                    case "q": #black queen
                        screen.blit(black_queen, (100 * col, 100 * row))
                    case "K": #white king
                        screen.blit(white_king, (100 * col, 100 * row))
                    case "k": #black king
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
                self.board[row][col].piece = white_str[(col) + (row - 6) * 8]
        # Adding black pawns
        for row in range(0, 2):
            for col in range(COLS):
                self.board[row][col].piece = black_str[col + row * 8]
        


        
    

