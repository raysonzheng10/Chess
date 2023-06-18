import pygame
from sys import exit
from helper.constants import WIDTH, HEIGHT

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')
clock = pygame.time.Clock()

green_surface = pygame.Surface((100,100))
green_surface.fill((127, 166, 80))

white_surface = pygame.Surface((100,100))
white_surface.fill((238, 238, 210))

pawn_surface = pygame.image.load('white_pawn.png')
pawn_surface = pygame.transform.scale(pawn_surface, (100,100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 1:
                screen.blit(green_surface, (100 * i, 100 * j))
            else:
                screen.blit(white_surface, (100 * i, 100 * j))
    screen.blit(pawn_surface, (100,100))
    pygame.display.update()
    clock.tick(60)