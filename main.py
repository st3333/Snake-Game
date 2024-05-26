import pygame as pg
import time
import random

speed = 15

# Window size
win_x = 720
win_y = 480

# Colors
black = pg.Color(0, 0, 0)
white = pg.Color(255, 255, 255)
red = pg.Color(255, 0, 0)
green = pg.Color(0, 255, 0)
blue = pg.Color(0, 0, 255)

pg.init()

# Window
pg.display.set_caption("Snake")
window = pg.display.set_mode((win_x, win_y))

# FPS
fps = pg.time.Clock()

snake_pos = [100, 50]

snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

# Apple
apple_pos = [random.randrange(1, (win_x // 10)) * 10,
             random.randrange(1, (win_y // 10)) * 10]

apple = True

direction = 'RIGHT'
change_to = direction

score = 0

def show_score(choice, color, font, size):

    score_font = pg.font.SysFont(font, size)

    score_show = score_font.render(f'Score: {str(score)}', True, color)
    score_rect = score_show.get_rect()

    # displaying Text
    window.blit(score_show, score_rect)

def game_over():
    font = pg.font.SysFont('Sans', 50)

    game_over_show = font.render(f"Your Score is: {str(score)}", True, red)

    game_over_rect = game_over_show.get_rect()

    # Set position text
    game_over_rect.midtop = (win_x / 2, win_y / 4)

    window.blit(game_over_show, game_over_rect)
    pg.display.flip()

    time.sleep(2)
    pg.quit()
    quit()

while True:

    for ev in pg.event.get():
        if ev.type == pg.KEYDOWN:
            if ev.key == pg.K_UP:
                change_to = 'UP'
            if ev.key == pg.K_DOWN:
                change_to = 'DOWN'
            if ev.key == pg.K_LEFT:
                change_to = 'LEFT'
            if ev.key == pg.K_RIGHT:
                change_to = 'RIGHT'

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP' 
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN' 
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT' 
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT' 
    
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake Body
    snake_body.insert(0, list(snake_pos))

    if snake_pos[0] == apple_pos[0] and snake_pos[1] == apple_pos[1]:
        score += 1
        apple = False
    else:
        snake_body.pop()

    if not apple:
        apple_pos = [random.randrange(1, (win_x // 10)) * 10,
                     random.randrange(1, (win_y // 10)) * 10]
        
    apple = True
    window.fill(black)

    for pos in snake_body:
        pg.draw.rect(window, green,
                     pg.Rect(pos[0], pos[1], 10, 10))
    pg.draw.rect(window, red, pg.Rect(
        apple_pos[0], apple_pos[1], 10, 10))
    
    if snake_pos[0] < 0 or snake_pos[0] > win_x - 10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > win_y - 10:
        game_over()

    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()
    show_score(1, white, 'Sono', 40)

    pg.display.update()
    fps.tick(speed)