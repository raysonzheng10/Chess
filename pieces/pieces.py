# Creating all piece surfaces
import pygame

# White pawn
pawn_surface = pygame.image.load('pieces/white_pawn.png')
pawn_surface = pygame.transform.scale(pawn_surface, (100,100))