import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up screen dimensions and colors
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Word Bomb")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Fonts
font_large = pygame.font.Font(None, 74)
font_small = pygame.font.Font(None, 50)

# Game variables
word_list = ["python", "pygame", "bomb", "explode", "timer", "keyboard", "game"]
current_word = random.choice(word_list)
typed_text = ""
time_limit = 5  # seconds to type each word
start_time = time.time()
score = 0
game_over = False

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    # Calculate remaining time
    elapsed_time = time.time() - start_time
    remaining_time = time_limit - elapsed_time

    # Display current word
    word_text = font_large.render(current_word, True, BLACK)
    screen.blit(word_text, (WIDTH // 2 - word_text.get_width() // 2, HEIGHT // 2 - 100))

    # Display typed text
    typed_text_render = font_small.render(typed_text, True, BLACK)
    screen.blit(typed_text_render, (WIDTH // 2 - typed_text_render.get_width() // 2, HEIGHT // 2))

    # Display timer
    timer_text = font_large.render(f"{int(remaining_time)}", True, RED if remaining_time <= 2 else BLACK)
    screen.blit(timer_text, (WIDTH // 2 - timer_text.get_width() // 2, HEIGHT // 2 + 100))

    # Display score
    score_text = font_small.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Check if time runs out
    if remaining_time <= 0:
        game_over = True

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game_over:
                # Reset the game if game over
                game_over = False
                score = 0
                current_word = random.choice(word_list)
                typed_text = ""
                start_time = time.time()
            elif event.key == pygame.K_BACKSPACE:
                typed_text = typed_text[:-1]
            elif event.key == pygame.K_RETURN:
                if typed_text.lower() == current_word:
                    score += 1
                    current_word = random.choice(word_list)
                    typed_text = ""
                    start_time = time.time()  # reset timer
                else:
                    game_over = True  # incorrect word ends the game
            else:
                typed_text += event.unicode

    # Display game over message
    if game_over:
        game_over_text = font_large.render("Game Over", True, RED)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 + 150))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
