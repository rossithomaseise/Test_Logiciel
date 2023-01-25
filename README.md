<h1> API Pastebin </h1>

<h4> Technologies utilisées : </h4>

python3, Flask, sqlite3, unittest

<h4>Architecture : </h4>  
  
user_server.py : API

functions_db.py : fonctions pour la base de donnée

test_fonctions_db.py : test du fichier functions_db.py

test_user_server.py : test API
  
texte.db : base de donnnée
  
texte.sql : code pour créer et remplir la base de donnée

requirements.txt : liste des packages python
  
.gitignore : fichiers ignoré par git
  
.pylintrc : fichier pour analyse static du code python

.ghtihub/workflows : contient les actions nose2, pylint et wheel_docker
  
Dockerfile : fichier pour mettre en Docker l'API

deploy.sh : script bash d'exécution du docker sur le serveur OVH

setup.py : fichier pour la création d'un fichier wheel

<h4> User Story :</h4>

Vous trouverez ici les différentes tâches réalisées :
  
US-1-creation_serveur (branche) : \
    --> US 1 : Création serveur (commit) \
    --> US 1 : Test création serveur (commit) avec : \
    curl -X GET 51.38.237.54:8882/isalive

US-2-creation-base_de_donnee (branche) : \
   --> US 2 : Création base de donnée (commit) \
   --> US 2 : Test création base de donnée (commit) \

US-3-creation_compte (branche) : \
  --> US 3 : Création compte (commit) \
  --> US 3 : Test création compte (commit) avec : \
  curl -X POST 51.38.237.54:8882/login -H "Content-Type: application/json" -d '{"username":"thamas", "password":"patatas"}'

US-4-ajout_texte (branche) : \
  --> US 4 : Vérification JSON et (si Utilisateur) vérification appartenance base de donnée (commit) \
  --> US 4 : Insertion texte et renvoie identifiant (commit) \
  --> US 4 : Test ajout texte (commit) avec : \
  curl -X POST 51.38.237.54:8882/add_txt -H "Content-Type: application/json" -d '{"username":"thamas", "password":"patatas","texte":"aller les patatas","privé":true}'\
  privé is a boolean -> True or False \
  Username et password ne sont pas nécessaire si le texte est public
  
US-5-recuperer_texte (branche) : \
  --> US 5 : Vérification JSON et (si privée) vérification appartenance base de donnée (commit) \
  --> US 5 : Récupération texte dans la base de donnée et Envoi (commit) \
  --> US 5 : Test récupérer texte (commit) avec : \
      curl -X GET 51.38.237.54:8882/get_text_private -H "Content-Type: application/json" -d '{"username":"thamas", "password":"patatas","id":4}' (si texte privé) \
      curl -X GET 51.38.237.54:8882/get_text_public -H "Content-Type: application/json" -d '{"id":6}' (si texte publique)

US-6-recuperer_historique_texte (branche) : \
  --> US 6 : Vérification JSON et appartenance base de donnée (commit) \
  --> US 6 : Récupération de tous les textes dans la base de donnée et Envoi (commit) \
  --> US 6 : Test récupérer historique texte (commit) avec : \
  curl -X GET 127.0.0.1:<port>/historique_texte -H "Content-Type: application/json" -d '{"username":"value1", "password":"value2"}'

<h4> Base de donnée : </h4> 

Utilisateur : id, identifiant, mot_de_passe

Texte : id, date_insertion, contenu, est_privee

Utilisateur_possede_texte : id_utilisateur, id_texte

<h4> Créer votre environnement python :</h4>

sudo apt install python3.8-venv

python3 -m venv env

source env/bin/activate

pipreqs --force . (installation des dépendances dans un fichier requirements.txt)

python3 -m pip install -r requirements.txt

<h4> Workflow Github : </h4>

git pull origin main

git checkout -b <nom-de-la-branche> 

(ou git checkout <nom-de-la-branche> si la branche a déjà été crée)
python3, Flask, sqlite3, unittest
git add <file.py> (ou git add *)

git status

git commit -m '<description-du-commit>'

git push

(ou git push origin <nom-de-la-branche> si vous êtes sur une autre branche)

pull requests dans l'interface graphique

// modification si besoin et re push

merge depuis l'interface graphique par une personne tierce

git branch -d <nom-de-la-branche> (pour détruire la branche : pas nécessaire)

<h4> Commandes Github utiles : </h4>

git branch (indique la branche actuelle)

git branch -a (liste les branches)

git checkout <branch> (pointe vers la branche indiquée)

git mv <ancien_file_name> <new_file_name> (renommer un fichier sur github)

git rm -rf clear <name_repository> (supprimer dossier sur github)

git rm <name_file> (supprimer un fichier sur github)
