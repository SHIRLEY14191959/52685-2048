import pygame
import random

pygame.init()

GRID_SIZE = 4
GRID_WIDTH = 100
GRID_MARGIN = 10
GRID_FONT_SIZE = 36
GRID_BG_COLOR = (187, 173, 160)
GRID_CELL_COLORS = {
    0: (205, 192, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}

WINDOW_SIZE = (GRID_WIDTH * GRID_SIZE + GRID_MARGIN * (GRID_SIZE + 1),
               GRID_WIDTH * GRID_SIZE + GRID_MARGIN * (GRID_SIZE + 1))
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("2048 Game")

grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

def generate_new_tile():
    empty_cells = [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = 2 if random.random() < 0.9 else 4

def draw_grid():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            cell_value = grid[i][j]
            cell_color = GRID_CELL_COLORS.get(cell_value, (255, 255, 255))
            pygame.draw.rect(window, cell_color, [
                             (GRID_MARGIN + GRID_WIDTH) * j + GRID_MARGIN,
                             (GRID_MARGIN + GRID_WIDTH) * i + GRID_MARGIN,
                             GRID_WIDTH, GRID_WIDTH])
            if cell_value:
                font = pygame.font.Font(None, GRID_FONT_SIZE)
                text = font.render(str(cell_value), True, (0, 0, 0))
                text_rect = text.get_rect()
                text_rect.center = (
                    (GRID_MARGIN + GRID_WIDTH) * j + GRID_MARGIN + GRID_WIDTH // 2,
                    (GRID_MARGIN + GRID_WIDTH) * i + GRID_MARGIN + GRID_WIDTH // 2)
                window.blit(text, text_rect)

def is_game_over():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] == 0:
                return False
            if i > 0 and grid[i][j] == grid[i - 1][j]:
                return False
            if i < GRID_SIZE - 1 and grid[i][j] == grid[i + 1][j]:
                return False
            if j > 0 and grid[i][j] == grid[i][j - 1]:
                return False
            if j < GRID_SIZE - 1 and grid[i][j] == grid[i][j + 1]:
                return False
    return True

def move(direction):
    if direction == "left":
        for i in range(GRID_SIZE):
            for j in range(1, GRID_SIZE):
                if grid[i][j]:
                    k = j
                    while k > 0 and grid[i][k - 1] == 0:
                        grid[i][k - 1] = grid[i][k]
                        grid[i][k] = 0
                        k -= 1
                    if k > 0 and grid[i][k - 1] == grid[i][k]:
                        grid[i][k - 1] *= 2
                        grid[i][k] = 0
    elif direction == "right":
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE - 2, -1, -1):
                if grid[i][j]:
                    k = j
                    while k < GRID_SIZE - 1 and grid[i][k + 1] == 0:
                        grid[i][k + 1] = grid[i][k]
                        grid[i][k] = 0
                        k += 1
                    if k < GRID_SIZE - 1 and grid[i][k + 1] == grid[i][k]:
                        grid[i][k + 1] *= 2
                        grid[i][k] = 0
    elif direction == "up":
        for j in range(GRID_SIZE):
            for i in range(1, GRID_SIZE):
                if grid[i][j]:
                    k = i
                    while k > 0 and grid[k - 1][j] == 0:
                        grid[k - 1][j] = grid[k][j]
                        grid[k][j] = 0
                        k -= 1
                    if k > 0 and grid[k - 1][j] == grid[k][j]:
                        grid[k - 1][j] *= 2
                        grid[k][j] = 0
    elif direction == "down":
        for j in range(GRID_SIZE):
            for i in range(GRID_SIZE - 2, -1, -1):
                if grid[i][j]:
                    k = i
                    while k < GRID_SIZE - 1 and grid[k + 1][j] == 0:
                        grid[k + 1][j] = grid[k][j]
                        grid[k][j] = 0
                        k += 1
                    if k < GRID_SIZE - 1 and grid[k + 1][j] == grid[k][j]:
                        grid[k + 1][j] *= 2
                        grid[k][j] = 0

running = True
generate_new_tile()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if not is_game_over():
                if event.key == pygame.K_LEFT:
                    move("left")
                elif event.key == pygame.K_RIGHT:
                    move("right")
                elif event.key == pygame.K_UP:
                    move("up")
                elif event.key == pygame.K_DOWN:
                    move("down")
                generate_new_tile()

    window.fill(GRID_BG_COLOR)
    draw_grid()
    pygame.display.flip()

pygame.quit()
