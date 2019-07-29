import pygame

import game_functions as gf
from button import Button
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats


def run_game():
    ai_settings = Settings()

    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    play_button = Button(ai_settings, screen, "Play")

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    ship = Ship(ai_settings, screen)

    aliens = Group()
    bullets = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_event(ai_settings, stats, screen, ship, aliens, bullets, play_button)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, stats, screen, sb, ship, aliens, bullets, play_button)


run_game()
