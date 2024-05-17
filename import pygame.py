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
fond = pygame.image.load("Plan de travail 1.png")

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu de singe")

# Chargement des images
image_personnage = pygame.image.load("Singe.png").convert_alpha()
image_obstacle = pygame.image.load("coco.png").convert_alpha()
image_bonus = pygame.image.load("banane officiel.png").convert_alpha()
image_multiplicateur = pygame.image.load("banane rose (1).png").convert_alpha()
background_image_defaite = 'Minskine.png'
background_image_victoir = 'singe qui a réussi.png'

background_image1 = pygame.image.load(background_image_defaite).convert()
background_image2 = pygame.image.load(background_image_victoir).convert()

# Juste pour rajouter du son
son_bonus = pygame.mixer.Sound("Bonus sound.wav")
son_mult = pygame.mixer.Sound("sON MULT.wav")
Son_Coco_danscrane = pygame.mixer.Sound("Singe mourant.wav")
Ost = pygame.mixer.Sound("Jungle AI.wav")
Crane = pygame.mixer.Sound("bonk meme.wav")
# Redimensionnement des images
image_personnage = pygame.transform.scale(image_personnage, (50, 50))
image_obstacle = pygame.transform.scale(image_obstacle, (50, 50))
image_bonus = pygame.transform.scale(image_bonus, (35, 35))
image_multiplicateur = pygame.transform.scale(image_multiplicateur, (35, 35))

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

# Définir la taille de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Menu")

# Chargez l'image de fond du menu
fond_menu_img = pygame.image.load("Plan de travail 1.png")  # Assurez-vous de remplacer "LA JUNGLE !!!!.png" par le chemin de votre image

# Chargez les images des boutons
bouton_jouer_img = pygame.image.load("bouton play.png")  # Assurez-vous de remplacer "Singe.png" par le chemin de votre image
bouton_options_img = pygame.image.load("quit.png")  # Assurez-vous de remplacer "Option.png" par le chemin de votre image

bouton_jouer_img = pygame.transform.scale(bouton_jouer_img, (100, 100)).convert_alpha()
bouton_options_img = pygame.transform.scale(bouton_options_img, (100, 100)).convert_alpha()

# Fonction pour afficher un message de fin de jeu
def afficher_message(fenetre, message, background_image):
    fenetre.blit(background_image, (0, 0))
    police_fin = pygame.font.SysFont("Arial", 50)
    texte_fin = police_fin.render(message, True, NOIR)
    fenetre.blit(texte_fin, ((largeur - texte_fin.get_width()) // 2, (hauteur - texte_fin.get_height()) // 2))
    pygame.display.flip()
    pygame.time.delay(2000)

# Fonction pour afficher le menu
def afficher_menu():
    bouton_jouer_rect = bouton_jouer_img.get_rect(topleft=(350, 200))
    bouton_options_rect = bouton_options_img.get_rect(topleft=(350, 350))

    menu_running = True
    while menu_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_jouer_rect.collidepoint(event.pos):
                    return "jeu"
                elif bouton_options_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
        
        fenetre.fill(BLANC)
        fenetre.blit(fond_menu_img, (0, 0))
        fenetre.blit(bouton_jouer_img, bouton_jouer_rect.topleft)
        fenetre.blit(bouton_options_img, bouton_options_rect.topleft)
        pygame.display.flip()

# Fonction pour gérer le jeu
def jeu():
    all_sprites = pygame.sprite.Group()
    personnage = Personnage()
    all_sprites.add(personnage)
    obstacles = pygame.sprite.Group()
    bonuses = pygame.sprite.Group()
    mult = pygame.sprite.Group()

    debut_jeu = pygame.time.get_ticks()

    clock = pygame.time.Clock()
    game_over = False
    score = 0
    victoire = False
    Ost.play()
    while not game_over and not victoire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if len(mult) < 1:
            Multiplicateur = multiplicateur()
            mult.add(Multiplicateur)
            all_sprites.add(Multiplicateur)

        if len(bonuses) < 4:
            bonus = Bonus()
            bonuses.add(bonus)
            all_sprites.add(bonus)
    
        if len(obstacles) < 7:
            obstacle = Obstacle()
            obstacles.add(obstacle)
            all_sprites.add(obstacle)

        all_sprites.update()

        bonus_collisions = pygame.sprite.spritecollide(personnage, bonuses, True)
        for bonus in bonus_collisions:
            score += 10
            son_bonus.play()

        mult_collisions = pygame.sprite.spritecollide(personnage, mult, True)
        for Multiplicateur in mult_collisions:
            score *= 1.5
            son_mult.play()

        if pygame.sprite.spritecollide(personnage, obstacles, False):
            game_over = True
            Son_Coco_danscrane.play()
            Crane.play()

        fenetre.fill(BLANC)
        fenetre.blit(fond, (0, 0))
        all_sprites.draw(fenetre)

        temps_ecoule = (pygame.time.get_ticks() - debut_jeu) // 1000

        police_score = pygame.font.SysFont("Arial", 30)
        texte_score = police_score.render("Score: " + str(score), True, BLANC)
        fenetre.blit(texte_score, (10, 10))

        texte_chrono = police_score.render("Temps écoulé: {} s".format(temps_ecoule), True, BLANC)
        fenetre.blit(texte_chrono, (500, 10))

        pygame.display.flip()
        clock.tick(60)

        if score >= 3000:
            victoire = True

    if victoire:
        afficher_message(fenetre, "Félicitations Singe !", background_image2)
        Ost.stop()
    else:
        afficher_message(fenetre, "Ne perd pas espoir... Singe", background_image1)
        Ost.stop
# Fonction principale pour gérer les transitions entre les états du jeu
def main():
    while True:
        etat = afficher_menu()
        if etat == "jeu":
            jeu()

if __name__ == "__main__":
    main()



