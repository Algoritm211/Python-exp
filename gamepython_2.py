import pygame
import random
from os import path
#Нахождение картинок с графикой
img_dir = path.join(path.dirname('/Users/alexfrost/Desktop/'),'Python projects/')
#Характеристики окна
WIDTH = 480
HEIGHT = 600
FPS = 60

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

'''Игра и окно'''
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()
'''подсчет очков'''
score = 0

font_score = pygame.font.match_font('Arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_score, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


'''классы объектов'''
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(ship_img, (50, 40))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,30))
        self.image = meteor_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -50)
        self.speedy = random.randrange(1, 6)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -50)
            self.speedy = random.randrange(1, 6)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((16, 16))
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        #Убивается если заходит за верхнюю часть экрана
        if self.rect.bottom < 0:
            self.kill()

'''игровая графика'''
background = pygame.image.load(path.join(img_dir, 'starfield.png')).convert()
background_rect = background.get_rect()
ship_img = pygame.image.load(path.join(img_dir, 'spacecraft.png')).convert()
meteor_img = pygame.image.load(path.join(img_dir, 'meteorite.png')).convert()
bullet_img = pygame.image.load(path.join(img_dir, 'bullet.png')).convert()


'''спрайты'''
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
ship = Ship()
all_sprites.add(ship)
for i in range(9):
    mob = Mob()
    all_sprites.add(mob)
    mobs.add(mob)



# Цикл игры
done = True
while done:
    # Обновление окна
    clock.tick(FPS)
    # События
    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ship.shoot()

    # Обновление персонажей
    all_sprites.update()
    #Попала ли пуля в метеорит
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        score += 1
        mob = Mob()
        all_sprites.add(mob)
        mobs.add(mob)

    hits = pygame.sprite.spritecollide(ship, mobs, False)
    if hits:
        done = False




    # Отображение

    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 50, WIDTH / 2, 15)
    # Удержание окна
    pygame.display.flip()

pygame.quit()
