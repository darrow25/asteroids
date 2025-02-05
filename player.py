import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
import math
from Shot import Shot



class Player(CircleShape):
    def __init__(self, x, y, shots):
        CircleShape.__init__(self, x, y, PLAYER_RADIUS)  
        self.timer = 0        
        self.rotation = 0
        self.speed = 0  # Start stationary
        self.velocity = pygame.Vector2(0, 0)
        self.position = pygame.Vector2(x, y)
        self.shots = shots

        self.rect = pygame.Rect(
            self.position.x - PLAYER_RADIUS, 
            self.position.y - PLAYER_RADIUS, 
            PLAYER_RADIUS * 2,
            PLAYER_RADIUS * 2
        )


    def shoot(self):
        
        if self.timer > 0:
            return
        
        self.timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)

        shot_velocity = pygame.Vector2(0, -1)
        shot_velocity.rotate_ip(self.rotation)
        shot_velocity = shot_velocity * PLAYER_SHOOT_SPEED

        shot.velocity = shot_velocity
        self.shots.add(shot)


    def move(self, dt):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
    
        # Scale the forward vector by speed to calculate velocity
        self.velocity = forward * self.speed

        # Update the position based on velocity and dt
        self.position += self.velocity * dt
        self.rect.center = (self.position.x, self.position.y)
        


    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    
    def update(self, dt):
        if self.timer > 0:
            self.timer = self.timer - dt
        if self.timer < 0:
            self.timer = 0
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        elif keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.speed = PLAYER_SPEED
        elif keys[pygame.K_s]:
            self.speed = -PLAYER_SPEED
        else:
            self.speed = 0
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.move(dt)
# in the player class
    def triangle(self):
        position = self.position
        
        # Forward vector (tip of the triangle)
        forward = pygame.Vector2(0, -1).rotate(self.rotation) * (self.radius * 2)
        
        # Right vector for the base corners
        right = pygame.Vector2(1, 0).rotate(self.rotation) * self.radius
        
        # Calculate the three points
        tip = position + forward  # Front of ship
        left = position - (forward/2) - right  # Bottom left
        right = position - (forward/2) + right  # Bottom right
        
        return [tuple(map(int, tip)), tuple(map(int, left)), tuple(map(int, right))]

    def draw(self, screen):
        # What list of points will be the "triangle"? Hint: Use self.triangle()
        # What color should the triangle be? Hint: Use "white"
        # Remember to set a line width of 2
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        