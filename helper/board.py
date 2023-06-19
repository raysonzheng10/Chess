import pygame
from helper.constants import gray_surface, green_surface, yellow_surface, ROWS, COLS
from pieces.pieces import white_pawn, white_bishop, white_king, white_knight, white_queen, white_rook, black_pawn, black_bishop, black_king, black_knight,black_queen, black_rook


class Tile:
    def __init__(self, row, col, piece):
        # piece tells what team and type of piece is on this tile
        self.piece = piece

        # x and y determine the position of the tile
        self.row = row
        self.col = col
    
class Board:
    def __init__(self):
        # generate the tiles that make up the board
        self.board = []
        self.selected_tile = None

        self.create_board()
    
    # function to draw the board, input takes in the screen 
    def draw_tiles(self, screen):
        # iterate through the board and draw the tiles
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 1:
                    screen.blit(green_surface, (100 * row, 100 * col))
                else:
                    screen.blit(gray_surface, (100 * row, 100 * col))
        if self.selected_tile != None:
            screen.blit(yellow_surface, (100 * self.selected_tile[1], 100 * self.selected_tile[0]))
                    
          
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
        
        
    def update_pieces(self, screen):
        #iterate through the matrix and update the screen
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
    
    

