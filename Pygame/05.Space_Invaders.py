import pygame
import random
import pygame
from pygame.locals import *
from pygame import mixer
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
DORITO_YELLOW = (250,133,19)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Dorito Invaders")
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
    #end constructor function
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= 2
        if keys[pygame.K_d] and self.rect.x < 680:
            self.rect.x += 2
    #end update
#end Class
class Bullet(pygame.sprite.Sprite):
    def __init__(self ):
        super().__init__()
        self.image = pygame.Surface([10,10])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
    #end contructor function
    def update(self):
        self.rect.y -= 3
        pygame.draw.polygon(screen,DORITO_YELLOW,[(self.rect.x,self.rect.y + 10), (self.rect.x + 10 ,self.rect.y + 10), (self.rect.x + 5,self.rect.y )])
    #end update
#end class
class Enemy(pygame.sprite.Sprite):
    def __init__(self,s_x,s_y):
        super().__init__()
        self.image = pygame.Surface([15,15])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = s_x
        self.rect.y = s_y
    #end contructor function
    def update(self):
        if enemy_move == 0:
            self.rect.x += (8 + increase_speed)
        elif enemy_move == 30:
            self.rect.x += ( 8 + increase_speed)
        elif enemy_move == 60:
            self.rect.y += (3 + increase_speed)
        elif enemy_move == 120:
            self.rect.x -= (8 + increase_speed)
        elif enemy_move == 150:
            self.rect.x -= (8 + increase_speed)
        elif enemy_move == 180:
            self.rect.y += (3 + increase_speed)
        #end if
        pygame.draw.polygon(screen,DORITO_YELLOW,[(self.rect.x,self.rect.y + 7.5 ), (self.rect.x +10 ,self.rect.y + 2 ), (self.rect.x + 12,self.rect.y + 13)])
    #end update
#end class
class Death_Wall(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.Surface([700,30])
            self.image.fill(BLACK)
            self.rect = self.image.get_rect()
        #end contructor function
#end class
class Star(pygame.sprite.Sprite):
    
    #Constructor Function
    def __init__(self, s_width, s_length):
        super().__init__()
        #Set star sprite image
        self.image = pygame.Surface([s_width,s_length])
        self.image.fill(WHITE)
        #set speed
        self.speed = 1
        #MAke star a rectangle
        self.rect = self.image.get_rect()
        #Set x y values
        self.rect.x = random.randrange(0,700)
        self.rect.y = random.randrange(0,400)
    # end of contruction function
    def update(self):
        #To make star spawn back at top of screen when it hits bottom
        if self.rect.y > 500 :
            self.rect.y = -50
            self.speed = 1
        else:
            #To make star move down
            self.rect.y = self.rect.y + self.speed

    #end update
#end class star
#initialize music
mixer.init()
pygame.mixer.music.load('Pygame/Earth.mp3')
pygame.mixer.music.play(-1)

#Global Variables
finish = False
time = 0
#Set group for star
star_group = pygame.sprite.Group()
#Determine amount of stars
number_of_stars = 10
#Adds stars to group
for i in range (number_of_stars):
    star = Star(2,2)
    star_group.add(star)
#List of all sprites used
all_sprites_list = pygame.sprite.Group()
# List of each enemy in the game
enemy_list = pygame.sprite.Group()
# List of each bullet
bullet_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()
player = Player(20, 20)
column = [75,150,225,300]
row = [120,240,360,480,600]
wall = Death_Wall()
wall.rect.x = 0
wall.rect.y = 475
all_sprites_list.add(wall)
wall_list.add(wall)
#Make enmies
def enemy_spawn():
    for i in range (4):
        for j in range (5):
            enemy = Enemy(row[j],column[i])
            all_sprites_list.add(enemy)
            enemy_list.add(enemy)
    #next j
#next i
#end enemy_spawn
all_sprites_list.add(player)
keys = pygame.key.get_pressed()
reload_time = 0
enemy_move = 0
lives = 100000000
score = 0
waves = 1
increase_speed = 2
#Define writing on screen 
intro_font = pygame.font.SysFont("Arial", 20)
text_font = pygame.font.SysFont("Arial", 10)
finish_font = pygame.font.SysFont("Arial", 100)
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img,(x,y))
enemy_spawn()
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
    # --- Game logic should go here
    time += 1
    star_group.update()
    #end if
    if reload_time <= 0:
        loaded = "Loaded"
    else:
        loaded = "Reloading"
    #end if
    enemy_move += 1
    if enemy_move > 240:
        enemy_move = 0
    #end if
    reload_time -= 1
    if event.type == pygame.MOUSEBUTTONDOWN and reload_time <= 0:
            # Fire a bullet if the user clicks the mouse button
            bullet = Bullet()
            # Set the bullet so it is where the player is
            bullet.rect.x = player.rect.x + 10 
            bullet.rect.y = player.rect.y
            # Add the bullet to the lists
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
            reload_time = 30
    #end if
    # Calculate mechanics for each bullet
    for bullet in bullet_list:
 
        # See if it hit an enemy
        enemy_hit_list = pygame.sprite.spritecollide(bullet, enemy_list, True)
 
        # For each block hit, remove the bullet and add to the score
        for enemy in enemy_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
        #next enemy
        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
        #end if
    #next bullet
    for enemy in enemy_list:
        enemy_wall_list = pygame.sprite.spritecollide(enemy, wall_list, True)
        for x in enemy_wall_list:
            enemy_list.remove(enemy)
            all_sprites_list.remove(enemy)
            score += 1
            lives -= 1
            wall = Death_Wall()
            wall.rect.x = 0
            wall.rect.y = 475
            all_sprites_list.add(wall)
            wall_list.add(wall)

    #next bullet
    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)

    #Draw here
    star_group.draw(screen)
    all_sprites_list.draw(screen)
    draw_text(loaded, text_font, WHITE, 25, 475)
    pygame.draw.polygon(screen,DORITO_YELLOW,[(player.rect.x + 4,player.rect.y + 10), (player.rect.x + 13 ,player.rect.y + 3), (player.rect.x + 15,player.rect.y + 13)])
    all_sprites_list.update()
    if score == 20:
        enemy_spawn()
        waves += 1
        increase_speed += 10
        score += 1
        pygame.time.wait(120)
    elif score == 41:
        enemy_spawn()
        waves += 1
        increase_speed += 10
        score += 1
        pygame.time.wait(120)
    elif score == 62:
        enemy_spawn()
        waves += 1
        increase_speed += 10
        score += 1
        pygame.time.wait(120)
    elif score == 83:
        enemy_spawn()
        waves += 1   
        increase_speed += 10
    #end if
    if finish == True:
        pygame.time.wait(1200)
        done = True
    if lives <= 0:
        draw_text("You Lose!", finish_font, WHITE, 150, 150)
        finish = True
    #end if
    if score >= 103:
        draw_text("You Win!", finish_font, WHITE, 150, 150)
        finish = True
    #end if
    if time < 240:
        draw_text("As the only survivor of Nacho Chees Doritos", intro_font, WHITE, 175, 200)
        draw_text("You must defeat all the Cool Ranch Doritos", intro_font, WHITE, 175, 250)
    #end if
    draw_text("Wave:"+str(waves), text_font, WHITE, 650, 475)
    draw_text("Score:"+str(score), text_font, WHITE, 25, 0)
    draw_text("Lives:"+str(lives), text_font, WHITE, 650, 0)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    # --- Limit to 60 frames per second
    clock.tick(60)
 #end while

pygame.quit()