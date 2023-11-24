# Import External Librarys
import pygame
import json
import random


# Create walls,only run once
class Wall:
    def __init__(self, length, width, x, y):
        self.length = length
        self.width = width
        self.x = x
        self.y = y
        self.collison_x = x + length
        self.collison_y = y + width


# item = Wall(30, 300, 500, 50)
# print(type(item))

def createWalls():
    wall_storage = []

    for i in range(3):
        walls_x = random.randrange(400, 600)
        walls_y = random.randrange(0, 100)
        walls = vars(Wall(20, 300, walls_x, walls_y))
        wall_storage.append(walls)
        print("mark1")

    print(wall_storage)

    with open('walls.json', 'w') as walls_list:
        json.dump(wall_storage, walls_list)


# createWalls()


#
#
#
# Load walls from Json file
with open("walls.json", "r") as wall_data_output:
    walls_list = json.load(wall_data_output)

print()

# drawing the walls


# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 540))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)




def drawWalls(walls_list):
    for walls in walls_list:
        pygame.draw.rect(screen, "grey", [walls['x'], walls['y'], walls['length'], walls['width']])
        pygame.display.flip()

def collisionDetect(player, wall):
     return (player.x > wall['x'] and player.x < wall['collison_x'] and player.y < wall['y'] and player.y < wall['collison_y'])



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    pygame.draw.rect(screen, "black", [player_pos.x, player_pos.y, 30, 30])

    drawWalls(walls_list)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt


    # collision detection

    for wall in walls_list:
        print(collisionDetect(player_pos, wall))
        if collisionDetect(player_pos, wall):
            player_pos.x = 0
            player_pos.y = 0

    print(player_pos.x, player_pos.y)


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

