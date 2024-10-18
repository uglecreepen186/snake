import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

window_width = 800
window_height = 600

segment_size = 20
segment_speed = 20

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Змейка")

clock = pygame.time.Clock()


def show_text(surface, text, size, x, y):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, WHITE)
    surface.blit(text_surface, (x, y))


def check_collision(segment_list):
    head = segment_list[0]
    if head[0] < 0 or head[0] >= window_width or head[1] < 0 or head[1] >= window_height:
        return True
    if head in segment_list[1:]:
        return True
    return False


def run_game():
    game_over = False
    game_close = False

    head_x = window_width // 2
    head_y = window_height // 2
    dx = 0
    dy = 0

    segment_list = []
    segment_length = 1

    apple_x = random.randint(0, (window_width // segment_size) - 1) * segment_size
    apple_y = random.randint(0, (window_height // segment_size) - 1) * segment_size

    while not game_over:
        while game_close:
            window.fill(BLACK)
            show_text(window, f"Конец игры! Ваш счёт: {segment_length - 1}", 30, 250, 300)
            show_text(window, "Нажмите 'Q' для выхода или 'C' для начала новой игры", 30, 110, 350)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        run_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -segment_speed
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = segment_speed
                    dy = 0
                elif event.key == pygame.K_UP:
                    dx = 0
                    dy = -segment_speed
                elif event.key == pygame.K_DOWN:
                    dx = 0
                    dy = segment_speed

        head_x += dx
        head_y += dy

        segment_list.insert(0, (head_x, head_y))

        if len(segment_list) > segment_length:
            segment_list.pop()

        if check_collision(segment_list):
            game_close = True

        if head_x == apple_x and head_y == apple_y:
            segment_length += 1
            apple_x = random.randint(0, (window_width // segment_size) - 1) * segment_size
            apple_y = random.randint(0, (window_height // segment_size) - 1) * segment_size

        window.fill(BLACK)

        for segment in segment_list:
            pygame.draw.rect(window, GREEN, (segment[0], segment[1], segment_size, segment_size))

        pygame.draw.rect(window, RED, (apple_x, apple_y, segment_size, segment_size))

        show_text(window, f"Очки: {segment_length - 1}", 30, 10, 10)

        pygame.display.update()
        clock.tick(15)

    pygame.quit()
    quit()


run_game()