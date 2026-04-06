# ------ Import dependencies --------
import pygame
from pygame.time import Clock

from constants import *
from logger import log_event, log_state
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
import sys

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

    # Create Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Assign the static containers field for the Player class
    Player.containers = (updatable, drawable)

    # Assign the static containers field for the asteroids class
    Asteroid.containers = (asteroids, updatable, drawable)

    # Assign the static containers field for the asteroidfield class
    AsteroidField.containers = (updatable,)

    # Instantiate player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Instantiate asteroid field
    asteroid_field = AsteroidField()

    # Instantiate shots
    Shot.containers = (shots, updatable, drawable)

    # Initiate the infinite loop
    while True:
        # call the logger
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # -- update all objects in the updatable group --
        updatable.update(dt)

        for asteroid in list(asteroids):
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game Over")
                sys.exit()

            for shot in list(shots):
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                    break

        # --- fill screen with black ----
        screen.fill("black")

        # Loop over drawables and draw them
        for obj in drawable:
            obj.draw(screen)

        # Refresh the screen
        pygame.display.flip()

        # End of loop timing
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
