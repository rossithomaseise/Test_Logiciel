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

