"""
   Description :
        Programme, Python, pour dessiner des formes géométriques
        en utilisant utilisant la bibliothèque turtle.
        
   Auteur : Mohammed Hashas
   Date   : novembre 2023
        
        Turtle est un module de la bibliothèque standard de Python qui permet 
        de créer des graphiques vectoriels à l'aide d'une interface graphique simple 
        et facile à apprendre. Ce module est souvent utilisé pour enseigner la 
        programmation aux débutants car il offre un moyen intuitif de dessiner 
        des formes géométriques, des motifs et des images.

        La fonctionnalité la plus couramment utilisée pour dessiner avec Turtle est 
        la création d'une fenêtre graphique où un curseur (appelé turtle, en anglais, 
        signifiant « tortue ») se déplace pour tracer des lignes en fonction des instructions 
        données. Cette tortue peut avancer, reculer, tourner à gauche ou à droite, et dessiner 
        des formes en fonction des commandes données par le programme.

        Le module Turtle fournit un ensemble de fonctions qui permettent de contrôler le mouvement 
        de la tortue, notamment forward(), backward(), left(), right(), up(), down(), etc.

"""

import turtle

# Fonction pour dessiner le triangle de Sierpinski de manière récursive
def sierpinski(t, order, size):
    if order == 0:
        # Dessiner le triangle de base
        for _ in range(3):
            t.forward(size)
            t.left(120)
    else:
        # Appeler récursivement la fonction pour chaque sous-triangle
        sierpinski(t, order - 1, size / 2)
        t.forward(size / 2)
        
        sierpinski(t, order - 1, size / 2)
        t.backward(size / 2)
        t.left(60)
        t.forward(size / 2)
        t.right(60)
        
        sierpinski(t, order - 1, size / 2)
        t.left(60)
        t.backward(size / 2)
        t.right(60)


def dessinerFormeGeometrique(tortue, csize, cote, angle):
    # Dessiner un carré, un triangle
    for _ in range(cote):
        tortue.forward(csize)
        tortue.left(angle)

# Initialisation du screen
screen = turtle.Screen()
screen.title("Dessin de formes géométriques")
screen.setup(width=700, height=700)
screen.tracer(0)

# Création de la tortue
t = turtle.Turtle()
t.speed(100)
t.up()
t.goto(-200, -200)                                  # Position centrale (0,0)
t.down()


# Appel de la fonction pour dessiner le triangle de Sierpinski
t.color("red")
sierpinski(t, 5, 300)                               # Dessine un Triangle de Sierpinski

# Dessiner un carré de cote = 300
t.color("blue")
dessinerFormeGeometrique(t, 300, 4, 90)             # Dessine un Carré

# Dessiner un triangle de cote = 300
t.color("green")
dessinerFormeGeometrique(t, 300, 3, 120)            # Dessine un Triangle

# Dessiner un pentagone de cote = 300
t.color("black")
dessinerFormeGeometrique(t, 300, 5, 72)             # Dessine un Pentagone

# Dessiner un pentagone de cote = 300
t.color("purple")
dessinerFormeGeometrique(t, 200, 8, 45)             # Dessine un polygone de 8 côtés


#********************* Pentagone/ ***************************************************
#                              /
#        108°                 /
#       pour l'angle interne / 72° pour le pentagone angle externe
#   _______________________ /)_________________
#
#*****************************************************************************

# Forcer la mise à jour de l'écran pour afficher le dessin complet
screen.update()

# Fermeture de la fenêtre lors d'un clic
screen.exitonclick()
turtle.done()