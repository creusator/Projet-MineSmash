# Projet-MineSmash

**Préréquis :**

  - Python 3.12
  
  - Pygame 2.6

**Documentation:**

  Quatres fichiers principaux :
  
  - Game.py -- Le script d'exécution du jeu
  
  - Blocs.py -- Gère les blocs et la grille qui permet de placer les blocs à leurs place

  - Personnage.py -- Gère les mouvements, les collisions, et les attributs du joueur (vie, armure ect...)

  - Interface.py -- Gère tout les éléments d'interface notamment la barre d'item, l'inventaire ect...

# Game.py

Ce fichier gère l'exécution de toutes les fonctions nécéssaires au jeux. Normalement vous n'aurez pas besoin de trop toucher à ce fichier pour résoudre les issues, à part pour empêcher le joueur de s'emmurer

  **Importation des fichiers et de pygame:**
  
  Permet d'acceder aux fonctions et classes écrites dans les autres fichiers du projet
    
  **Initialisation de pygame:**

  Trois variables permettent de définir la taille de la fenêtre et la limite du framerate

  **Initialisation des objects de base:**

  Défini les principaux objects utilisés dans le projet notamment :

  -Le joueur

  -La grille 

  -Les éléments d'interface

  **Boucle principale :**

  -défini delta

  -boucle qui détecte les appuis de touches et effectue les actions en conséquence.

  -dessine les éléments à l'écran et actualise l'affichage

# Blocs.py

Ce fichier contient toutes les définitions de blocs ainsi que les fonction nécéssaires à leur affichage sur l'écran

  **Importation des librairies :**
  
  La grille de bloc utilise la librairie JSON pour stocker et modifer la grille de blocs.
  Pygame est aussi présent pour la partie affichage de cette dite grille

  **Classe Grille() :**
  
  Cette classe s'occupe de gérer la position des blocs et leurs boîte de collision, puis de les afficher à l'écran
  
  init():
  - défini la largeur, hauteur de la grille
  - défini la taille des blocs sur l'écran (textures en x16, affiché en x64 sur l'écran)

  charger():
  - permet de charger le fichier JSON et d'extraire la matrice qu'il contient

  placer_bloc():
  - permet de placer un bloc de pierre à des coordonées données

  detruire_bloc():
  - permet de détruire n'importe quel bloc de la grille à des coordonées données

  get_coord_grille():
  - prend des coordonées x, y sur l'écran et renvoie les indice de la grille correspondant à ces coordonées

  get_bloc():
  - prend des indices de la grille et renvoie l'indice du bloc a cet endroit

  get_collision_list():
  - renvoie une liste de rect en fonction des blocs solides présents sur la matrice

  dessiner():
  -affiche les blocs de la matrice sur l'écran 

  **Classe Bloc() :**

  Cette classe défini un objet général de type bloc, elle sera utilisé par Solide() et Liquide() pour affiner les caratéristiques du bloc.

  init():
  - défini le chemin vers le sprite du bloc
  - défini la taille des rects pour les collisions

  charger_sprite():
  -redimensionne le sprite en 16x en 64x

  

  
  
