import pygame
import random
import os
import time
pygame.mixer.init()
BALL_IMGS = [pygame.image.load(os.path.join("imgs", "ball1.png"))]
collideSound = pygame.mixer.Sound(os.path.join('sound','beep.wav'))

class Ball:
    r=20
    vx = 5
    angle = -0.0001
    def __init__(self, WIN):
        self.WIN = WIN
        self.x= WIN.get_width()/2 - self.r
        self.y= WIN.get_height()/2 - self.r
        self.vy = random.randint(-4,5)
        self.img = pygame.transform.scale(BALL_IMGS[0],(2*self.r, 2*self.r))
        ran=random.randint(1,2)
        if ran==1: self.vx = - self.vx

        ran = random.randint(1, 9)
        if ran <= 4:
            self.vy = ran 
        else: self.vy = ran - 9
    


    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.y <= 0:
            self.vy = abs(self.vy)
            print("wall top")
        if self.y + 2*self.r >= 720:
            self.y =680
            self.vy = - abs(self.vy)
            print("Wall bottom")

    def draw(self,WIN):        
        WIN.blit(self.img,(self.x,self.y))

    def collide(self, paddle):
        left = 35
        right = 1205
        # Left: 35
        # Right: 1205
        if paddle.y+100 > self.y >= paddle.y:
            if paddle.player == 1 and self.x == left:
                # left
                self.vx = -self.vx
                
                ran = random.randint(1, 9)
                if ran <= 4:
                    self.vy = ran 
                else: self.vy = ran - 9
                collideSound.play()

            if paddle.player == 2 and self.x == right:
                # right
                self.vx = -self.vx

                ran = random.randint(1, 9)
                if ran <= 4:
                    self.vy = ran 
                else: self.vy = ran - 9
                collideSound.play()
    def lose(self):
        if self.x <=0 or self.x >= self.WIN.get_width() - self.r*2:
            print("Oops")

            if self.x <= 0:
                self.vx = abs(self.vx)
                return 1
            elif self.x >= self.WIN.get_width() - self.r*2:
                self.vx = -abs(self.vx)
                return 2
            else:
                return 3