import pygame
pygame.init()
pygame.display.set_caption("Runner") 
screen = pygame.display.set_mode((1280, 800))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()

