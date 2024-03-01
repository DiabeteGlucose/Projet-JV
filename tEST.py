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

# Charger l'image de l'arrière-plan
fond = pygame.image.load("LA JUNGLE !!!!.png")

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu de singe")

# Chargement des images
image_personnage = pygame.image.load("Singe.png").convert_alpha()
image_obstacle = pygame.image.load("bANANESprite.png").convert_alpha()
image_bonus = pygame.image.load("banana BLUE.png").convert_alpha()
image_multiplicateur = pygame.image.load("Salade.png").convert_alpha()

# Redimensionnement des images
image_personnage = pygame.transform.scale(image_personnage, (50, 50))
image_obstacle = pygame.transform.scale(image_obstacle, (50, 50))
image_bonus = pygame.transform.scale(image_bonus, (25, 25))
image_multiplicateur = pygame.transform.scale(image_multiplicateur, (50, 25))
class Personnage(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_personnage
        self.rect = self.image.get_rect()
        self.rect.x = largeur // 2
        self.rect.y = hauteur - 100
        self.vitesse = 7

    def update(self):
        touches = pygame.key.get_pressed()
        if touches[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.vitesse
        if touches[pygame.K_RIGHT] and self.rect.x < largeur - self.rect.width:
            self.rect.x += self.vitesse

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_obstacle
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(largeur - self.rect.width)
        self.rect.y = -self.rect.height
        self.vitesse = random.randint(3, 8)

    def update(self):
        self.rect.y += self.vitesse
        if self.rect.y > hauteur:
            self.rect.x = random.randrange(largeur - self.rect.width)
            self.rect.y = -self.rect.height
            self.vitesse = random.randint(4, 7)

class Bonus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_bonus
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(largeur - self.rect.width)
        self.rect.y = -self.rect.height
        self.vitesse = random.randint(2, 5)
    
    def update(self):
        self.rect.y += self.vitesse
        if self.rect.y > hauteur:
            self.rect.x = random.randrange(largeur - self.rect.width)
            self.rect.y = -self.rect.height
            self.vitesse = random.randint(4, 7)

class multiplicateur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_multiplicateur
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(largeur - self.rect.width)
        self.rect.y = -self.rect.height
        self.vitesse = random.randint(7, 11)
    
    def update(self):
        self.rect.y += self.vitesse
        if self.rect.y > hauteur:
            self.rect.x = random.randrange(largeur - self.rect.width)
            self.rect.y = -self.rect.height
            self.vitesse = random.randint(7, 11)


# Création des sprites
all_sprites = pygame.sprite.Group()
personnage = Personnage()
all_sprites.add(personnage)
obstacles = pygame.sprite.Group()
bonuses = pygame.sprite.Group()
mult = pygame.sprite.Group()

debut_jeu = pygame.time.get_ticks()

# Boucle de jeu
clock = pygame.time.Clock()
game_over = False
score = 0
victoire = False
 
 
while not game_over and not victoire:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    if len(mult) < 1:
        Multiplicateur = multiplicateur()
        mult.add(Multiplicateur)
        all_sprites.add(Multiplicateur)

    # Ajout de bonus
    if len(bonuses) < 4:
        bonus = Bonus()
        bonuses.add(bonus)
        all_sprites.add(bonus)
    
    # Au début du jeu

    # Ajout d'obstacles
    if len(obstacles) < 7:
        obstacle = Obstacle()
        obstacles.add(obstacle)
        all_sprites.add(obstacle)

    # Mise à jour des sprites
    all_sprites.update()

# Gestion des bonus
    bonus_collisions = pygame.sprite.spritecollide(personnage, bonuses, True)
    for bonus in bonus_collisions:
        score += 10

    # Gestion des mult
    mult_collisions = pygame.sprite.spritecollide(personnage, mult, True)
    for Multiplicateur in mult_collisions:
        score *= 1.5


    # Gestion des collisions
    if pygame.sprite.spritecollide(personnage, obstacles, False):
        game_over = True

    # Effacement de l'écran
    fenetre.fill(BLANC)
    
     # Affichage de l'arrière-plan
    fenetre.blit(fond, (0, 0))

    # Affichage des sprites
    all_sprites.draw(fenetre)

    # Début du jeu
    

     # Calcul du temps écoulé depuis le début du jeu en secondes
    temps_ecoule = (pygame.time.get_ticks() - debut_jeu) // 1000


        # Affichage du score
    police_score = pygame.font.SysFont("Arial", 30)
    texte_score = police_score.render("Score: " + str(score), True, BLANC)
    fenetre.blit(texte_score, (10, 10))

    # Affichage du chronomètre à gauche de l'écran
    police_fin = pygame.font.SysFont("Arial", 30)
    texte_chrono = police_fin.render("Temps écoulé: {} s".format(temps_ecoule), True, BLANC)
    fenetre.blit(texte_chrono, (500, 10))


    # Rafraîchissement de l'écran
    pygame.display.flip()

    # Limite de FPS
    clock.tick(60)

 # Vérification de la victoire
    if score >= 1000 :
        victoire = True

if victoire:
    fenetre.fill(BLANC)
    police_fin = pygame.font.SysFont("Arial", 50)
    texte_fin = police_fin.render("Félicitations ! Pas mal les bzez !", True, NOIR)
    fenetre.blit(texte_fin, ((largeur - texte_fin.get_width()) // 2, (hauteur - texte_fin.get_height()) // 2))
    pygame.display.flip()


# Affichage du message de fin de jeu
if game_over:
    fenetre.fill(BLANC)
    police_fin = pygame.font.SysFont("Arial", 50)
    texte_fin = police_fin.render("Ta mère l'ourang-outan", True, NOIR)
    fenetre.blit(texte_fin, ((largeur - texte_fin.get_width()) // 2, (hauteur - texte_fin.get_height()) // 2))
    pygame.display.flip()

# Attente avant de quitter
pygame.time.delay(2000)

# Fermeture de Pygame
pygame.quit()
sys.exit()