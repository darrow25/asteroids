import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from Shot import Shot 

def main():
    pygame.init()
    score = 0
    pygame.font.init()
    font = pygame.font.Font(None, 36)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroids_field = AsteroidField()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)
    
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() 
    dt = 0
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")
        updatable.update(dt)
        collisions = pygame.sprite.groupcollide(shots, asteroids, True, False)
        for shot, hit_asteroids in collisions.items():
            for asteroid in hit_asteroids:
                score += asteroid.split()
        for sprite in drawable:
            sprite.draw(screen)
        if pygame.sprite.spritecollide(player, asteroids, False):
            print("Game Over!")
            
                
            sys.exit()
        for sprite in drawable:
            sprite.draw(screen)
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        pygame.display.flip()
        dt = clock.tick(60) /1000
        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
       main() 

        