# Projet-MineSmash

**Préréquis :**

  -Python 3.12
  
  -Pygame 2.6

**Documentation:**
  Quatres fichiers principaux :
  
  -Game.py -- Le script d'exécution du jeu
  
  -Blocs.py -- Gère les blocs et la grille qui permet de placer les blocs à leurs place

  -Personnage.py -- Gère les mouvements, les collisions, et les attributs du joueur (vie, armure ect...)

  -Interface.py -- Gère tout les éléments d'interface notamment la barre d'item, l'inventaire ect...

# Game.py

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

  -boucle qui détecte les appuis de touche uniques (pas de maintient de touche)

  -dessine les éléments à l'écran et actualise l'affichage

  
