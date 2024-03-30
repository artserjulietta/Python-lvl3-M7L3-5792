import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set up display
width = 800
height = 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Snake block size and speed
block_size = 20
snake_speed = 20

# Fonts
font_style = pygame.font.SysFont(None, 50)

# Function to draw snake
def snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], block_size, block_size])

# Function to display message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [width / 6, height / 3])

# Function to move the snake
def move_snake(x_change, y_change, x, y):
    x += x_change * block_size
    y += y_change * block_size
    return x, y

# Function to check boundary collision
def check_boundary_collision(x, y, boundary_width, boundary_height):
    if x >= boundary_width or x < 0 or y >= boundary_height or y < 0:
        return True
    return False

# Function to check food collision
def check_food_collision(snake_head, food_pos):
    if snake_head == food_pos:
        return True
    return False

# Function to check game over
def check_game_over(x, y, boundary_width, boundary_height):
    if x >= boundary_width or x < 0 or y >= boundary_height or y < 0:
        return True
    return False

# Main game function
def gameLoop():
    game_over = False
    game_close = False

    # Initial position of snake
    x1 = width / 2
    y1 = height / 2

    # Initial change in position
    x1_change = 0
    y1_change = 0

    # Initial snake body
    snake_list = []
    length_of_snake = 1

    # Initial position of food
    foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    while not game_over:
        while game_close == True:
            display.fill(black)
            message("You lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            # Checking for events in game over screen
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Checking for events in game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -1
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 1
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -1
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = 1
                    x1_change = 0

        # Move the snake
        x1, y1 = move_snake(x1_change, y1_change, x1, y1)

        # Check if snake hits the boundaries
        if check_boundary_collision(x1, y1, width, height):
            game_close = True

        # Update position of snake
        display.fill(black)
        pygame.draw.rect(display, red, [foodx, foody, block_size, block_size])

        # Snake body mechanism
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if snake eats the food
        if check_food_collision(snake_head, (foodx, foody)):
            foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0
            length_of_snake += 1

        # Check if snake hits itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # Draw snake
        snake(block_size, snake_list)
        pygame.display.update()

        # Control game speed
        pygame.display.update()
        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    quit()

# Pytest tests
def test_snake_movement():
    assert move_snake(0, -1, 0, 0) == (0, -20)
    assert move_snake(1, 0, 0, 0) == (20, 0)
    assert move_snake(0, 1, 0, 0) == (0, 20)
    assert move_snake(-1, 0, 0, 0) == (-20, 0)

def test_boundary_collision():
    assert check_boundary_collision(800, 600, 810, 590) == True
    assert check_boundary_collision(800, 600, -10, 590) == True
    assert check_boundary_collision(800, 600, 790, 610) == True
    assert check_boundary_collision(800, 600, 790, -10) == True

def test_food_collision():
    assert check_food_collision((20, 20), (20, 20)) == True
    assert check_food_collision((20, 20), (40, 40)) == False

def test_game_over():
    assert check_game_over(0, 0, 800, 600) == False
    assert check_game_over(810, 590, 800, 600) == True
    assert check_game_over(-10, 590, 800, 600) == True
    assert check_game_over(790, 610, 800, 600) == True
    assert check_game_over(790, -10, 800, 600) == True

# Start the game loop
if __name__ == "__main__":
    gameLoop()
    input("www")
