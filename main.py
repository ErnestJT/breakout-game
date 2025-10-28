import time
from game_components import Ball, Game, Paddle, Scoreboard
from block_handler import BlockManager

def play_breakout():
    game = Game()
    
    paddle = Paddle()
    ball = Ball()
    block_manager = BlockManager()
    scoreboard = Scoreboard()

    game.screen.listen()
    game.screen.onkeypress(paddle.go_right,'Right')
    game.screen.onkeypress(paddle.go_left, 'Left')

    while True:
        game.screen.update()
        time.sleep(ball.move_speed)
        ball.move()

        if not game.lives:
            game.game_over()
            scoreboard.update_high_score()
            break
        
        if ball.ycor() < -280:
            paddle.go_home()
            ball.reset_ball()
            game.lives -= 1
            game.write_lives()

        if ball.ycor() > 280:
            ball.bounce_y()

        if ball.xcor() > 280 or ball.xcor() < -280:
            ball.bounce_wall()

        if ball.distance(paddle) < 50 and ball.ycor() < -230:
            ball.sety(-220)
            ball.bounce_y()

        if not block_manager.blocks:
            block_manager.create_blocks()
        
        for block in block_manager.blocks:
            if block_manager.detect_collision(block, ball):
                scoreboard.update_score(block)
                ball.bounce_y()

                ball.speed_up(block.block_color)
                block.hideturtle()
                block_manager.blocks.remove(block)
                del block
    game.screen.mainloop()

if __name__ == '__main__':
    play_breakout()