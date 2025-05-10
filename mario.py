import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MARIO_WIDTH = 50
MARIO_HEIGHT = 50
GRAVITY = 1
JUMP_STRENGTH = 15

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Mario Game")

# Mario class
class Mario:
    def __init__(self):
        self.rect = pygame.Rect(100, SCREEN_HEIGHT - MARIO_HEIGHT, MARIO_WIDTH, MARIO_HEIGHT)
        self.velocity_y = 0
        self.on_ground = True

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = -JUMP_STRENGTH
            self.on_ground = False

        # Apply gravity
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        # Check for ground collision
        if self.rect.y >= SCREEN_HEIGHT - MARIO_HEIGHT:
            self.rect.y = SCREEN_HEIGHT - MARIO_HEIGHT
            self.on_ground = True
            self.velocity_y = 0

    def draw(self, surface):
        pygame.draw.rect(surface, BLUE, self.rect)

# Main game loop
def main():
    clock = pygame.time.Clock()
    mario = Mario()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        mario.move(keys)

        # Fill the screen with white
        screen.fill(WHITE)

        # Draw Mario
        mario.draw(screen)

        # Update the display
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()