import pygame

# Initialize pygame
pygame.init()

# Set up the game window
game_width = 800
game_height = 600
window = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption('Pong')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Paddle settings
paddle_width = 15
paddle_height = 100
paddle_speed = 5

# Ball settings
ball_size = 15
ball_speed_x = 5
ball_speed_y = 5

# Initialize paddles and ball
player1_y = (game_height // 2) - (paddle_height // 2)
player2_y = (game_height // 2) - (paddle_height // 2)
ball_x = game_width // 2
ball_y = game_height // 2

# Game loop
guardando = True
while guardando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            guardando = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= paddle_speed
    if keys[pygame.K_s] and player1_y < game_height - paddle_height:
        player1_y += paddle_speed
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= paddle_speed
    if keys[pygame.K_DOWN] and player2_y < game_height - paddle_height:
        player2_y += paddle_speed

    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with top and bottom
    if ball_y <= 0 or ball_y >= game_height - ball_size:
        ball_speed_y = -ball_speed_y

    # Ball collision with paddles
    if (ball_x <= paddle_width and player1_y <= ball_y <= player1_y + paddle_height) or (ball_x >= game_width - paddle_width - ball_size and player2_y <= ball_y <= player2_y + paddle_height):
        ball_speed_x = -ball_speed_x

    # Reset ball if it goes past paddle
    if ball_x < 0 or ball_x > game_width:
        ball_x = game_width // 2
        ball_y = game_height // 2

    # Clear screen
    window.fill(BLACK)

    # Draw paddles and ball
    pygame.draw.rect(window, WHITE, (0, player1_y, paddle_width, paddle_height))
    pygame.draw.rect(window, WHITE, (game_width - paddle_width, player2_y, paddle_width, paddle_height))
    pygame.draw.ellipse(window, WHITE, (ball_x, ball_y, ball_size, ball_size))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit pygame
pygame.quit()