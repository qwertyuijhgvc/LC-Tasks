import pygame
import random
import pygame
import math

pygame.init()

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 153,   0,   0)
BLUE    =   (0,   0, 255)
YELLOW = (255, 255, 0)
BROWN = (102, 51, 0)
LIGHT_BROWN = (153, 76, 0)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("I always hated the color blue")
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Classes
class Player(pygame.sprite.Sprite):
    def __init__(self, s_width, s_length):
        super().__init__()
        self.image = pygame.Surface([s_width,s_length])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 450
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= 2
        if keys[pygame.K_d] and self.rect.x < 680:
            self.rect.x += 2
#end Class
class Bullet(pygame.sprite.Sprite):
    def __init__(self ):
        super().__init__()
        self.image = pygame.Surface([4,10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y -= 3
class Enemy(pygame.sprite.Sprite):
    def __init__(self,s_x,s_y):
        super().__init__()
        self.image = pygame.Surface([10,10])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = s_x
        self.rect.y = s_y
    def update(self):
        self.rect.x

#Global Variables
all_sprites_list = pygame.sprite.Group()
player = Player(20, 20)
column = [75,150,225,300]
row = [120,240,360,480,600]
for i in range (4):
    for j in range (5):
        enemy = Enemy(row[j],column[i])
        all_sprites_list.add(enemy)
all_sprites_list.add(player)
keys = pygame.key.get_pressed()
reload_time = 0
#Define writing on screen 
text_font = pygame.font.SysFont("Arial", 10)
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img,(x,y))
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
    # --- Game logic should go here
    if reload_time < 0:
        loaded = "Loaded"
    else:
        loaded = "Reloading"
    all_sprites_list.update()
    reload_time -= 1
    if event.type == pygame.MOUSEBUTTONDOWN and reload_time <= 0:
            # Fire a bullet if the user clicks the mouse button
            bullet = Bullet()
            # Set the bullet so it is where the player is
            bullet.rect.x = player.rect.x + 10 
            bullet.rect.y = player.rect.y
            # Add the bullet to the lists
            all_sprites_list.add(bullet)
            reload_time = 30
    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)

    #Draw here
    all_sprites_list.draw(screen)
    draw_text(loaded, text_font, WHITE, 25, 475)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    # --- Limit to 60 frames per second
    clock.tick(60)
 #end while

pygame.quit()