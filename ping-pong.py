from pygame import *
from time import time as timer
window = display.set_mode((800, 500))
display.set_caption('Пинг-Понг')
window.fill((30, 255, 200))
font.init()
font1 = font.SysFont('Arial', 50)
font2 = font.SysFont('Arial', 30)
time = time.Clock()
dy = 3
dx = 3
point1 = 0
point2 = 0
wall1 = Surface((800, 10))
wall2 = Surface((10, 50))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__()
        self.width = player_width
        self.height = player_height
        self.image = transform.scale(image.load(player_image), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
    def blit(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        up, down = False, False
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 50:
            up = True
        if key_pressed[K_DOWN] and self.rect.y < 350:
            down = True
        if up:
            self.rect.y -= self.speed
        if down:
            self.rect.y += self.speed
    def update2(self):
        up, down = False, False
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 50:
            up = True
        if key_pressed[K_s] and self.rect.y < 350:
            down = True
        if up:
            self.rect.y -= self.speed
        if down:
            self.rect.y += self.speed
    
class Ball(GameSprite):
    def update(self):
        global point1
        global point2
        global dy
        global dx
        self.rect.x += dx
        self.rect.y += dy
        if self.rect.y < 50 or self.rect.y > 450:
            dy *= -1
        if self.rect.x < 0:
            dy *= -1
            dx *= -1
            self.rect.x = 370
            point2 += 1
        if self.rect.x > 800:
            dy *= -1
            dx *= -1
            self.rect.x = 370
            point1 += 1

player1 = Player('ping-pong.png', 100, 250, 50,150, 5)
player2 = Player('ping-pong.png', 620, 250, 50, 150,5)
ball = Ball('ball.png', 370, 250, 50, 50, 0)
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((30, 255, 200))
    if not finish:
        points1 = font2.render('Очки: ' + str(point1), True, (0,0,0))
        points2 = font2.render('Очки: ' + str(point2), True, (0,0,0))
        window.blit(wall1, (0, 40))
        window.blit(wall2, (400, 0))
        window.blit(points1, (20, 5))
        window.blit(points2, (650, 5))
        player1.blit()
        player1.update2()
        player2.blit()
        player2.update1()
        ball.blit()
        ball.update()
        if sprite.collide_rect(ball, player1.rect.right) or sprite.collide_rect(ball, player2.rect.left):
            dx *= -1
    if point1 >= 10:
        finish = True
        win = font1.render('Игрок 1 выиграл!', True, (0,0,0))
        window.blit(win, (210, 240))
    if point2 >= 10:
        finish = True
        win = font1.render('Игрок 2 выиграл!', True, (0,0,0))
        window.blit(win, (210, 240))
    display.update()
    time.tick(60)
