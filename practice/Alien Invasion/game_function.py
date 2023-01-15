import sys
import pygame

def check_events(ship):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    ship.moving_left = False

def update_screen(bg_color,screen,ship):
    # 每次循环都绘制屏幕
    screen.fill(bg_color)
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()