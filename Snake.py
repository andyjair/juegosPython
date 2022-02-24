import pygame
from pygame.math import Vector2
import random


pygame.init()

ALTO = 480
ANCHO = 720

WIN = pygame.display.set_mode((ANCHO,ALTO))
SCORE_TEXT = pygame.font.SysFont("Russo One",40)

class Snake:
    def __init__(self):
        self.body = [Vector2(20,100),Vector2(20,110),Vector2(20,120)]
        self.direction = Vector2(0,20)
        self.add = False

    def draw(self):
        for bloque in self.body:
            pygame.draw.rect(WIN,(255,255,255),(bloque.x,bloque.y,20,20))

    def move(self):
        if self.add == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body = body_copy[:]   
            self.add = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body = body_copy[:]    

    def move_up(self):  
        self.direction = Vector2(0,-20) 

    def move_down(self):  
        self.direction = Vector2(0,20)

    def move_right(self):  
        self.direction = Vector2(20,0)

    def move_left(self):  
        self.direction = Vector2(-20,0)  

    def die(self):      
        if self.body[0].x >= ANCHO+20 or self.body[0].y >= ALTO+20 or self.body[0].x <= -20 or self.body[0].y <= -20:
            return True  

        for i in self.body[1:]:
            if self.body[0] ==i:
                return True   

class Apple:
    def __init__(self):
        self.generate()

    def draw(self):
        pygame.draw.rect(WIN,(255,255,255),(self.pos.x,self.pos.y,20,20))    

    def generate(self):
        self.x = random.randrange(0,ANCHO/20)
        self.y = random.randrange(0,ALTO/20)
        self.pos = Vector2(self.x*20,self.y*20) 

    def check_collision(self,snake):
        if snake.body[0] == self.pos:
            self.generate()
            snake.add = True
            return True
        for bloque in snake.body[1:]:
            if self.pos == bloque:
                self.generate()    
        return False


def main():
    snake = Snake()
    apple = Apple()
    score = 0
    fps = pygame.time.Clock()

    while True:

        fps.tick(15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN and snake.direction.y != 20:
                if event.key == pygame.K_UP:
                    snake.move_up()    

            if event.type == pygame.KEYDOWN and snake.direction.y != -20:
                if event.key == pygame.K_DOWN:
                    snake.move_down()

            if event.type == pygame.KEYDOWN and snake.direction.x != -20:
                if event.key == pygame.K_RIGHT:
                    snake.move_right()

            if event.type == pygame.KEYDOWN and snake.direction.x != 20:
                if event.key == pygame.K_LEFT:
                    snake.move_left()                        

        WIN.fill((0,0,0))
        snake.draw()
        apple.draw()
        snake.move()

        if snake.die():
            quit()

        if apple.check_collision(snake):    
            score +=1

        text = SCORE_TEXT.render("Score: {}".format(score),1,(255,255,255))
        WIN.blit(text,(ANCHO-text.get_width()-20,20))

        pygame.display.update()      
main()
