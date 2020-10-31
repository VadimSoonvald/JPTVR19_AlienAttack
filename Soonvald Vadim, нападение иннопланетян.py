import pygame
import random
import time
pygame.init()

class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((0, 0, 0))
    
    def set_position(self, xpos, ypos):
        self.x = xpos
        self.y = ypos
    
    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))

def Intersect(x1,y1,x2,y2):
    if(x1 > x2-32) and (x1 < x2+32) and (y1 > y2-32) and (y1 < y2+32):
        return True


screen = pygame.display.set_mode((640,480))
pygame.key.set_repeat(1, 1)

pygame.display.set_caption('Invaders')

backdrop = pygame.image.load('backdrop.bmp') 
screen.blit(backdrop, (0, 0))
enemies = []
missiles = []

x = 0
count = 0

for count in range(10): 
    enemies.append(Sprite(50 * x + 50, 50, 'baddie.bmp'))
    x += 1

hero = Sprite(20, 400, 'hero.bmp')
ourmissile = Sprite(0, 480, 'heromissile.bmp')
enemymissile = Sprite(0, 480, 'baddiemissile.bmp')

run = True
enemyspeed = 4
timer = 0        
clock = pygame.time.Clock()

while run:
    
    heromid = hero.x + 16
    screen.blit(backdrop, (0, 0))

    for count in range(len(enemies)):
        enemies[count].x += enemyspeed
        enemies[count].render()

    if enemies[len(enemies) - 1].x > 590:
        enemyspeed = -3
        for count in range(len(enemies)):
            enemies[count].y += 5

    if enemies[0].x < 10:
        enemyspeed = 3
        for count in range(len(enemies)):
            enemies[count].y += 5

    if ourmissile.y < 480 and ourmissile.y > 0:
        ourmissile.render()
        ourmissile.y += -5

    if enemymissile.y >= 480 and len(enemies) > 0:
        enemymissile.x = enemies[random.randint(0, len(enemies) - 1)].x
        enemymissile.y = enemies[0].y

    if Intersect(hero.x, hero.y, enemymissile.x, enemymissile.y):
        run = False

    for count in range(0, len(enemies)):
        if Intersect(ourmissile.x, ourmissile.y, enemies[count].x, enemies[count].y):
            del enemies[count]
            break

    if len(enemies) == 0:
        run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and hero.x < 590:
                hero.x += 5
            if event.key == pygame.K_LEFT and hero.x > 10:
                hero.x -= 5
            if event.key == pygame.K_SPACE:
                if (ourmissile.x, ourmissile.y) == (0, 480) or ourmissile.y <= 0:
                    ourmissile.x = hero.x
                    ourmissile.y = hero.y

        enemymissile.render()
        enemymissile.y += 5

    hero.render()
    pygame.time.delay(7)
    pygame.display.update()

pygame.quit()           