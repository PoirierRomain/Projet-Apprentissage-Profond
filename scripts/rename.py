import os

def renameImagesFile(mypath,prefixe,suffixe):
    """
    Renomme les fichiers dans un répertoire sous la forme prefixe_id_suffixe.extension .

    Args:
        mypath (str): Chemin du répertoire contenant les images à renommer.
        prefixe (str): Préfixe à ajouter au nom des images.
        suffixe (str): Suffixe à ajouter au nom des images.

    Returns:
        None
    """
    
    compteur = 0
    listImages = os.listdir(mypath)

    for image in listImages:
        # Récupérer l'extension du fichier
        nom_image, extension = os.path.splitext(image)
        
        # Vérifier si le fichier a une extension
        if extension == '':
            # Supprimer le fichier sans extension
            os.remove(os.path.join(mypath, image))
            continue

        # Construire le nouveau nom de fichier
        nouveau_nom = f"{prefixe}_{compteur}_{suffixe}{extension}"

        # Chemin actuel et nouveau chemin pour le fichier
        ancien_chemin = os.path.join(mypath, image)
        nouveau_chemin = os.path.join(mypath, nouveau_nom)

        # Renommer le fichier
        os.rename(ancien_chemin, nouveau_chemin)

        # Incrémenter le compteur
        compteur += 1
        
    
        
def renameCheese(pathbdd, name):
    """
    Renomme les fichiers de différentes catégories (surplus, test, train, validation)
    pour un type de fromage donné.

    Args:
        pathbdd (str): Chemin de la base de données contenant les fichiers à renommer.
        name (str): Nom du type de fromage.

    Returns:
        None
    """
    
    globalpath= pathbdd + name + "/"
    prefixe = name
    suffixes = ["surplus", "test", "train", "validation"]
    
    # Pour chaque fichier
    for suffixe in suffixes :
        
        # On rentre dans le fichier
        mypath = globalpath + suffixe + "/"
        
        # On renome tout
        renameImagesFile(mypath,prefixe,suffixe)

def renamebdd(pathbdd):
    """
    Renomme les fichiers de différentes catégories (surplus, test, train, validation)
    pour plusieurs types de fromages dans une base de données.

    Args:
        pathbdd (str): Chemin de la base de données contenant les fichiers à renommer.

    Returns:
        None
    """
    fromages = ["beaufort","bleu","brie","camembert","comte","morbier","roquefort","tomme_de_savoie"]

    for fromage in fromages:
        renameCheese(pathbdd, fromage)
        
renamebdd("./scripts/")
