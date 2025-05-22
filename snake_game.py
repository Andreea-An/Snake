import pygame
import time
import random

# Initialisation de pygame
pygame.init()

# Définition des couleurs
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Définition de la taille de l'écran
display_width = 800
display_height = 600

# Création de la fenêtre de jeu
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game by Cascade')

# Horloge pour contrôler la vitesse du jeu
clock = pygame.time.Clock()

# Taille du serpent et vitesse du jeu
snake_block = 10
snake_speed = 15

# Définition des polices
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Fonction pour afficher le score
def your_score(score):
    value = score_font.render("Score: " + str(score), True, black)
    dis.blit(value, [0, 0])

# Fonction pour dessiner le serpent
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

# Fonction pour afficher un message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [display_width / 6, display_height / 3])

# Fonction principale du jeu
def gameLoop():
    game_over = False
    game_close = False

    # Position initiale du serpent
    x1 = display_width / 2
    y1 = display_height / 2

    # Changement de position
    x1_change = 0
    y1_change = 0

    # Liste qui contient les segments du serpent
    snake_list = []
    length_of_snake = 1

    # Position initiale de la nourriture
    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("Perdu! Appuyez sur Q pour Quitter ou C pour Continuer", red)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Vérifier si le serpent touche les bords
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True

        # Mise à jour de la position du serpent
        x1 += x1_change
        y1 += y1_change
        
        dis.fill(blue)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Vérifier si le serpent se touche lui-même
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        # Vérifier si le serpent a mangé la nourriture
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Démarrer le jeu
gameLoop()
