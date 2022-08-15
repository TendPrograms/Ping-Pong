from pygame import *
window = display.set_mode((800, 500))
display.set_caption('Пинг-Понг')
window.fill((30, 255, 150))
font.init()
font = font.SysFont('Arial', 50)
time = time.Clock()
dy = 3
dx = 3
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
        window.blit(self.image, self.rect.x, self.rect.y)

class Player(GameSprite):
    def update1(self):
        up, down, left, right = False, False, False, False
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y < 10:
            up = True
        if key_pressed[K_DOWN] and self.rect.y > 470:
            down = True
        if key_pressed[K_LEFT] and self.rect.x < 430:
            left = True
        if key_pressed[K_RIGHT] and self.rect.x > 770:
            right = True
        if up:
            self.rect.y -= self.speed
        if down:
            self.rect.y += self.speed
        if left:
            self.rect.x -= self.speed
        if right:
            self.rect.x += self.speed
    def update2(self):
        up, down, left, right = False, False, False, False
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y < 10:
            up = True
        if key_pressed[K_s] and self.rect.y > 470:
            down = True
        if key_pressed[K_a] and self.rect.x < 10:
            left = True
        if key_pressed[K_d] and self.rect.x > 370:
            right = True
        if up:
            self.rect.y -= self.speed
        if down:
            self.rect.y += self.speed
        if left:
            self.rect.x -= self.speed
        if right:
            self.rect.x += self.speed
    
class Ball(GameSprite):
    def update(self):
        global dy
        global dx

player1 = Player('ping_pong1.png', 5, 250, 100,100, 5)
player2 = Player('ping_pong2.png', 760, 250, 100, 100,5)

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if not finish:
        player1.update2()
        player2.update1()
    
    display.update()
    time.tick(60)