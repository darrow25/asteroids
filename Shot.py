from circleshape import CircleShape
from constants import SHOT_RADIUS
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2()
        self.rect = pygame.Rect(0, 0, SHOT_RADIUS * 2, SHOT_RADIUS * 2)  # A square bounding box
        self.rect.center = (x, y)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = (int(self.position.x), int(self.position.y))

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), self.position, SHOT_RADIUS)  # White circle
    
