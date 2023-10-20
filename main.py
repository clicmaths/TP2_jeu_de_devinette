#variables
import random

reponse = 'oui'


#programme
while reponse == "oui":#boucle pour rejouer
    def bornes():#fonctions pour choisir la borne minimale et maximale
        borne_minimale = int(input("entrez la borne minimale\n"))
        borne_maximale = int(input("entrez la borne maximale\n"))
        return(borne_minimale, borne_maximale)


    (borne_minimale, borne_maximale) = bornes() #définitions des variables
    nombre = random.randint(borne_minimale, borne_maximale) # importer une valeur aléatoire
    essai = int(input("entrez un chiffre de " + str(borne_minimale) + " à " + str(borne_maximale) + "\n"))
    nbessai = 0
    while essai != nombre:#boucle pour dire si l'utilisateur a écris la bonne réponse
        nbessai += 1
        if essai < nombre:
            print("Mauvaise réponse, le nombre est plus grand que essai\n entrez votre essai")

        elif essai > nombre:
            print("Mauvaise réponse, le nombre est plus petit que essai\n entrez votre essai")

        essai = int(input("entrez un chiffre de " + str(borne_minimale) + " à " + str(borne_maximale) + "\n"))

    nbessai += 1
    print("Bonne réponse vous avez deviné en "+ str(nbessai) +" essais")
    reponse = str(input("voulez-vous faire une autre partie?\n oui ou non\n"))


