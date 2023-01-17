DROP TABLE IF EXISTS Utilisateur;
DROP TABLE IF EXISTS Texte;
DROP TABLE IF EXISTS Utilisateur_possede_texte; 

CREATE TABLE Utilisateur
(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  identifiant TEXT NOT NULL,
  mot_de_passe TEXT NOT NULL
);

CREATE TABLE Texte
(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  date_insertion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  contenu TEXT NOT NULL,
  est_privee BOOLEAN
);

CREATE TABLE Utilisateur_possede_texte
(
  id_utilisateur INTEGER,
  id_texte INTEGER,
  FOREIGN KEY (id_utilisateur) REFERENCES Utilisateur(id),
  FOREIGN KEY (id_texte) REFERENCES Texte(id)
);

INSERT INTO Utilisateur (identifiant,mot_de_passe) VALUES ("youss","Yellow");
INSERT INTO Utilisateur (identifiant,mot_de_passe) VALUES ("FredeRick","VeryS@fe14");

INSERT INTO Texte (contenu,est_privee) VALUES ("Une belle phrase",FALSE);
INSERT INTO Texte (contenu,est_privee) VALUES ("Une autre belle phrase",TRUE);
INSERT INTO Texte (contenu,est_privee) VALUES ("Es una linda frase",TRUE);

INSERT INTO Utilisateur_possede_texte (id_utilisateur,id_texte) SELECT (SELECT id FROM Utilisateur WHERE identifiant = "youss" AND mot_de_passe = "Yellow") as id_utilisateur,
(SELECT id FROM Texte WHERE contenu = "Une autre belle phrase") as id_texte;
INSERT INTO Utilisateur_possede_texte (id_utilisateur,id_texte) SELECT (SELECT id FROM Utilisateur WHERE identifiant = "youss" AND mot_de_passe = "Yellow") as id_utilisateur,
(SELECT id FROM Texte WHERE contenu = "Es una linda frase") as id_texte;
