from enum import Enum

class Directions(Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4


class Snake:
    def __init__(self, block_size, border):
        self.block_size = block_size
        self.border = border
        self.color = "#DACDCB"
        self.score = 0

        self.respawn()

    def respawn(self):
        self.length = 3
        self.body = [(20, 20), (40, 20), (60, 20)]
        self.direction = Directions.RIGHT
    
    def draw(self, game, root):
        for block in self.body:
            game.draw.rect(root, self.color, (block[0], block[1], self.block_size, self.block_size))

    def move(self):
        head = self.body[-1]
        if self.direction == Directions.DOWN :
            next_block = (head[0], head[1] + self.block_size)
            self.body.append(next_block)

        if self.direction == Directions.UP :
            next_block = (head[0], head[1] - self.block_size)
            self.body.append(next_block)

        if self.direction == Directions.LEFT :
            next_block = (head[0] - self.block_size, head[1])
            self.body.append(next_block)

        if self.direction == Directions.RIGHT:
            next_block = (head[0] + self.block_size, head[1])
            self.body.append(next_block)
        
        if self.length < len(self.body):
            self.body.pop(0)

    def control(self, direction):
        if self.direction == Directions.UP:
            self.direction = direction

        if self.direction == Directions.DOWN:
            self.direction = direction

        if self.direction == Directions.LEFT:
            self.direction = direction

        if self.direction == Directions.RIGHT:
            self.direction = direction

    def grow_up(self):
        self.length += 1
        self.score += 10

    def eat_food(self, food):
        head = self.body[-1]
        if head[0] == food.x and head[1] == food.y:
            self.grow_up()
            food.respawn()