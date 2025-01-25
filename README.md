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

  **Classe Grille() :**
  
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

  **Classe Bloc() :**

  Cette classe défini un objet général de type bloc, elle sera utilisé par Solide() et Liquide() pour affiner les caratéristiques du bloc.

  init():
  - Défini le chemin vers le sprite du bloc
  - Défini la taille des rects pour les collisions

  charger_sprite():
  - Redimensionne le sprite en 16x en 64x

  **Classe Solide() :**
  Cette classe utilise les propiétés de Bloc() pour créer des blocs avec les attributs d'un solide

  init():
  - Défini la dureté du bloc
  - Défini la flammabilité du bloc
  - Défini si le bloc à des collisions ou pas

  **Classe Solide() :**
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
