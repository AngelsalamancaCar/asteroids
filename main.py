# ------ Import dependencies --------
import pygame
from constants import *
from logger import log_state


def main():
    # Initialize the game
    pygame.init()

    # Print the notifications.
    print("Starting Asteroids with pygame version: 2.6.1")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Initiate the infinite loop
    while True:
        # call the logger
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # --- fill screen with black ----
        screen.fill("black")

        # Refresh the screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
