import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры окна игры
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Цвета
BLACK = (0, 0, 0)
NEON_BLUE = (72, 198, 231)
NEON_PURPLE = (171, 71, 188)

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Неоновый Кликер")

# Загрузка заднего фона (можно заменить на свой файл изображения)
background = pygame.Surface(screen.get_size())
background.fill(NEON_BLUE)

# Загрузка изображения для кликов
click_image = pygame.image.load("clicker.png")
click_rect = click_image.get_rect()

# Позиция изображения для кликов
click_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Текущий счет кликов
score = 0

# Основной игровой цикл
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if click_rect.collidepoint(event.pos):
                score += 1
                # Проверяем, достиг ли игрок 10 кликов
                if score == 10:
                    # Очищаем экран
                    screen.fill(NEON_BLUE)
                    # Отображаем текст на всем экране
                    font = pygame.font.Font(None, 48)
                    text = font.render("Вы достигли 10 кликов, теперь вы гей", True, NEON_PURPLE)
                    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                    screen.blit(text, text_rect)
                    # Обновляем экран
                    pygame.display.flip()
                    # Ждем некоторое время перед выходом
                    pygame.time.delay(3000)
                    running = False  # Завершаем игру

    # Отображение заднего фона
    screen.blit(background, (0, 0))

    # Отображение изображения для кликов
    screen.blit(click_image, click_rect)

    # Отображение счета
    font = pygame.font.Font(None, 36)
    text = font.render(f"Счет: {score}", True, NEON_PURPLE)
    screen.blit(text, (20, 20))

    # Обновление экрана
    pygame.display.flip()

    # Ограничение частоты кадров
    clock.tick(60)

# Завершение Pygame
pygame.quit()
sys.exit()
