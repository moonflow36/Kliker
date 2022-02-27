import pygame.image
from pygame.color import THECOLORS


class Seed:
    def __init__(self):
        self.count = 0
        self.image = pygame.image.load(r"img/seed.png")
        self.pos = (40, 0)

    def draw(self, screen):
        screen.blit(self.image, self.pos)


    def write(self, screen):
        font = pygame.font.SysFont('couriernew', 20)
        text = font.render(f"{self.count}", True, [255, 255, 255])
        screen.blit(text, (765, 35))
