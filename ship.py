import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""

        # Get the game screen and get its rect.
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('cc2e_codes/project_1/images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""

        # Update the x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        # print(self.rect.x, self.rect.y)
        # print(self.rect.top, self.rect.bottom, self.rect.left, self.rect.right)
        # print(self.rect.topleft, self.rect.bottomleft, self.rect.topright, self.rect.bottomright)
        # print(self.rect.midtop, self.rect.midleft, self.rect.midbottom, self.rect.midright)
        # print(self.rect.center, self.rect.centerx, self.rect.centery)
        # print(self.rect.size, self.rect.width, self.rect.height)
        # print(self.rect.w, self.rect.h)
        self.screen.blit(self.image, self.rect)
