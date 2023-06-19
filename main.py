#IMPORT IMPORTANT FILES
import pygame
from sys import exit
from helper.constants import WIDTH, HEIGHT, GRAY, LIGHT_GREEN
from helper.board import Board


#INITIALIZING SCREEN
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')
icon = pygame.image.load('pieces/white_knight.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()


#CREATE BOARD
board = Board()

# Function that puts the pos of mouse click into board.selected_tile
def retrieve_mouse_pos(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        # Gets the row and col positions from the click
        mouse_pos = pygame.mouse.get_pos()
        row = mouse_pos[1] // 100
        col = mouse_pos[0] // 100
        board.selected_tile = [row, col]

# Function that handles exiting the game
def game_quit(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()

    
def main():
    while True:
        # Main loop, listening to different events/inputs
        for event in pygame.event.get():
            # Puts the pos of mouse click into board.selected_tile
            retrieve_mouse_pos(event)

            # Quit functionality
            game_quit(event)
            
        
        board.draw_tiles(screen)
        board.update_pieces(screen)

        pygame.display.update()
        clock.tick(60)


main()