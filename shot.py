# ---------- import dependencies ----------------
import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, SHOT_RADIUS)

    def update(self, dt):
        self.position += self.velocity * dt

    def collides_with(self, other):
        if CircleShape:
            distance = self.position.distance_to(other.position)
            return distance <= (self.radius + other.radius)
