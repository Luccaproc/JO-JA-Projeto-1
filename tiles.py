import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill((105,105,105))
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, shift_x):
        self.rect.x += shift_x
