import sqlite3
conn = sqlite3.connect('Textes.db',check_same_thread=False)
conn.row_factory = sqlite3.Row
c = conn.cursor()

def init_db():
    

    with open('texte.sql', 'r',encoding="utf-8") as sql_file:
        sql_script = sql_file.read()

    c.executescript(sql_script)

    c.execute('INSERT INTO Utilisateur (identifiant,mot_de_passe) VALUES ("youss","Yellow")')
    conn.commit()
    c.execute('INSERT INTO Utilisateur (identifiant,mot_de_passe) VALUES ("FredeRick","VeryS@fe14")')
    conn.commit()
    c.execute('INSERT INTO Texte (contenu,est_privee) VALUES ("Une autre belle phrase",TRUE)')
    conn.commit()
    c.execute('INSERT INTO Texte (contenu,est_privee) VALUES ("Es una linda frase",TRUE)')
    conn.commit()
    c.execute('INSERT INTO Texte (contenu,est_privee) VALUES ("Ceci est une phrase",FALSE)')
    conn.commit()
    c.execute('INSERT INTO Utilisateur_possede_texte (id_utilisateur,id_texte) SELECT (SELECT id FROM Utilisateur WHERE identifiant = "youss" \
    AND mot_de_passe = "Yellow") as id_utilisateur,(SELECT id FROM Texte WHERE contenu = "Une autre belle phrase") as id_texte')
    conn.commit()
    c.execute('INSERT INTO Utilisateur_possede_texte (id_utilisateur,id_texte) SELECT (SELECT id FROM Utilisateur WHERE identifiant = "youss" AND mot_de_passe = "Yellow") as id_utilisateur,\
    (SELECT id FROM Texte WHERE contenu = "Es una linda frase") as id_texte')
    conn.commit()



def valid_user(username,password):
    users_list=c.execute('SELECT * FROM  Utilisateur')
    if(any(raw['identifiant'] == username and raw['mot_de_passe'] == password for raw in users_list)):
        return True
    return False


def add_user(username,password):
    c.execute("INSERT INTO Utilisateur (identifiant,mot_de_passe) VALUES (?,?) ;",[username,password])
    conn.commit()
    #Récupérer l'id de l'utilisateur qu'on vient d'ajouter
    c.execute("SELECT id FROM Utilisateur WHERE identifiant=(?) and mot_de_passe=(?)",[username,password])
    id_user=c.fetchone()[0]
    return id_user

def get_user(user_id):
    c.execute("SELECT * FROM Utilisateur WHERE id = (?);",[user_id])
    ligne = c.fetchone()
    return [ligne[i] for i in range(3)]

def get_users():
    c.execute("SELECT * FROM Utilisateur;")
    ligne = c.fetchall()
    res = [[ligne[j][i] for i in range(3)] for j in range (len(ligne))]
    return res

def get_text_public(text_id):
    c.execute("SELECT * FROM Texte WHERE id = (?);",[text_id])
    ligne = c.fetchone()
    if(ligne[3]==True):
        return "Error: trying to access a private text"
    return ligne[2]

def get_text_private(text_id,username,password):

    if(valid_user(username,password) == False):
        return "Invalid user"
    c.execute("SELECT contenu FROM Texte WHERE id = (?);",[text_id])
    ligne = c.fetchone()
    return ligne[0]

def get_texts_user(username,password):
    c.execute("SELECT id FROM Utilisateur WHERE identifiant=(?) and mot_de_passe=(?)",[username,password])
    id_user=c.fetchone()[0]
    c.execute("SELECT * FROM Utilisateur_possede_texte WHERE id_utilisateur=(?)",[id_user])
    table=c.fetchall()
    texts = [get_text_private(table[i][1],username,password) for i in range(len(table))]
    return texts


def get_texts():
    c.execute("SELECT contenu FROM Texte")
    ligne = c.fetchall()
    return [ligne[i][0] for i in range(len(ligne))]
    
def add_text(text_content,is_private):
    c.execute("INSERT INTO Texte (contenu,est_privee) VALUES (?,?) ;",[text_content,is_private])
    conn.commit()

    #Récupérer l'id de l'utilisateur qu'on vient d'ajouter
    c.execute("SELECT id FROM Texte WHERE contenu=(?)",[text_content])
    id_text=c.fetchone()[0]
    return id_text
  

def add_text_private(text_content,username,password):
    add_text(text_content,True)
    c.execute("SELECT id FROM Texte ORDER BY id DESC LIMIT 1")
    id_text = c.fetchone()[0]
    c.execute("SELECT id FROM Utilisateur WHERE identifiant = (?) AND mot_de_passe = (?)", [username,password])
    try:
        id_user = c.fetchone()[0]
        c.execute("INSERT INTO Utilisateur_possede_texte VALUES (?,?)", [id_user,id_text])
        conn.commit()
        return id_text
    except TypeError:
        print("L'utilisateur n'existe pas")
        return False