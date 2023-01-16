import sys
import pygame

def check_keydown_events(event,ship):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True

def check_keyup_events(event,ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False
def check_events(ship):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event,ship)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event,ship)

def update_screen(bg_color,screen,ship):
    # 每次循环都绘制屏幕
    screen.fill(bg_color)
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()