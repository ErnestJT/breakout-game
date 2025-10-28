from turtle import Screen, Turtle
from enum import StrEnum

class BlockColor(StrEnum):
    GREEN = 'green'
    YELLOW = 'yellow'
    RED = 'red'
    BLUE = 'blue'

ALIGNMENT = 'CENTER'
STYLE = ('Comic Sans',20,'normal')
BLOCK_COLOR_SPEEDS = {
            BlockColor.GREEN: 1,
            BlockColor.YELLOW: 3,
            BlockColor.RED: 5,
            BlockColor.BLUE: 7
        }
BLOCK_VALUES = {
    BlockColor.GREEN: 20,
    BlockColor.YELLOW: 25,
    BlockColor.RED: 40,
    BlockColor.BLUE: 60
}

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.turtlesize(1,1)
        self.X_DIRECTION = -1
        self.Y_DIRECTION = -1
        self.move_speed = 0.07
    
    def move(self) -> None:
        x = self.xcor() + 10 * self.X_DIRECTION
        y = self.ycor() + 10 * self.Y_DIRECTION
        self.goto(x,y)

    def bounce_wall(self) -> None:
        self.X_DIRECTION *= -1

    def bounce_y(self) -> None:
        self.Y_DIRECTION *= -1

    def reset_ball(self) -> None:
        self.X_DIRECTION = 1
        self.Y_DIRECTION = 1
        self.move_speed = 0.07
        self.goto(0,0)

    def speed_up(self, color: BlockColor) -> None:
        self.move_speed -= 0.0001 * BLOCK_COLOR_SPEEDS[color]

class Game:
    def __init__(self) -> None:
        self.screen = Screen()
        self.screen.setup(600,600)
        self.screen.bgcolor('black')
        self.screen.tracer(0)
        self.screen.colormode(255)
        
        self.lives_text = Turtle()
        self.lives_text.goto(250,280)
        self.lives_text.color('white')
        self.lives_text.penup()
        self.lives_text.hideturtle()
        
        self.lives = 3
        self.write_lives()
    
    def write_lives(self):
        self.lives_text.clear()
        self.lives_text.write(f'Lives: {self.lives}', font = ('Comic Sans',10,'normal'), align=ALIGNMENT)
    
    def game_over(self):
        gameover_text = Turtle()
        gameover_text.color('white')
        gameover_text.penup()
        gameover_text.hideturtle()
        gameover_text.write(f'GAME OVER', font = ('Comic Sans', 50, 'normal'), align = ALIGNMENT)

class Paddle(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color('white')
        self.penup()
        self.shape('square')
        self.shapesize(0.5,5)
        self.go_home()

    def go_home(self) -> None:
        self.goto(0,-250)

    def go_right(self) -> None:
        if self.xcor() == -245:
            self.goto(self.xcor() + 5 , self.ycor())

        if self.xcor() < 223:
            new_x = self.xcor() + 20
            self.goto(new_x,self.ycor())

    def go_left(self) -> None:
        if self.xcor() > -220:
            new_x = self.xcor() - 20
            self.goto(new_x,self.ycor())
        else:
            self.goto(-245,self.ycor())


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.goto(0,260)
        self.color('white')
        self.score = 0
        with open('data.txt') as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()

        self.write_score()

    def write_score(self) -> None:
        self.clear()
        self.write(f'Score: {self.score}  High Score: {self.high_score}', align=ALIGNMENT, font=STYLE)

    def update_score(self, block) -> None:
        self.score += BLOCK_VALUES[block.block_color]
        self.write_score()

    def update_high_score(self) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode = 'w') as file:
                file.write(f'{self.high_score}')
        self.write_score()
