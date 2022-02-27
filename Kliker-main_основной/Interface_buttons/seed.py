import pygame.image

class Seed:
    def __init__(self):
        self.count = 0
        self.image = pygame.image.load(r'img/seed.png')
        self.pos = (700, 0)

    def draw(self, screen):
        screen.blit(self.image, self.pos)
        self.write(screen)

    def write(self, screen):
        font = pygame.font.SysFont('arial', 20)
        text = font.render(f"{self.count}", True, [255, 255, 255])
        screen.blit(text, (715, 35))