import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from game_stats import GameStats

def run_game():
    # 初始化游戏并创建屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen_height = ai_settings.screen_height
    screen_width = ai_settings.screen_width
    bg_color = ai_settings.bg_color
    screen = pygame.display.set_mode((screen_height,screen_width))
    pygame.display.set_caption('Alien Invasion')
    
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 创建一艘飞船
    ship = Ship(ai_settings,screen)
    # 创建外星人编组
    aliens = Group()
    # 创建用于存储子弹的编组
    bullets = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    # 开始游戏主循环
    while True:
        # 监听键鼠事件
        gf.check_events(ai_settings,screen,ship,bullets)
        if stats.game_active:
            ship.update_moving()
            gf.update_bullets(ai_settings,screen,ship,bullets,aliens)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
        # 屏幕事件
        gf.update_screen(bg_color,screen,ship,aliens,bullets)
        

run_game()