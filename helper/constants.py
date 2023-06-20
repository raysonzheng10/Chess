# constant variables that will not be changed
import pygame

# Width and Height for the general window, Number of rows/columns, size of each tile
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
TILE_SIZE = WIDTH / COLS

MOVE_CIRCLE_SIZE = 17  #pixels 

#Colors
LIGHT_GREEN = (127, 166, 80) #chess.com green tiles
GRAY = (238, 238, 210) #chess.com gray tiles
GREEN_HIGHLIGHT = (187, 203, 43) #chess.com green highlight tile
GRAY_HIGHLIGHT = (247, 247, 105) #chess.comm gray highlight tile
GREEN_MOVE = (106, 135, 77) #chess.com movement circle green
GRAY_MOVE = (214, 214, 189) #chess.com movement circle gray

# Surfaces created from above colors
gray_surface = pygame.Surface((100,100))
gray_surface.fill(GRAY)
green_surface = pygame.Surface((100,100))
green_surface.fill(LIGHT_GREEN)

blackH_surface = pygame.Surface((100,100))
blackH_surface.fill(GREEN_HIGHLIGHT)
whiteH_surface = pygame.Surface((100,100))
whiteH_surface.fill(GRAY_HIGHLIGHT)

