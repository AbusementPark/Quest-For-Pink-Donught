import pygame
import sys

pygame.init()

w = pygame.display.set_mode((800,800))

pygame.display.set_caption("QFPD")

clock = pygame.time.Clock()

sprite = pygame.image.load("test.png")
leave = False

def drawSprite(x, y):
	w.blit(sprite, (x, y))

while not leave:
    drawSprite(0, 0)
    for event in pygame.event.get():
	    print(event)
	    if event.type == pygame.QUIT:
		    leave = True
    for i in range(800):
        w.fill((255,255,255))
        drawSprite(i, 0)
        pygame.display.update()
        clock.tick(60)
		
pygame.quit()
sys.exit()
