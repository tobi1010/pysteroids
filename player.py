import pygame
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOT_SPEED,
    PLAYER_SHOOT_COOLDOWN,
)
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):

    def __init__(
        self,
        x,
        y,
    ):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.containers = None
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        if self.timer <= 0:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = (
                pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
            )
            self.timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_j]:
            self.rotate(-dt)
        if keys[pygame.K_l]:
            self.rotate(dt)
        if keys[pygame.K_i]:
            self.move(dt)
        if keys[pygame.K_k]:
            self.move(-dt)
        if keys[pygame.K_u]:
            self.shoot(dt)
