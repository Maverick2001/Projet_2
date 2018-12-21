"""Informations"""
#!/usr/bin/env python3
#-*- coding : utf-8 -*-

#licence : CC
#Author : Hery Rabenjarijaona TS3 ; Arthur Merle TS3 ; Renaud Jouen--Tachoire TS2

#Ce programme choisit un mot de 10 lettres dans un dictionnaire, et propose de jouer à le deviner en proposant des lettres


"""Importation de bibliothèques"""
import csv #cela va nous permettre de lire le fichier csv du dictionnaire
import random #on pourra utiliser une fonction qui permettra de choisir au hasard un mot


"""Ouverture du dictionnaire et transformation du dictionnaire en une liste de mots"""
dicoListe = [] #création d'une liste qui va conternir tous les mots du dictionnaire
mot10Lettres = [] #création d'une liste qui va contenir tous les mots ayant 10 lettres
separateur = " " #le séparateur utilisé dans le fichier est un espace

with open("DicoCSV.csv","r") as dico : #ouverture du fichier csv où les mots sont stockés // https://www.browserling.com/tools/newlines-to-spaces
    dicoLecture = csv.reader(dico, delimiter=separateur) #lecture du fichier
    for mots in dicoLecture :
        dicoListe = list(mots) #transformation de tous les mots sous forme de liste

#print(dicoListe)


"""Création d'une fonction qui enlève les accents du mot"""
def accent () :
    global motDico
    motDico = motDico.replace("é","e")
    motDico = motDico.replace("è","e")
    motDico = motDico.replace("ê","e")
    motDico = motDico.replace("ë","e")

    motDico = motDico.replace("ï","i")
    motDico = motDico.replace("î","i")

    motDico = motDico.replace("à","a")
    motDico = motDico.replace("â","a")
    motDico = motDico.replace("ä","a")

    motDico = motDico.replace("ù","u")
    motDico = motDico.replace("û","u")
    motDico = motDico.replace("ü","u")

    motDico = motDico.replace("ç","c")


"""Sélection d'un mot de 10 lettres au hasard """
for i in range (len(dicoListe)) : #on ajoute tous les mots de 10 lettres dans une liste
    if len(dicoListe[i]) == 10 : #si le nombre de lettres dans le mot est égal à 10
        mot10Lettres.append(dicoListe[i]) #alors on le rajoute à notre liste qui contient les mots à 10 lettres

motDico = random.choice(mot10Lettres) #choisit un mot au hasard dans toute la liste // https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list

motDicoAccent = motDico #on enregistre le mot avec pour le donner à la fin de la partie

#print(motDico)
accent() #on enlève les accents du mot
#print (motDico)

motDico = list(motDico.upper()) #transformation de chaque lettre du mot choisi sous forme de liste

#print (motDico)


"""Compteur de points"""
nombrePts = 8 #nombre de points au départ

def compteurPoints () : #création d'une fonction que soustrait un point pour chaque faute
    global nombrePts #pour modifier une variable dans une fonction, cette variable doit être définie comme globale // https://stackoverflow.com/questions/11904981/local-variable-referenced-before-assignment
    nombrePts = nombrePts -1 #on enlève 1 point pour une faute


"""Affichage des règles"""
print("LE JEU DU PENDU")
print("---Les règles---")
print("Le mot à deviner est un mot de 10 lettres")
print("Vous ne pouvez proposer qu'une seule lettre à la fois")
print("Vous partez avec 8 points, une faute vous enlevera un point")
print("Si vous voulez résoudre le mot en une fois, tapez le mot en entier")
print("Vous gagnez la partie si vous avez trouvé le mot","\n")


"""Affichage des 1ère et dernière lettres du mot choisi"""
for i in range (len(motDico)) :
    if i == 0 :
        print (motDico[0], end = " ") #ça affiche la première lettre ; "end =" permet de ne pas sauter de ligne à la fin de l'affichage de la lettre
    elif i == 9 :
        print(motDico[9], end = " ") #ça affiche la dernière lettre
    else :
        print ("_", end = " ") #le reste des lettres est caché

