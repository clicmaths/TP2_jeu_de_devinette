#variables
import random

reponse = 'oui'


#boucle pour rejouer
while reponse == "oui":
    def bornes():#fonctions pour choisir la borne minimale et maximale
        borne_minimale = int(input("entrez la borne minimale\n"))
        borne_maximale = int(input("entrez la borne maximale\n"))
        return(borne_minimale, borne_maximale)

    #définitions des variables
    (borne_minimale, borne_maximale) = bornes() 
    # importer une valeur aléatoire
    nombre = random.randint(borne_minimale, borne_maximale) 
    essai = int(input("entrez un chiffre de " + str(borne_minimale) + " à " + str(borne_maximale) + "\n"))
    nbessai = 0
    #boucle pour dire si l'utilisateur a écris la bonne réponse
    while essai != nombre:
        nbessai += 1
        if essai < nombre:
            print("Mauvaise réponse, le nombre est plus grand que essai\n entrez votre essai")

        elif essai > nombre:
            print("Mauvaise réponse, le nombre est plus petit que essai\n entrez votre essai")

        essai = int(input("entrez un chiffre de " + str(borne_minimale) + " à " + str(borne_maximale) + "\n"))

    nbessai += 1
    print("Bonne réponse vous avez deviné en "+ str(nbessai) +" essais")
    reponse = str(input("voulez-vous faire une autre partie?\n oui ou non\n"))


