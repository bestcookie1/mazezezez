#создай игру "Лабиринт"!
import pygame
from PIL import Image
pygame.init()
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, width, height, speed):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load(filename), (width, height)
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def draw(self):
        window.blit(self. image, self.rect)

class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.right < W:
            self.rect.x += self.speed
            if pygame.sprite.spritecollide(self, walls, False):
                self.rect.x -= self.speed
        elif keys[pygame.K_LEFT]and self.rect.left > 0:
            self.rect.x -= self.speed
            if pygame.sprite.spritecollide(self, walls, False):
                self.rect.x += self.speed
        elif keys[pygame.K_UP]and self.rect.top < H:
            self.rect.y -= self.speed
            if pygame.sprite.spritecollide(self, walls, False):
                self.rect.y += self.speed
        elif keys[pygame.K_DOWN] and self.rect.bottom > 0:
            self.rect.y += self.speed
            if pygame.sprite.spritecollide(self, walls, False):
                self.rect.y -= self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update(self, x1, x2):
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

        if self.rect.x <= x1:
            self.direction = 'right'
        if self.rect.right >= x2:
            self.direction = 'left'

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        window.blit(self.image, self.rect)

player = Player('hero.png', 265, 420, 30, 70, 10)
bot = Enemy('cyborg.png', 200, 200, 80, 60, 2 )
win = pygame.transform.scale(
    pygame.image.load("C:/Users/anech/Downloads/win.webp"), (100, 100))
lose = pygame.transform.scale(
    pygame.image.load("C:/Users/anech/Downloads/lose.jpg"), (100, 100))

walls = pygame.sprite.Group()
walls.add(
    Wall(300, 300, 50,300, (0, 250, 0) ),
    Wall(300, 300, 300,50, (0, 250, 0) ),
    Wall(600, 150, 50, 200, (0, 250, 0) ),
    Wall(400, 150, 200, 50, (0, 250, 0) ),
    Wall(200, 150, 200, 50, (0, 250, 0) ),
    Wall(200, 300, 50,300, (0, 250, 0) ),
    Wall(0, 300, 200,50, (0, 250, 0) )
)

money = GameSprite('treasure.png', 550, 50, 100, 100, 500)
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('jungles.ogg')

pygame.mixer.music.play()

W, H = 700, 500
FPS = 120

back = pygame.transform.scale(
    pygame.image.load("C:/mmm/derevo2.jpeg"), (W, H))

window = pygame.display.set_mode((W,H))
pygame.display.set_caption('Лабиринт')

clock = pygame.time.Clock()

game = True
finish = False

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    if pygame.sprite.collide_rect(player, bot):
        finish = True
        window.blit(lose,(200,200))
    elif pygame.sprite.collide_rect(player, money):
        finish = True
        window.blit(win,(200,200))
        
    if not finish:
        player.update()
        bot.update(50,500)
        window.blit(back, (0,0))
        player.draw()
        bot.draw()
        money.draw()
        walls.draw(window)


    pygame.display.update()
    clock.tick(FPS)
