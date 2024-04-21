import pygame
from datetime import datetime

#pygame bastaluy
pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Keanuz")
screen.fill((155, 206, 222))
ic = pygame.image.load('im/sam.png')
pygame.display.set_icon(ic)

clock = pygame.time.Clock()
#suret engizu

main = pygame.image.load("im/mickey.png")
minute = pygame.image.load("im/right.png")
second = pygame.image.load("im/left.png")

main = pygame.transform.scale(main, (800,800))
minute = pygame.transform.scale(minute, (500, 450))
second = pygame.transform.scale(second, (30,500))
#oryndalu process

q = True
while q:

    current_time = datetime.now()

    minute_angel = current_time.minute * 6.5 * -1.5
    second_angel =current_time.second * 6.5 * -1

    rotated_minute = pygame.transform.rotate(minute, minute_angel)
    rotated_second = pygame.transform.rotate(second, second_angel)

    screen.blit(main, main.get_rect(center=screen.get_rect().center))
    screen.blit(rotated_minute, rotated_minute.get_rect(center=screen.get_rect().center))
    screen.blit(rotated_second, rotated_second.get_rect(center=screen.get_rect().center))
    clock.tick(60)

    pygame.display.update()

    for zat in pygame.event.get():
        if zat.type == pygame.QUIT:
            pygame.quit()
            q = False


