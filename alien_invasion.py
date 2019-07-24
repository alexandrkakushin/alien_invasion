import pygame

import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    ai_settings = Settings()

    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)

    while True:
        gf.check_event(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()