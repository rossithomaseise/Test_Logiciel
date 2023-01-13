"""  Test database functions"""
 
import unittest

from functions_db import add_user,get_user,get_users,get_texts_user,add_text,add_text_private,get_text,get_texts



class TestDBFunctions(unittest.TestCase):
    """ Class for unit test"""
    def test_get_user_db(self):
        user=get_user(1)
        self.assertEqual(user[1],"youss")
        self.assertEqual(user[2],"Yellow")
        user=get_user(2)
        self.assertEqual(user[1],"FredeRick")
        self.assertEqual(user[2],"VeryS@fe14")
        
    def test_add_user_db(self):
        id_user=add_user("JulienGenty","Mo!td$p@sse")
        user=get_user(id_user)
        self.assertEqual(user[1],"JulienGenty")
        self.assertEqual(user[2],"Mo!td$p@sse")

        id_user=add_user("Mai","HerPAssw0rd")
        user=get_user(id_user)
        self.assertEqual(user[1],"Mai")
        self.assertEqual(user[2],"HerPAssw0rd")

    def test_get_users_db(self):
        users=get_users()
        self.assertEqual(users[1][1],"FredeRick")
        self.assertEqual(users[-1][1],"Mai")
        self.assertEqual(users[-2][1],"JulienGenty")
        self.assertEqual(users[-2][2],"Mo!td$p@sse")

    def test_get_text_db(self):
        text = get_text(1);
        self.assertEqual(text,"Une belle phrase")
        text = get_text(2);
        self.assertEqual(text,"Une autre belle phrase")

    def test_add_text_db(self):
        id_text = add_text("Es ist ein schône Satz",False)
        text = get_text(id_text)
        self.assertEqual(text,"Es ist ein schône Satz")
        id_text = add_text("Nous sommes le 12 Janvier 2023",False)
        text = get_text(id_text)
        self.assertEqual(text,"Nous sommes le 12 Janvier 2023")

    def test_add_text_private_db(self):

        add_user("youss","Yellow")
        id_text = add_text_private("Es ist ein schône Satz","youss","Yellow")
        text = get_text(id_text)
        self.assertEqual(text,"Es ist ein schône Satz")
        add_user("FredeRick","VeryS@fe14")

        id_text = add_text_private("Fredosaure","FredeRick","VeryS@fe14")
        text = get_text(id_text)
        self.assertEqual(text,"Fredosaure")

    def test_get_texts_db(self):
        list_text = get_texts()
        self.assertEqual(list_text[0],"Une belle phrase")
        self.assertEqual(list_text[1],"Une autre belle phrase")

    def test_get_texts_user_db(self):
        texts=get_texts_user("youss","Yellow")
        self.assertEqual(texts[0],"Une autre belle phrase")
        self.assertEqual(texts[1],"Es una linda frase")
        

if __name__ == '__main__':
    unittest.main()
