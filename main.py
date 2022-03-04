import pygame
import json
from player import Hero
from enemy import Enemy

pygame.init()
screen = pygame.display.set_mode([800, 400])

font = pygame.font.SysFont('courier', 16)
display_map = font.render("", True, "#ffffff")

with open("map.json") as mapdata:
    maps = json.load(mapdata)


player = Hero("Your Mom")
current_map = maps["castle"]


def drawmap():
    map_data = []
    rowstring = ""
    for y, row in enumerate(current_map):
        for x, col in enumerate(current_map[row]):
            if player.x == x and player.y == y:
                rowstring = rowstring + "x"
            else:
                rowstring = rowstring + str(col)
        map_data.append(rowstring)
        rowstring = ""
    return map_data


# the main game loop
while True:
    screen.fill("#000000")
    # draw the map onto the screen
    for i, row in enumerate(drawmap()):
        display_map = font.render(row,True, "#ffffff")
        screen.blit(display_map, (0, i*16))
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.move(player.x, player.y-1)
            if event.key == pygame.K_a:
                player.move(player.x-1, player.y)
            if event.key == pygame.K_s:
                player.move(player.x, player.y+1)
            if event.key == pygame.K_d:
                player.move(player.x+1, player.y)
        if event.type == pygame.QUIT:
            pygame.quit()

    # updates the screen
    pygame.display.update()

