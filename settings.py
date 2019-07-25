class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5

        # Параметры пули
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Параметры пришельца
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1
