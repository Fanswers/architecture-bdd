# Présentation du projet

Ce projet consiste à vérifier une correlation entre les concerts réalisés en France par certains artistes et leur popularité spotify.

Pour cela nous avons scrappé les artistes les plus consultés qui effectuent un concerts en France sur le site [Infoconcert](https://www.infoconcert.com/).
Puis nous avons récuperé certaines informations depuis l'API Spotify.

## Installation

Prérequis:
 - Docker
 - Make (facultatif)

Pour installer le projet il vous suffit de taper la commande suivante à la racine du projet : <br>
Si Make d'installé (Makefile vous permet de manipuler vos conteneurs plus simplement):
````text 
make compose
````
Sinon :
````text 
docker-compose up -d
````

Maintenant que tous les conteneurs ont été créés et lancés vous pouvez acceder aux streamlit et à l'API:

API : http://127.0.0.1:5000/ <br>

Si les liens ne fonctionnent pas, aller voir dans les logs de Docker sur les conteneurs associés pour récuperer l'ip de l'api et modifier votre ip dans la ligne 13 du streamlit.py

Ouvrir un terminal à la racine du projet et executer la commande suivante:
````text 
streamlit run streamlit.py
````
Récuperer le lien fournit pour se connecter au streamlit

## Conclusion

Nous n'avons pas trouvé de corrélation entre les concerts qu'un artiste réalise et un gain de popularité conséquent après ce ce concert.<br>
Il y a deux raisons possibles à cette conclusion.
Les données que nous avons récupérées ne sont pas assez étalées dans le temps (seulement 1 semaine).
La deuxième raison est qu'il y a de fortes chances que les personnes allant voir des artistes en concert, soient déjà abonnées à ceux-ci.
