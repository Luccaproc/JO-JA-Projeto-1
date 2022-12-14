import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        # Imagem do player
        self.image = pygame.Surface((64,128))
        self.image.fill((207,159,255))
        self.rect = self.image.get_rect(topleft = pos)

        # Movimentação do player
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 5
        self.gravity = 0.5
        self.jump_height = -14

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        keys = pygame.key.get_pressed()
        self.direction.y = self.jump_height

    def update(self):
        self.get_input()
        #self.rect.y += self.direction.y * self.speed

