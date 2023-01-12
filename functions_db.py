import sqlite3
import random

conn = sqlite3.connect('Textes.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

def get_users():
    c.execute("SELECT * FROM Utilisateur;")
    ligne = c.fetchall()
    res = [[ligne[j][i] for i in range(3)] for j in range (len(ligne))]
    return res

def get_user(id):
    c.execute("SELECT * FROM Utilisateur WHERE id = (?);",[id])
    ligne = c.fetchone()
    return [ligne[i] for i in range(3)]

def add_user(username,password):
    c.execute("INSERT INTO Utilisateur (identifiant,mot_de_passe) VALUES (?,?) ;",[username,password])
    ligne = c.fetchone()
    conn.commit()

def get_text(id):
    c.execute("SELECT contenu FROM Texte WHERE id = (?);",[id])
    ligne = c.fetchone()
    return ligne[0]

def get_texts():
    c.execute("SELECT contenu FROM Texte")
    ligne = c.fetchall()
    return [ligne[i][0] for i in range(len(ligne))]

def add_text_public(text_content,is_private):
    c.execute("INSERT INTO Texte (contenu,est_privee) VALUES (?,?) ;",[text_content,is_private])
    ligne = c.fetchone()
    conn.commit()

def add_text_private(text_content,username,password):
    add_text_public(text_content,True)
    c.execute("SELECT id FROM Texte ORDER BY id DESC LIMIT 1")
    id_text = c.fetchone()[0]
    c.execute("SELECT id FROM Utilisateur WHERE identifiant = (?) AND mot_de_passe = (?)", [username,password])
    id_user = c.fetchone()[0]
    c.execute("INSERT INTO Utilisateur_possede_texte VALUES (?,?)", [id_user,id_text])
    ligne = c.fetchone()
    conn.commit()


if __name__ == "__main__":

    add_user("JulienGenty","Mo!td$p@sse")
    add_text_private("def(): fonction","JulienGenty","Mo!td$p@sse")
