import pygame as pg
pg.init()


class GameSprite(pg.sprite.Sprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, size_x, size_y, speed):
        super().__init__()
        self.img = pg.transform.scale(pg.image.load(sprite_image), (size_x, size_y))
        self.rect = self.img.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
        self.speed = speed

    def draw(self):
        window.blit(self.img, (self.rect.x, self.rect.y))


class Rocket(GameSprite):
    def update1(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        elif keys[pg.K_s] and self.rect.y < 300:
            self.rect.y += self.speed

    def update2(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        elif keys[pg.K_DOWN] and self.rect.y < 300:
            self.rect.y += self.speed


class Ball(GameSprite):
    def update(self):
        self.rect.x += speed_x
        self.rect.y += speed_y


window = pg.display.set_mode((700, 500))
clock = pg.time.Clock()

speed_x = 5
speed_y = 5

ball = Ball("ball.png", 300, 200, 70, 70, 10)
player1 = Rocket("platform.png", 0, 20, 150, 200, 10)
player2 = Rocket("platform.png", 570, 20, 150, 200, 10)

game = True
while game:
    window.fill((200, 200, 255))
    player1.draw()
    player1.update1()
    player2.draw()
    player2.update2()
    ball.draw()
    ball.update()

    if ball.rect.y >= 500 - 70:
        speed_y *= -1
    elif ball.rect.y <= 0:
        speed_y *= -1

    if ball.rect.colliderect(player2.rect) or ball.rect.colliderect(player1.rect):
        speed_x *= -1

    for e in pg.event.get():
        if e.type == pg.QUIT:
            game = False

    pg.display.update()
    clock.tick(60)