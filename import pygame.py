import pygame
import random
import sys

# Initialisation de Pygame
pygame.init()

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Dimensions de l'écran
largeur = 800
hauteur = 600
taille_fruit = 50

# Création de l'écran
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu de rattrapage de fruits")

# Définition des classes
class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super(Fruit, self).__init__()
        self.image = pygame.Surface([taille_fruit, taille_fruit])
        self.image.fill(BLANC)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(largeur - taille_fruit)
        self.rect.y = -taille_fruit
        self.vitesse = random.randint(1, 5)

    def update(self):
        self.rect.y += self.vitesse
        if self.rect.y > hauteur:
            self.rect.y = -taille_fruit
            self.rect.x = random.randrange(largeur - taille_fruit)
            self.vitesse = random.randint(1, 5)

class Joueur(pygame.sprite.Sprite):
    def __init__(self):
        super(Joueur, self).__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(NOIR)
        self.rect = self.image.get_rect()
        self.rect.x = (largeur - self.rect.width) // 2
        self.rect.y = hauteur - 100

    def update(self):
        pos_souris = pygame.mouse.get_pos()
        self.rect.x = pos_souris[0]

# Création des groupes de sprites
tous_les_sprites = pygame.sprite.Group()
fruits = pygame.sprite.Group()

# Création du joueur
joueur = Joueur()
tous_les_sprites.add(joueur)

# Boucle de jeu
clock = pygame.time.Clock()
game_over = False
score = 0

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Création de nouveaux fruits
    if len(fruits) < 10:
        fruit = Fruit()
        fruits.add(fruit)
        tous_les_sprites.add(fruit)

    # Mise à jour des sprites
    tous_les_sprites.update()

    # Détection des collisions
    collisions = pygame.sprite.spritecollide(joueur, fruits, True)
    for collision in collisions:
        score += 1

    # Affichage du score
    fenetre.fill(BLANC)
    pygame.draw.line(fenetre, NOIR, (0, hauteur - 50), (largeur, hauteur - 50), 5)
    police = pygame.font.SysFont("Arial", 25)
    texte_score = police.render("Score: " + str(score), True, NOIR)
    fenetre.blit(texte_score, (10, hauteur - 40))

    # Affichage des sprites
    tous_les_sprites.draw(fenetre)

    pygame.display.flip()

    # Limite de 60 images par seconde
    clock.tick(60)

pygame.quit()
sys.exit()
