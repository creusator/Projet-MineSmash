# Projet-MineSmash

**Préréquis :**

  - Python 3.12
  - Pygame 2.6

**Documentation:**

  Fichiers principaux :

  - Variables_Globales.py -- Contient les variables importantes comme la taille de l'écran et des blocs afin d'être modifiable facilement dans tout les scripts.
  - Game.py -- Le script d'exécution du jeu
  - Blocs.py -- Gère la création des blocs et de la grille qui permet de placer les blocs à leurs place
  - Personnage.py -- Gère les mouvements, les collisions, et les attributs du joueur (vie, armure ect...)
  - Interface.py -- Gère tout les éléments d'interface notamment la barre d'item, l'inventaire ect...

# Variables_Globales.py

Contient les variables importantes comme la taille de l'écran et des blocs afin d'être modifiable facilement dans tout les scripts.

Gardez de préférence un ratio 2:1 entre ces valeurs pour l'instant :
- SCREEN_WIDTH, largeur de la fenêtre de jeu
- SCREEN_HEIGHT, hauteur de la fenêtre de jeu

- TILE_SIZE, taille des blocs dans le monde
- FRAMERATE, limite d'images par seconde

# Game.py

Ce fichier gère l'exécution de toutes les fonctions nécéssaires au jeux. Normalement vous n'aurez pas besoin de trop toucher à ce fichier pour résoudre les issues, à part peut être pour empêcher le joueur de s'emmurer.

  **Importation des fichiers et de pygame:**
  
  Permet d'accéder aux fonctions et classes écrites dans les autres fichiers du projet
    
  **Initialisation de pygame:**

  Trois variables permettent de définir la taille de la fenêtre et la limite du framerate

  **Initialisation des objects de base:**

  Défini les principaux objects utilisés dans le projet notamment :

  - Le joueur
  - La grille 
  - Les éléments d'interface

  **Boucle principale :**

  - Défini delta (variable qui permet de rendre la vitesse de déplacement indépendante du framerate)
  - Boucle qui détecte les appuis de touches et effectue les actions en conséquence.
  - Dessine les éléments à l'écran et actualise l'affichage

# Blocs.py

Ce fichier contient toutes les définitions de blocs ainsi que les fonction nécéssaires à leur affichage sur l'écran

  **Importation des librairies :**
  
  La grille de bloc utilise la librairie JSON pour stocker et modifer la grille de blocs.
  Pygame est aussi présent pour la partie affichage de cette dite grille

  **Classe Grille :**
  
  Cette classe s'occupe de gérer la position des blocs et leurs boîte de collision, puis de les afficher à l'écran
  
  init():
  - Défini la largeur, hauteur de la grille
  - Défini la taille des blocs sur l'écran (textures en x16, affiché en x64 sur l'écran)

  charger():
  - Permet de charger le fichier JSON et d'extraire la matrice qu'il contient

  placer_bloc():
  - Permet de placer un bloc de pierre à des coordonées données

  detruire_bloc():
  - Permet de détruire n'importe quel bloc de la grille à des coordonées données

  get_coord_grille():
  - Prend des coordonées x, y sur l'écran et renvoie les indice de la grille correspondant à ces coordonées

  get_bloc():
  - Prend des indices de la grille et renvoie l'indice du bloc a cet endroit

  get_collision_list():
  - Renvoie une liste de rect en fonction des blocs solides présents sur la matrice

  dessiner():
  - Affiche les blocs de la matrice sur l'écran 

  **Classe Bloc :**

  Cette classe défini un objet général de type bloc, elle sera utilisé par Solide() et Liquide() pour affiner les caratéristiques du bloc.

  init():
  - Défini le chemin vers le sprite du bloc
  - Défini la taille des rects pour les collisions

  charger_sprite():
  - Redimensionne le sprite en 16x en 64x

  **Classe Solide :**
  
  Cette classe utilise les propiétés de Bloc() pour créer des blocs avec les attributs d'un solide

  init():
  - Défini la dureté du bloc
  - Défini la flammabilité du bloc
  - Défini si le bloc à des collisions ou pas

  **Classe Liquide :**
  
  Cette classe utilise les propriétés de Bloc() pour créer des blocs avec les attributs d'un liquide

  init():
  - Défini les dégats infligés au joueur quand il touche le liquide
  - Défini la viscosité du liquide

  **Fonction identify_bloc() et définitions:**

  identify_bloc():
  - Renvoi un objet bloc ainsi que tout ses attributs en fonction d'un id

  stone_bloc() :
  - Défini le bloc de pierre
    
  grass_bloc() :
  - Défini le bloc d'herbe

  dirt_bloc() :
  - Défini le bloc de terre

  air() :
  - Défini le bloc d'air

  Dans chacune de ces définitions il y est précisé les caratéristiques du bloc.
  
  L'id du bloc est défini dans la fonction identify_bloc()

