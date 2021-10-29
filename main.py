import pygame

from food import *
from snake import *


class Background:
    def __init__(self, color):
        self.bg_color = color

def create_color():
        elements = random.sample(color_palette, 6)
        created_color = "".join(elements)
        return f"#{created_color}"

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

    if keys[pygame.K_f]:
        pygame.display.toggle_fullscreen()

    if keys[pygame.K_d]:
        snake.color = create_color()
        apple.color = create_color()
        background.bg_color = create_color()

pygame.init()

borders = (800, 600)
block_size = 20
color_palette = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

root = pygame.display.set_mode(borders)
pygame.display.set_caption("Snake Game")

snake = Snake(block_size, borders, "#EAD8D4")
apple = Food(block_size, borders, "#F35736")
background = Background("black")


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

    root.fill(background.bg_color)
    show_stats()
    
    check_keys()
    snake.move()

    snake.eat_food(apple)

    snake.draw(pygame, root)
    apple.draw(pygame, root)

    pygame.display.update()
