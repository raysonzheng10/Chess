# Creating all piece surfaces
import pygame

# White pawn
white_pawn = pygame.image.load('pieces/white_pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (100,100))

# Black pawn
black_pawn = pygame.image.load('pieces/black_pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (100,100))