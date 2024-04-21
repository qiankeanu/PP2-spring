import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Red ball")
icon = pygame.image.load("im/gg.png")
pygame.display.set_icon(icon)
x, y = 320, 240
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y-55>0: y -= 10
    if pressed[pygame.K_DOWN] and y+55<480: y += 10
    if pressed[pygame.K_LEFT] and x-55>0: x -= 10
    if pressed[pygame.K_RIGHT] and x+55<640: x += 10
    

    screen.fill((255, 255, 255))  # заполнить экран белым
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)  # рисую круг

    clock.tick(60)
    pygame.display.flip()  # флип