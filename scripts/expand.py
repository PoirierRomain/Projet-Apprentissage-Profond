from PIL import Image
import os
import matplotlib as plt

def expandImage(mypath):
    # Création du fichier expand (si il n'existe pas)
    img = Image.open(mypath)
    # Ouverture de l'image avec PIL
    imgCopy = img.copy()
    # pour toutes les modifications
    img.transpose(Image.FLIP_TOP_BOTTOM)
    
    # Affichage
    fig, axes = plt.subplots(1, 2)

    # Afficher la première image sur le premier axe
    axes[0].imshow(img)
    axes[0].axis('off')  # Pour ne pas afficher les axes

    # Afficher la deuxième image (redimensionnée) sur le deuxième axe
    axes[1].imshow(imgCopy)
    axes[1].axis('off')  # Pour ne pas afficher les axes

    # Afficher les deux images côte à côte
    plt.show()
    
    img.close()
    imgCopy.close()