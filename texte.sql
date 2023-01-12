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
SELECT * FROM Utilisateur;

INSERT INTO Texte (contenu,est_privee) VALUES ("Une belle phrase",FALSE);
SELECT * FROM Texte;

INSERT INTO Utilisateur_possede_texte (id_utilisateur,id_texte) SELECT (SELECT id FROM Utilisateur WHERE identifiant = "string" AND mot_de_passe = "tanga") as id_utilisateur,
(SELECT id FROM Texte WHERE contenu = "Mon string est tendu" AND est_privee = FALSE) as id_texte;
SELECT * FROM Utilisateur_possede_texte;
