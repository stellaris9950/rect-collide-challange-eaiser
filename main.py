
# Import External Librarys
import pygame
import json
import random


# Create walls,only run once
class Wall:
    def __init__(self, x, y, length, width):
        self.length = length
        self.width = width
        self.x = x
        self.y = y
        self.collision_x = x + length
        self.collision_y = y + width


# item = Wall(30, 300, 500, 50)
# print(type(item))

def boarderCreate(screen_width, screen_height):
    boarders = []


    boarder = vars(Wall(0, 0, 10, screen_height))
    boarders.append(boarder)
    boarder = vars(Wall(0, 0, screen_width, 10))
    boarders.append(boarder)
    boarder = vars(Wall(screen_width-10, 0, 10, screen_height))
    boarders.append(boarder)
    boarder = vars(Wall(0, screen_height-10, screen_width, 10))
    boarders.append(boarder)


    print(boarders)

    with open('walls.json', 'w') as boarder_list:
        json.dump(boarders, boarder_list)

# boarderCreate(720,540)

def createWalls():
    wall_storage = []

    for i in range(3):
        walls_x = random.randrange(400, 600)
        walls_y = random.randrange(0, 100)
        walls = vars(Wall(walls_x, walls_y, 20, 300))
        wall_storage.append(walls)
        print("mark1")

    print(wall_storage)

    with open('walls.json', 'w') as walls_list:
        json.dump(wall_storage, walls_list)

# createWalls()

# Load walls from Json file
with open("walls.json", "r") as wall_data_output:
    walls_list = json.load(wall_data_output)


# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 540))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)



# drawing the walls
def drawWalls(walls_list):
    for walls in walls_list:
        pygame.draw.rect(screen, "grey", [walls['x'], walls['y'], walls['length'], walls['width']])

def collisionDetect(player, wall):
    return wall['collision_x'] >= player.x >= wall['x']-30 and wall['y']-30 <= player.y <= wall['collision_y']


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Game Logic

    player_movement = 300 * dt

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= player_movement
    if keys[pygame.K_s]:
        player_pos.y += player_movement
    if keys[pygame.K_a]:
        player_pos.x -= player_movement
    if keys[pygame.K_d]:
        player_pos.x += player_movement

    # collision detection
    for wall in walls_list:
        # Eaiser one
        """
        if collisionDetect(player_pos, wall):
            player_pos.x = 0
            player_pos.y = 0
        """
        if collisionDetect(player_pos, wall):
            player_pos = pygame.Vector2(50, 300)



    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    pygame.draw.rect(screen, "black", [player_pos.x, player_pos.y, 30, 30])

    drawWalls(walls_list)

    print(player_pos.x, player_pos.y)


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()



