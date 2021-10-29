import random


class Food:
    def __init__(self, block_size, border, color):
        self.block_size = block_size
        self.border = border

        self.color = color
        self.respawn()

    def respawn(self):
        blocks_inx = self.border[0] / self.block_size 
        blocks_iny = self.border[1] / self.block_size 

        self.x = random.randint(0, blocks_inx - 1) * self.block_size
        self.y = random.randint(0, blocks_iny - 1) * self.block_size
    
    def draw(self, game, root):
        game.draw.rect(root, self.color, (self.x, self.y, self.block_size, self.block_size))
