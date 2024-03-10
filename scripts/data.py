import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

def getImage(cheese, nbr, set, pathbdd):
    imageName = cheese + "_" + nbr + "_" + set
    imagePath = pathbdd + cheese + "/" + set + "/" + imageName
    
    return mpimg.imread(imagePath)


def loadSetImages(cheese, set, pathbdd):
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
        # read l'image avec mpimg.imread()
        image = mpimg.imread(pathImages + imageName)
        
        # Ajouter l'image dans le dictionnaire avec pour nom le compteur
        images_dict[counter] = image
        
        # Incrémentation du compteur
        counter += 1
    
    # retourner le dictionnaire
    return images_dict

def loadCheeseImage(cheese, pathbdd):
    '''
        Récupère les images de différents ensembles pour un type de cheese spécifié à partir d'un chemin donné
        et les stocke dans un dictionnaire de dictionnaires.

    Args:
        cheese (str): Le type de cheese dont on souhaites récupérer les images.
        pathbdd (str): Le chemin du répertoire où se trouvent les images.

    Returns:
        dict: Un dictionnaire de dictionnaires contenant les images récupérées pour chaque ensemble,
        où la clé principale est le nom de l'ensemble et la valeur est un dictionnaire d'images.

    '''
    
    sets = ["surplus", "train", "test", "validation"]
    
    # Création d'un dictionnaire vide
    cheese_images = {}
    
    # Pour chaque set
    for set_name in sets:
        # Récupérer le dictionnaire du set
        set_dict = loadSetImages(cheese, set_name, pathbdd)
        
        # Associer au dictionnaire vide la clé : set_name et la valeur : set_dict
        cheese_images[set_name] = set_dict
    
    # retourner le dictionnaire
    return cheese_images

def loadbdd(pathbdd):
    '''
        Charge les données d'images pour différents types de fromages à partir
        d'un répertoire donné et les stocke dans un dictionnaire.

    Args:
        pathbdd (str): Le chemin du répertoire où se trouvent les données
        d'images pour différents types de fromages.

    Returns:
        cheeseDict : Le dictionnaire correspondant à la base de donnée.
    '''
    
    cheeses = ["beaufort","bleu","brie","camembert","comte","morbier","roquefort","tomme_de_savoie"] 
 
    # Création d'un dictionnaire vide
    cheeseDict = {}
    
    # Pour chaque set
    for cheese in cheeses:
        # Récupérer le dictionnaire du set
        cheese_dict = loadCheeseImage(cheese, pathbdd);
        
        # Associer au dictionnaire vide la clé : set_name et la valeur : set_dict
        cheeseDict[cheese] = cheese_dict
    
    # retourner le dictionnaire
    return cheeseDict

dic = loadbdd("")
print(list(dic.keys()))
print(list(dic["brie"].keys()))
print(list(dic["brie"]["test"].keys()))




