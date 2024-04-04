import pygame
import random

# Initialize Pygame
pygame.init()

# Set up screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 100
NUM_ROWS = 4
NUM_COLS = 4
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Memory Match Game")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Load images
images = []
for i in range(1, 9):
    image = pygame.image.load(f"image{i}.png").convert()
    images.extend([image, image])

# Shuffle images
random.shuffle(images)

# Set up game variables
board = [[-1] * NUM_COLS for _ in range(NUM_ROWS)]
selected = []
score = 0

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and len(selected) < 2:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            col = mouse_x // CELL_SIZE
            row = mouse_y // CELL_SIZE
            if (row, col) not in selected:
                selected.append((row, col))

    # Draw board
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            if (i, j) in selected or board[i][j] != -1:
                screen.blit(images[board[i][j]], (j * CELL_SIZE, i * CELL_SIZE))

    # Check if two tiles are selected
    if len(selected) == 2:
        row1, col1 = selected[0]
        row2, col2 = selected[1]
        if images[board[row1][col1]] == images[board[row2][col2]]:
            score += 1
            selected = []
        else:
            pygame.time.wait(1000)
            board[row1][col1] = -1
            board[row2][col2] = -1
            selected = []

    # Check if game is over
    if score == 8:
        font = pygame.font.Font(None, 36)
        text = font.render("Congratulations! You won!", True, GREEN)
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
