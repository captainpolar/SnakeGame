import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 102)
red = (250, 0, 0)  # Other nice red color: 213, 50, 80
green = (152, 251, 152)
blue = (30, 144, 255)  # other nice combo: 50, 151, 213

dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

# Fonts
font_style = pygame.font.SysFont("roboto", 30)
score_font = pygame.font.SysFont("chango", 55)
level_font = pygame.font.SysFont("chango", 55)


def score(score):
    value = score_font.render("Score: " + str(score), True, blue)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])


def gameLoop():
    end_game = False
    close_game = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Snake_Length = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10) * 10
    foody = round(random.randrange(0, dis_width - snake_block) / 10) * 10

    while not end_game:

        while close_game:
            dis.fill(green)  # change color
            message("GAME OVER! Press SPACE to play again or ESC to quit.", red)
            score(Snake_Length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        end_game = True
                        close_game = False
                    if event.key == pygame.K_SPACE:
                        gameLoop()

            # for event in pygame.event.get():
                # if event.type == pygame.KEYDOWN:
                    # if event.key == pygame.K_2:
                        # end_game = True
                        # close_game = False
                    # if event.key == pygame.K_1:
                        # gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            close_game = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(green)  # change color maybe
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])  # change food color maybe
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Snake_Length:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                close_game = True

        our_snake(snake_block, snake_List)
        score(Snake_Length - 1)


        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10) * 10
            foody = round(random.randrange(0, dis_height - snake_block) / 10) * 10
            Snake_Length += 1

        clock.tick(snake_speed)

# Planning to add levels:
    # if level == 1 and score == 10:
        # level +=2
        # snake_speed = 20
    pygame.quit()
    quit()


gameLoop()
