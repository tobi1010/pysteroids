import pygame
import random
from constants import ASTEROID_MIN_RADIUS

from circleshape import CircleShape


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.containers = None

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x, self.position.y, new_radius)
            a2 = Asteroid(self.position.x, self.position.y, new_radius)
            random_angle = random.uniform(20, 50)
            a1.velocity = self.velocity.rotate(random_angle) * 1.2
            a2.velocity = self.velocity.rotate(-random_angle) * 1.2
            self.kill()

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