print("\n","Nombre d'essais = ",nombrePts) #on indique au joueur le nombre d'essais qu'il possède


"""Création d'une liste avec les lettres trouvées du joueur"""
motDevine = [motDico[0],"_","_","_","_","_","_","_","_",motDico[9]]

#print("\n",motDevine)


"""Création d'une liste qui va contenir toutes les lettres proposées par le joueur"""
lettreProp = []


"""Création d'une liste qui contient toutes les lettres possibles de proposer"""
lettrePermise = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


"""Commencement de la partie"""
while nombrePts > 0 : #tant que le joueur a encore des points, il continue de jouer

    lettre = input("nouvelle lettre ?") #l'utilisateur rentre une lettre
    lettre = lettre.upper() #cette lettre est convertie en majuscule


    if (lettre in lettrePermise and len(lettre) == 1) : #vérification que la lettre est admise


        """Vérification que la lettre que le joueur entre, n'a pas déjà été proposée"""
        if lettre in lettreProp : #la fonction "in" permet de savoir si la lettre est dans la liste // https://fr.wikibooks.org/wiki/Programmation_Python/Listes
            print("La lettre",lettre,"a déjà été proposée")

        else :

            """Indique les lettres déjà proposées"""
            lettreProp.append(lettre) #on ajoute la lettre entrée par le joueur dans la liste des lettres proposées

            if len(lettreProp) != 1 :
                print("Ces lettres ont déjà étaient proposées :","-".join(lettreProp))

            z = 1
            y = 0
            while z < 9 :
                if lettre == motDico[z] : #si le joueur trouve une lettre
                    motDevine[z]=lettre #le tiret est remplacé par la lettre
                    print(" ".join(motDevine))
                    y +=1 #si le joueur trouve une lettre, y != 0
                    #print(y)
                z+=1

            if (y >= 1 and nombrePts != 1 and motDico != motDevine):
                print("Bravo, il vous reste toujours",nombrePts,"chances")

            if (y >= 1 and nombrePts == 1 and motDico != motDevine) :
                    print("Bravo, il vous reste toujours",nombrePts,"chance")


            """Enlever un point au compteur """
            if y == 0  : #si le joueur n'a pas trouvé de lettre, y = 0, donc il perd un point
                compteurPoints() #on appel la fonction qui enlève un point
                print("La lettre",lettre,"n'existe pas dans le mot")

                if nombrePts > 1 : #indication du nombre d'essais restants
                    print("Il ne vous reste plus que", nombrePts,"chances")
                if nombrePts == 1 :
                    print("Il vous reste une dernière chance")
                if nombrePts == 0 : #si le joueur n'a plus de point, il a perdu
                    print("Vous avez perdu la partie, le mot était :",motDicoAccent) #on affiche le mot que l'utilisateur devait trouver
                    print("Retentez votre chance en appuyant sur Ctrl+F9 pour rejouer")
                    exit()

                print(" ".join(motDevine))


            """Si le joueur a gagné"""
            if motDico == motDevine : #si le joueur a trouvé le mot en entier, il a gagné
                print ("BRAVO, vous avez gagné, le mot était bien", motDicoAccent)
                print ("Appuyer sur Ctrl+F9 pour rejouer ! ")
                exit() #la partie est finie


        """Si le joueur décide de proposer le mot en entier"""
    elif len(lettre) > 1: #s'il y a plus d'une lettre cela signifie que le joueur propose un mot
        lettre = lettre.lower() #on convertit le mot en minuscule
        if lettre == motDicoAccent : #si le joueur a bon alors il a gagné
            print("Félicitations ! Vous avez trouvé le bon mot :",motDicoAccent)
            exit()
        else : #en revanche si ce n'est pas le bon mot, il perd un point
            print("Le mot proposé n'est pas le bon !")
            compteurPoints ()
            print("Vous avez perdu 1 point")
            print("Il vous reste plus que",nombrePts,"points")
            print(" ".join(motDevine))

    else :
        print("Ce caractère n'est pas valide, proposez une lettre")

