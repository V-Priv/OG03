import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/Тир.jpg")
pygame.display.set_icon(icon)


target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH-target_width)
target_y = random.randint(0, SCREEN_HEIGHT-target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Переменные для движения мыши
moving_mode = False
velocity_x = 2  # скорость по оси X
velocity_y = 2  # скорость по оси Y

running = True

while running:
  screen.fill(color)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      mouse_x, mouse_y = pygame.mouse.get_pos()
      if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
          target_x = random.randint(0, SCREEN_WIDTH - target_width)
          target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    if event.type == pygame.KEYDOWN: # Переключение режима движения
      if event.key == pygame.K_m: # Нажатие клавиши "M" для переключения режима
        moving_mode = not moving_mode

    if moving_mode:    # логика движения мишени
      target_x += velocity_x
      target_y += velocity_y
      if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
          velocity_x = -velocity_x
      if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
          velocity_y = -velocity_y

    screen.blit( target_img, (target_x,target_y))
    pygame.display.update()

# pass

pygame.quit()
