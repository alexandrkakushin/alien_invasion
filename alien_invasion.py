import pygame

import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group


def run_game():
    ai_settings = Settings()

    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)

    aliens = Group()
    bullets = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_event(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets, aliens)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
