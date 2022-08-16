from pygame import *
from random import randint
window = display.set_mode((700, 500))
display.set_caption('Пинг-Понг')
window.fill((30, 255, 200))
font.init()
mixer.init()
font1 = font.SysFont('Arial', 50)
font2 = font.SysFont('Arial', 30)
kick = mixer.Sound('kick-ball.ogg')
win_sound = mixer.Sound('game-won.ogg')
time = time.Clock()
dy = randint(1,5)
dx = 6
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
        if self.rect.y > 460 or self.rect.y < 55:
            kick.play()
            dy *= -1
        if self.rect.x < 0:
            dy = 0
            dx *= -1
            self.rect.x = player1.rect.right + 10
            self.rect.y = player1.rect.centery
            kick.play()
            point2 += 1
        if self.rect.x > 640:
            dy = 0
            dx *= -1
            self.rect.x = player2.rect.x - 10
            self.rect.y = player2.rect.centery
            kick.play()
            point1 += 1

player1 = Player('ping-pong.png', -36, 250, 100,150, 5)
player2 = Player('ping-pong.png', 635, 250, 100, 150,5)
ball = Ball('ball.png', 370, 250, 50, 50, 0)
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((30, 255, 200))
    if not finish:
        collide1 = False
        collide2 = False
        points1 = font2.render('Очки: ' + str(point1), True, (0,0,0))
        points2 = font2.render('Очки: ' + str(point2), True, (0,0,0))
        window.blit(wall1, (0, 40))
        window.blit(wall2, (350, 0))
        window.blit(points1, (30, 5))
        window.blit(points2, (570, 5))
        player1.blit()
        player1.update2()
        player2.blit()
        player2.update1()
        ball.blit()
        ball.update()
        if ball.rect.bottom > player1.rect.top and ball.rect.top < player1.rect.bottom and ball.rect.right > player1.rect.left + 40 and ball.rect.left < player1.rect.right - 40:
            collide1 = True
        if ball.rect.bottom > player2.rect.top and ball.rect.top < player2.rect.bottom and ball.rect.right > player2.rect.left + 40 and ball.rect.left < player2.rect.right - 40:
            collide2 = True
        if collide1 or collide2:
            kick.play()
            if dy >= 1:
                dy = randint(1,5)
            if dy <= -1:
                dy = randint(-5,-1)
            if dy == 0:
                dy = randint(-5, 5)
            dx *= -1

    if point1 >= 10:
        finish = True
        win = font1.render('Игрок 1 выиграл!', True, (0,0,0))
        win_sound.play()
        window.blit(win, (180, 240))
    if point2 >= 10:
        finish = True
        win_sound.play()
        win = font1.render('Игрок 2 выиграл!', True, (0,0,0))
        window.blit(win, (180, 240))
    display.update()
    time.tick(60)
