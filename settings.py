import pygame


class Settings:
    """A class to store all setting for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Quit the game settings
        self.quit_keys = [
            pygame.K_q, pygame.K_ESCAPE,
            pygame.K_END
        ]

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed = 0.3
        self.fleet_drop_speed = 3
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
