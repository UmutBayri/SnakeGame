import pygame

from food import *
from snake import *

def check_keys():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        snake.control(Directions.UP)

    if keys[pygame.K_DOWN]:
        snake.control(Directions.DOWN)

    if keys[pygame.K_RIGHT]:
        snake.control(Directions.RIGHT)

    if keys[pygame.K_LEFT]:
        snake.control(Directions.LEFT)

pygame.init()

borders = (500, 500)
background = "#1E1918"
block_size = 20

root = pygame.display.set_mode(borders)
pygame.display.set_caption("Snake Game")

snake = Snake(block_size, borders)
apple = Food(block_size, borders)

clock = pygame.time.Clock()
font = pygame.font.SysFont("Times", 20)

def show_stats():
    FPS = clock.get_fps()
    text_fps = font.render(f"FPS : {int(FPS)}", True, "white")
    text_score = font.render(f"Score : {snake.score}", True, "white")
 
    root.blit(text_score, (20, 20))
    root.blit(text_fps, (borders[0] - (text_fps.get_size()[0] + 20), 20))

run = True
while run :
    clock.tick(18)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    root.fill(background)
    show_stats()
    
    check_keys()
    snake.move()

    snake.eat_food(apple)

    snake.draw(pygame, root)
    apple.draw(pygame, root)

    pygame.display.update()