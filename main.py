# ------ Import dependencies --------
import pygame
from pygame.time import Clock

from constants import *
from logger import log_state
from player import Player

# ------- Start game config ---------


def main():
    # Initialize the game
    pygame.init()

    # Print the notifications.
    print("Starting Asteroids with pygame version: 2.6.1")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create clock object
    clock = pygame.time.Clock()

    # Create delta time variable
    dt = 0

    # Instantiate player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Initiate the infinite loop
    while True:
        # call the logger
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # -- update all objects --
        player.update(dt)

        # --- fill screen with black ----
        screen.fill("black")

        # Draw player
        player.draw(screen)

        # Refresh the screen
        pygame.display.flip()

        # End of loop timing
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
