# constant variables that will not be changed
import pygame
pygame.init()

# Width and Height for the general window, Number of rows/columns, size of each tile
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
TILE_SIZE = WIDTH / COLS

MOVE_CIRCLE_SIZE = 17  #pixels 
ATTACK_CIRCLE_SIZE = 46 #pixels
INSIDE_CIRCLE = 38 #pixels

#Colors
LIGHT_GREEN = (127, 166, 80) #chess.com green tiles
GRAY = (238, 238, 210) #chess.com gray tiles
GREEN_HIGHLIGHT = (187, 203, 43) #chess.com green highlight tile
GRAY_HIGHLIGHT = (247, 247, 105) #chess.comm gray highlight tile
GREEN_MOVE = (106, 135, 77) #chess.com movement circle green
GRAY_MOVE = (214, 214, 189) #chess.com movement circle gray
RED_CHECK = (234, 58, 48) #lichess red check


# Surfaces created from above colors
gray_surface = pygame.Surface((100,100))
gray_surface.fill(GRAY)
green_surface = pygame.Surface((100,100))
green_surface.fill(LIGHT_GREEN)

blackH_surface = pygame.Surface((100,100))
blackH_surface.fill(GREEN_HIGHLIGHT)
whiteH_surface = pygame.Surface((100,100))
whiteH_surface.fill(GRAY_HIGHLIGHT)



# Win screen text
text_font = pygame.font.SysFont("Times New Roman", 50, True)

white_win_text = text_font.render("White Wins!", True, "White", "black")
white_win_screen = white_win_text.get_rect()
white_win_screen.center = (WIDTH / 2, HEIGHT / 2)

black_win_text = text_font.render("Black Wins!", True, "Black", "White")
black_win_screen = black_win_text.get_rect()
black_win_screen.center = (WIDTH / 2, HEIGHT / 2)


# SFX
move_self_sfx = pygame.mixer.Sound('sfx/move-self.mp3')
capture_sfx = pygame.mixer.Sound('sfx/capture.mp3')
castle_sfx = pygame.mixer.Sound('sfx/castle.mp3')
