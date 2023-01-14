import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    # 初始化游戏并创建屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen_height = ai_settings.screen_height
    screen_width = ai_settings.screen_width
    bg_color = ai_settings.bg_color
    screen = pygame.display.set_mode((screen_height,screen_width))
    pygame.display.set_caption('Alien Invasion')
    
    # 创建一艘飞船
    ship = Ship(screen)
    
    # 开始游戏主循环
    while True:
        # 监听键鼠事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        # 每次循环都绘制屏幕
        screen.fill(bg_color)
        ship.blitme()
        
        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()