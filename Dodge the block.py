import pygame
import sys
import random

pygame.init()


WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Blocks")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


player_width, player_height = 50, 50
player_x, player_y = WIDTH // 2, HEIGHT - 100
player_speed = 7

block_width, block_height = 50, 50
block_speed = 5
blocks = []


clock = pygame.time.Clock()


score = 0


running = True
while running:
    screen.fill(WHITE) 

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    
    if random.randint(1, 20) == 1:  
        blocks.append([random.randint(0, WIDTH - block_width), 0])

    
    for block in blocks[:]:
        block[1] += block_speed
        if block[1] > HEIGHT:  
            blocks.remove(block)
            score += 1  # Increase score for dodging
        if (player_x < block[0] + block_width and
            player_x + player_width > block[0] and
            player_y < block[1] + block_height and
            player_y + player_height > block[1]):  
            print(f"Game Over! Final Score: {score}")
            running = False

    
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))


    for block in blocks:
        pygame.draw.rect(screen, RED, (block[0], block[1], block_width, block_height))

    
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))


    pygame.display.flip()
    clock.tick(30)  


pygame.quit()
sys.exit()
