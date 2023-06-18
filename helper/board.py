import pygame
from helper.constants import GRAY, LIGHT_GREEN, ROWS, COLS
from pieces.pieces import white_pawn, black_pawn

class Board:
    def __init__(self):
        # generate the tiles that make up the board
        self.board = []
        self.selected_piece = None

        self.create_board()
    
    # function to draw the board, input takes in the screen 
    def draw_tiles(self, screen):
        # iterate through the board and draw the tiles
        
        # Define surfaces to later output onto screen 
        gray_surface = pygame.Surface((100,100))
        gray_surface.fill(GRAY)
        green_surface = pygame.Surface((100,100))
        green_surface.fill(LIGHT_GREEN)

        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 1:
                    screen.blit(green_surface, (100 * i, 100 * j))
                else:
                    screen.blit(gray_surface, (100 * i, 100 * j))
                    
          
    def create_board(self):
        for row in range(ROWS):
            holder = []
            for col in range(COLS):
                holder.append(0)
            self.board.append(holder)
        # Adding white pawns
        for row in range(6, 8):
            for col in range(COLS):
                self.board[row][col] = "P"
        # Adding black pawns
        for row in range(0, 2):
            for col in range(COLS):
                self.board[row][col] = "p"
    def update_pieces(self, screen):
        #iterate through the matrix and update the screen
        for row in range(ROWS):
            for col in range(COLS):
                input = self.board[row][col]
                match input:
                    case "P": #white pawns
                        screen.blit(white_pawn, (100 * col, 100 * row))
                    case "p": #black pawns
                        screen.blit(black_pawn, (100 * col, 100 * row))



class Tile:
    def __init__(self, row, col):
        # piece and history determine previous and current pieces on the tile
        self.piece = None
        self.history = []

        # x and y determine the position of the tile
        self.row = row
        self.col = col

        # color determined by the x and y pos of the tile
        self.color = None