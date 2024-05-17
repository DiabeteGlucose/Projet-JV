import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Constantes de l'écran
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (255, 255, 255)

# Classe pour le joueur
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 5

    def update(self, walls):
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx = -self.speed
        if keys[pygame.K_RIGHT]:
            dx = self.speed
        if keys[pygame.K_UP]:
            dy = -self.speed
        if keys[pygame.K_DOWN]:
            dy = self.speed

        # Déplacer le joueur et vérifier les collisions
        self.rect.x += dx
        if pygame.sprite.spritecollideany(self, walls):
            self.rect.x -= dx
        
        self.rect.y += dy
        if pygame.sprite.spritecollideany(self, walls):
            self.rect.y -= dy

# Classe pour les murs
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# Initialisation de l'écran
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Collision entre le joueur et le mur")

# Création des groupes de sprites
all_sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()

# Création des objets
player = Player(100, 100)
wall = Wall(300, 200, 200, 50)

# Ajout des objets aux groupes de sprites
all_sprites.add(player)
all_sprites.add(wall)
walls.add(wall)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mise à jour des objets
    all_sprites.update(walls)

    # Dessin à l'écran
    screen.fill(BACKGROUND_COLOR)
    all_sprites.draw(screen)
    pygame.display.flip()

    # Contrôle de la cadence de la boucle
    pygame.time.Clock().tick(60)

# Quitter Pygame
pygame.quit()
sys.exit()



