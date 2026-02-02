import matplotlib.pyplot as plt
import os
import PIL
from PIL import Image
import numpy as np

def loadSetImages(cheese, set, pathbdd, flag, heigth, width):
    ''' 
    La fonction getSetImages récupère les images d'un ensemble spécifié d'un type de cheese
    à partir d'un chemin donné et les stocke dans un dictionnaire où la clé est le numéro d'ordre
    de l'image et la valeur est l'image elle-même.

    Args:
        - cheese (str) : Le type de cheese dont vous souhaitez récupérer les images.
        - set (str) : Le nom de l'ensemble d'images à récupérer.
        - pathbdd (str) : Le chemin du répertoire où se trouvent les images.

    Returns:
        - dict : Un dictionnaire contenant les images récupérées, où la clé est un numéro d'ordre
        de l'image et la valeur est l'image elle-même.
    '''


    # Path où se situe les images du set
    pathImages = pathbdd + cheese + "/" + set + "/"
    
    # Création d'un dictionnaire vide
    images_dict = {}
    
    # Initialisation d'un compteur
    counter = 1
    
    # Récupération de la liste des fichiers dans pathbdd
    images = os.listdir(pathImages)
    
    # Pour chaque fichier
    for imageName in images:
        if imageName == ".DS_Store":
            continue
        # read l'image 
        image = Image.open(pathImages + imageName)
        image = image.convert('RGB')
        
        # Redimensionnement de l'image
        if flag :
            image = image.resize((width,heigth), Image.BILINEAR)
        # Remplissage de la variable x
        x = np.asarray(image)
        
        # Fermeture de l'image
        image.close()
        
        # Ajouter l'image dans le dictionnaire avec pour nom le compteur
        images_dict[counter] = x
        
        # Incrémentation du compteur
        counter += 1
    
    # retourner le dictionnaire
    return images_dict

def loadSetImage(set, pathbdd,flag, heigth, width):
    '''
        Récupère les images de différents ensembles pour un type de set spécifié à partir d'un chemin donné
        et les stocke dans un dictionnaire de dictionnaires.

    Args:
        set (str): Le type de set dont on souhaites récupérer les images.
        pathbdd (str): Le chemin du répertoire où se trouvent les images.

    Returns:
        dict: Un dictionnaire de dictionnaires contenant les images récupérées pour chaque ensemble,
        où la clé principale est le nom de l'ensemble et la valeur est un dictionnaire d'images.

    '''
   
    sets = ["train", "test", "validation"]
    
    # Création d'un dictionnaire vide
    set_images = {}
    
    # Pour chaque set
    for cheese in cheeses:
        print("chargement du fromage : " + cheese)
        # Récupérer le dictionnaire du set
        set_dict = loadSetImages(cheese, set, pathbdd,flag, heigth, width)
        
        # Associer au dictionnaire vide la clé : set_name et la valeur : set_dict
        set_images[cheese] = set_dict
    
    # retourner le dictionnaire
    return set_images

def loadbdd(pathbdd,flag, heigth, width):
    '''
        Charge les données d'images pour différents types de fromages à partir
        d'un répertoire donné et les stocke dans un dictionnaire.

    Args:
        pathbdd (str): Le chemin du répertoire où se trouvent les données
        d'images pour différents types de fromages.

    Returns:
        MyDict : Le dictionnaire correspondant à la base de donnée.
    '''
    
    cheeses = ["beaufort","bleu","brie","camembert","comte","morbier","roquefort","tomme_de_savoie"]
 
    # Création d'un dictionnaire vide
    MyDict = {}
    
    # Pour chaque set
    for set in sets:
        print("chargement du set : " + set)
        # Récupérer le dictionnaire du set
        setDict = loadSetImage(set, pathbdd,flag, heigth, width);
        
        # Associer au dictionnaire vide la clé : set_name et la valeur : set_dict
        MyDict[set] = setDict
    
    # retourner le dictionnaire
    return MyDict

def getImage(dictBdd, cheese: str, set: str, nbr: int):
    """
    Obtient une image à partir d'un dictionnaire de base de données d'images en spécifiant
    le nom du fromage, le nom de l'ensemble et l'index de l'image.

    Args :
    dictBdd (dict) : Un dictionnaire représentant la base de données d'images. 
                     La structure doit être : {nom_du_fromage : {nom_ensemble : {index : image}}}
    cheese (str) : Le nom du fromage dont on veut obtenir l'image.
    set_ (str) : Le nom de l'ensemble auquel appartient l'image.
    nbr (int) : L'index de l'image dans l'ensemble spécifié.

    Returns :
    L'image correspondant aux paramètres spécifiés.
    Si les paramètres ne correspondent à aucune image dans la base de données, retourne None.

    """
    try:
        return dictBdd[cheese][set][nbr]
    except KeyError:
        # Si une clé est manquante, retourne None
        return None

def getStatsDict(dictBdd):
    """
    Calcule des statistiques (nombre d'images, statistiques de hauteur, statistiques de largeur) à partir d'un dictionnaire d'images.

    Paramètres :
    dictBdd (dict) : Un dictionnaire imbriqué représentant la base de données d'images.
                 La structure est : {nom_du_fromage : {nom_ensemble : {index : image}}}

    Renvoie :
    tuple : Un tuple contenant :
        - nbrImage (int) : Nombre total d'images.
        - heigthStat (list) : Une liste contenant la hauteur minimale, moyenne et maximale des images.
                               Format : [hauteur_min, hauteur_moy, hauteur_max]
        - widthStat (list) : Une liste contenant la largeur minimale, moyenne et maximale des images.
                              Format : [largeur_min, largeur_moy, largeur_max]
    """

    nbrImage = 0
    heigthStat = [None, None, None]
    widthStat = [None, None, None]
    
    for cheese in dictBdd.keys():
        dictCheese = dictBdd[cheese]
        for set_name in dictCheese.keys():
            dictSet = dictCheese[set_name]
            for index in dictSet.keys():
                image = dictSet[index]
                nbrImage += 1
                heigth = image.shape[0]
                width = image.shape[1]
                
                if heigthStat[0] is None:
                    heigthStat = [heigth, heigth, heigth]
                    widthStat = [width, width, width]
                
                heigthStat[1] += heigth
                widthStat[1] += width
                
                heigthStat[0] = min(heigth, heigthStat[0])
                widthStat[0] = min(width, widthStat[0])
                
                heigthStat[2] = max(heigth, heigthStat[2])
                widthStat[2] = max(width, widthStat[2])
    
    heigthStat[1] = heigthStat[1] / nbrImage
    widthStat[1] = widthStat[1] / nbrImage
    
    return nbrImage, heigthStat, widthStat

dic = loadbdd("./scripts/",1,200,200)
stat = getStatsDict(dic)
print("nombre d'image", stat[0])
print("Stat sur la hauteur", stat[1])
print("Stat sur la largeur", stat[2])
image = getImage(dic,"train","brie",2)
print(dic.keys)
print(dic["train"].keys())
print(dic["train"]["brie"].keys())
print(image.shape)
# Afficher l'image
# Créer une figure et des sous-graphiques (axes)
fig, axes = plt.subplots(1, 2)

# Afficher la première image sur le premier axe
axes[0].imshow(image)
axes[0].axis('off')  # Pour ne pas afficher les axes

# Afficher la deuxième image (redimensionnée) sur le deuxième axe
axes[1].imshow(image)
axes[1].axis('off')  # Pour ne pas afficher les axes

# Afficher les deux images côte à côte
plt.show()





