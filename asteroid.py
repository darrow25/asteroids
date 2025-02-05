import pygame
from circleshape import CircleShape
import random 
from constants import ASTEROID_MIN_RADIUS, ASTEROID_POINTS
WHITE = (255, 255, 255)
class Asteroid(CircleShape):
    def __init__(self, x, y, velocity, radius):
        super().__init__(x, y, radius)
        self.radius = radius
        self.velocity = velocity

        self.rect = pygame.Rect(
                x - radius,  # Top-left x-coordinate
                y - radius,  # Top-left y-coordinate
                radius * 2,  # Width
                radius * 2   # Height
            )

    def draw(self, surface):
    
        pygame.draw.circle(surface, WHITE, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

        self.rect.center = (int(self.position.x), int(self.position.y))

    def split(self):
        points = ASTEROID_POINTS.get(self.radius, 0)
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return points
        
        random_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        Asteroid(self.position.x, self.position.y, new_velocity1 * 1.2, new_radius)
        Asteroid(self.position.x, self.position.y, new_velocity2 * 1.2, new_radius) 
        return points
