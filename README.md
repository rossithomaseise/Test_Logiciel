<h1>Technologies utilisées : </h1>

python3, Flask, sqlite3, unittest

Commandes Github :

git add <file.py> (ou git add *)

git commit -m "blablabla"
git push origin US-blablabla
git pull-request (ou pull requests dans l'interface graphique)
// modification si besoin et re push
git checkout master
git pull origin master
git merge master US-blablabla (régler conflit)

Architecture (fichiers user_server.py et test_user_server.py et texte.db et texte.sql) :

US-1-creation_serveur (branche)
  --> US 1 : Création serveur (commit)
  --> US 1 : Test création serveur (commit) 
      curl -X GET 127.0.0.1:<port>/isalive

US-2-creation-base_de_donnee (branche)
   --> US 2 : Création base de donnée (commit)
   --> US 2 : Test création base de donnée (commit)

US-3-creation_compte (branche) (POST ...)
  --> US 3 : Création compte (commit)
  --> US 3 : Test création compte (commit)
      curl -v -X POST 127.0.0.1:9009/login -H "Content-Type: application/json"  -d '{"username":"value1", "password":"value2"}'

US-4-ajout_texte (branche) (POST ...)
  --> US 4 : Vérification JSON et (si Utilisateur) vérification appartenance base de donnée (commit)
  --> US 4 : Insertion texte dans la base de donnée et renvoie lien (commit)
  --> US 4 : Test ajout texte (commit)
      curl -v -X POST 127.0.0.1:9009/login -H "Content-Type: application/json"  -d '{"username":"value1", "password":"value2", "texte":"value3","privé":"value4"}'
  
US-5-recuperer_texte (branche)
  --> US 5 : Vérification JSON et (si privée) vérification appartenance base de donnée (commit)
  --> US 5 : Récupération texte dans la base de donnée et Envoi (commit)
  --> US 5 : Test récupérer texte (commit) 
      curl -X GET 127.0.0.1:<port>/id_texte -H "Content-Type: application/json" -d '{"username":"value1", "password":"value2"}' (si texte privé)
      curl -X GET 127.0.0.1:<port>/id_texte

US-6-recuperer_historique_texte (branche)
  --> US 6 : Vérification JSON et appartenance base de donnée (commit)curl -X GET 127.0.0.1:<port>/isalive
  --> US 6 : Récupération de tous les textes dans la base de donnée et Envoi (commit)
  --> US 6 : Test récupérer historique texte (commit)
      curl -X GET 127.0.0.1:<port>/historique_texte -H "Content-Type: application/json" -d '{"username":"value1", "password":"value2"}'

Base de donnée (texte.db) :

Utilisateur : id, identifiant, mot_de_passe

Texte : id, date_insertion, contenu, est_privee

Utilisateur_possede_texte : id_utilisateur, id_texte
