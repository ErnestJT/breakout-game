from turtle import Turtle
from game_components import Ball, BlockColor




class Block(Turtle):
    def __init__(self, color: BlockColor) -> None:
        super().__init__()
        
        self.shape('square')
        self.shapesize(2, 1)
        self.color(color)
        self.penup()
        self.setheading(270)
        
        self.block_color = color


class BlockManager:
    def __init__(self) -> None:
        super().__init__()
        self.blocks: list[Block] = []
        self.create_blocks()

    def create_blocks(self) -> None:
        block_y = 130
        for color in BlockColor:
            block_x = -255
            for _ in range(11):
                turtle = Block(color = color)
                turtle.goto(block_x, block_y)
                self.blocks.append(turtle)
                
                block_x += 50
            block_y += 30
    
    def detect_collision(self, block: Block, ball: Ball) -> bool:
        if block.distance(ball) < 30:
            return True
        return False