# Personnage.py

Ce fichier gère un des objet les plus important du jeu, le personnage. 
Il contient les fonction nécéssaires à ses déplacements et son affichage à l'écran.

  **Importations et définition:**
  - Importation de pygame
  - Importation de la classe Grille() du fichier Blocs.py
  - Définition de vecteur, évite de devoir répéter pygame.math.Vector2

  **Classe Personnage:**

  init() :
  - Définition des variables suivantes :
      - Chemin vers le sprite
      - Vie, armure
      - valeure d'incrémentation de l'accélération, de la friction, de la gravité et de la puissance du saut
      - vitesses maximales horizontale et verticale
      - variables d'état is_jumping et is_on_ground

  - Définition des vecteurs suivants :
        - Coordonées
        - Vélocité, vecteur directionnel appliqué aux coordonées du joueur.
        - Accélération, vecteur appliqué à la vélocité pour accélérer

  charger_sprite():
  - Permet de redimensionner le sprite du personnage en une taille affichable à l'écran

  player_collision_list():
  - En utilisant la fonction get_collision_list() de la classe grille, cette fonction renvoie la liste des rects avec lesquels le rect du personnage est en collision

  check_collision_x():
  - Cette fonction détermine en fonction de la vélocité du joueur, si il doit s'arrêter de bouger vers la gauche ou la droite.
    Si c'est le cas, le personnage sera bloqué dans la dite direction. La fonction velocity_limit() permet de limiter son accélération.

  check_collision_y():
  - Cette fonction détermine en fonction de la vélocité du joueur, si il doit s'arrêter de tomber ou de sauter.
    Si c'est le cas, le personnage sera bloqué dans la dite direction.
    Pour pouvoir détecter la collision vers le bas, le rect du joueur est déplacé d'un pixel vers le bas et est immédiatement replacé pour éviter de rester bloqué dans le bloc.

  horizontal_movement():
  - Effectue les déplacements horizontaux du joueur en fonction des touches appuyés et des variables d' accélération et de friction
  - Empêche le joueur d'accélérer à l'infini grace à la fonction velocity_limit

  vertical_movement():
  - Gère les déplacements verticaux du joueur, plus précisément l'application de la gravité.
  - Empêche le joueur de tomber trop vite en fonction de la variable max_fall_speed

  jump():
  - Gère le saut du joueur en fonction de la barre espace et des variable is_on_ground, is_jumping et jump_force

  move():
  - Utilise les fonctions suivantes :
      - horizontal_movement() pour appliquer les mouvements horizontaux
      - check_collision_x() pour corriger les potentiels emmurements
      - vertical_movement() pour appliquer la gravité
      - check_collision_y() pour empêcher le joueur de tomber dans le sol

  debug():
  - Affiche le rectange de collision du joueur *fonction sujette à évoluer au gré des besoins*

  afficher():
  - Permet d'afficher le sprite du personnage sur l'écran.

# Interface.py

Ce fichier contient toutes les fonctions nécéssaires à l'affichage et la gestion de l'interface.
Sujet aux changements, les fonctionnalités liées à l'inventaire et l'interface n'ont pas fini d'être implémentés

Importation de pygame

**Classe Inventaire**

init():
- Définition de deux sprites
- Définition de deux variables de coordonées (x, y)
- Définiton de is_open qui permet de savoir si l'inventaire est ouvert ou non

charger_inventaire():
- Permet de redimensionner le sprite de l'inventaire a une taille affichable

ouvrir():
- Modifie la valeur de la constante en fonction de celle ci
- La fonction est appelé lorsque la touche e est appuyé

afficher():
- Affiche le sprite de l'inventaire en fonction de la constante

**Classe Barre_outil:**

init():
- Définition du chemin du sprite de la barre d'outils
- Définition de deux variables de coordonées
- Définition de la valeur de l'emplacement du curseur dans la barre

charger_barre():
- Permet de redimensionner le sprite de la barre d'outils pour être utilisable à l'écran

afficher():
- Affiche le sprite de la barre d'outils en fonction de la constante d'ouverture et de la position du curseur de séléction

scroll():
- Change la position du curseur de séléction en fonction de la molette de la souris

**Classe Barre_vie:**

init():
- Définition du chemin du sprite de la barre de vie
- Définition de deux variables de coordonées
- Défintion des variables de taille de la barre

charger_barre():
- Renvoie le sprite de la barre avec une dimension utilisable

afficher():
- Permet d'afficher la barre sur l'écran

**Classe Barre_armure:**

init():
- Définition du chemin du sprite de la barre d'armure
- Définition de deux variables de coordonées
- Défintion des variables de taille de la barre

charger_barre():
- Renvoie le sprite de la barre avec une dimension utilisable

afficher():
- Permet d'afficher la barre sur l'écran
