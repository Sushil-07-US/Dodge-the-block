import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Blocks")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player properties
player_width, player_height = 50, 50
player_x, player_y = WIDTH // 2, HEIGHT - 100
player_speed = 7

# Block properties
block_width, block_height = 50, 50
block_speed = 5
blocks = []

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Score
score = 0

# Main game loop
running = True
while running:
    screen.fill(WHITE)  # Clear the screen each frame

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Add new blocks
    if random.randint(1, 20) == 1:  # Random chance to add a block
        blocks.append([random.randint(0, WIDTH - block_width), 0])

    # Move blocks and check for collision
    for block in blocks[:]:
        block[1] += block_speed
        if block[1] > HEIGHT:  # Remove blocks that go off the screen
            blocks.remove(block)
            score += 1  # Increase score for dodging
        if (player_x < block[0] + block_width and
            player_x + player_width > block[0] and
            player_y < block[1] + block_height and
            player_y + player_height > block[1]):  # Collision check
            print(f"Game Over! Final Score: {score}")
            running = False

    # Draw the player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    # Draw the blocks
    for block in blocks:
        pygame.draw.rect(screen, RED, (block[0], block[1], block_width, block_height))

    # Display the score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()
    clock.tick(30)  # Limit the frame rate to 30 FPS

# Quit Pygame
pygame.quit()
sys.exit()
