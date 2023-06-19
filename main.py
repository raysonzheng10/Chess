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


def main():
    while True:
        # Main loop, listening to different events/inputs
        for event in pygame.event.get():
            # User clicks on the board
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Gets the row and col positions from the click
                mouse_pos = pygame.mouse.get_pos()
                row = mouse_pos[1] // 100
                col = mouse_pos[0] // 100
                board.selected_tile = [row, col]

                print(board.selected_tile)
                # Check and see what was clicked on
                
            # Quit functionality
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            #if event type == start game, run initlize
        
        if board.selected_tile == None:
            board.draw_tiles(screen)
        else: 
            board.update_selection(screen)
        board.update_pieces(screen)

        pygame.display.update()
        clock.tick(60)


main()