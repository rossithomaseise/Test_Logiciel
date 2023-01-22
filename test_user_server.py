"""  Test user server """
 
import unittest
import shlex
import time
import subprocess
import json
import requests
#import functions_db as db
#from user_server import get_text_public,login,is_alive,get_text_private

#db.init_db()

class TestUserSrv(unittest.TestCase):
    """ Class for unit test"""
    srv_sub_process = None

    TestPort = "8889"
    SrvAddr = "127.0.0.1"
    SrvUrl = "http://" + SrvAddr + ":" + TestPort

    def setUp(self):
        """ set up the server"""
        cmd = "flask --app user_server run --port="+self.TestPort
        args = shlex.split(cmd)
        self.srv_sub_process = subprocess.Popen(args) #pylint: disable=consider-using-with 
        time.sleep(1)

    def tearDown(self):
        """ kill the server"""
        print("killing subprocess user_server")
        self.srv_sub_process.kill()
        self.srv_sub_process.wait()

    # can be tested with :
    # $ curl -X GET 127.0.0.1:<port>/isalive
    def test_launch_srv(self):
        """ send a request to the server"""
        response = requests.get(self.SrvUrl+"/isalive", timeout=10)
        self.assertEqual(response.status_code,200)


    def test_login(self):
        response = requests.post(self.SrvUrl+"/login", timeout=10)
        self.assertEqual(response.status_code,400) #missing json payload
        response = requests.post(self.SrvUrl+"/login",json={"key": "value"}, timeout=10)
        self.assertEqual(response.status_code,400) # bad json payload
        response = requests.post(self.SrvUrl+"/login",json={"username":"youss", "password":"Yellow"}, timeout=10)
        self.assertEqual(response.status_code,200)

    def test_get_text_public(self):
        response = requests.get(self.SrvUrl+'/get_text_public',json={"id":3}, timeout=10)
        self.assertEqual(response.content.decode('ascii'),"Ceci est une phrase")

    def test_get_text_private(self):
        response = requests.get(self.SrvUrl+'/get_text_private',json={"id":2,"username":"youss", "password":"Yellow"}, timeout=10)
        self.assertEqual(response.content.decode('ascii'),"Es una linda frase")
        response = requests.get(self.SrvUrl+'/get_text_private',json={"id":3,"username":"youss", "password":"Yellow"}, timeout=10)
        self.assertEqual(response.content.decode('ascii'),"Ceci est une phrase")

    def test_historique_texte(self):
        response = requests.get(self.SrvUrl + "/historique_texte", json = {"username": "youss", "password": "Yellow"}, timeout = 10)
        answer = json.loads((response.content).decode("utf-8"))
        self.assertEqual((answer[0]),"Une autre belle phrase")
        self.assertEqual((answer[1]),"Es una linda frase")

    def test_add_text(self):
        response = requests.post(self.SrvUrl+"/add_txt", timeout=10)
        self.assertEqual(response.status_code,400) #missing json payload
        response = requests.post(self.SrvUrl+"/add_txt",json={"key": "value"}, timeout=10)
        self.assertEqual(response.status_code,400) # bad json payload
        payload = {"username":"value1", "password":"value2","texte":"blablabla","privé":False}
        response = requests.post(self.SrvUrl+"/login",json={"username":"value1", "password":"value2"}, timeout=10)
        response = requests.post(self.SrvUrl+"/add_txt",json=payload, timeout=10)
        self.assertEqual(response.status_code,200)
        payload = {"username":"value1", "password":"value2","texte":"12345789","privé":True}
        response = requests.post(self.SrvUrl+"/add_txt",json=payload, timeout=10)
        self.assertEqual(response.status_code,200)
        payload = {"texte":"blablabla","privé":False}
        response = requests.post(self.SrvUrl+"/add_txt",json=payload, timeout=10)
        self.assertEqual(response.status_code,200)
        payload = {"username":"value1", "password":"value2","texte":"blablabla","privé":False}
        response = requests.post(self.SrvUrl+"/add_txt",json=payload, timeout=10)
        self.assertEqual(response.status_code,200)
        payload={"username":"value1", "password":"fake_password","texte":"blablabla","privé":True}
        response = requests.post(self.SrvUrl+"/add_txt",json=payload, timeout=10)
        self.assertEqual(response.status_code,400)
        payload={"texte":"blablabla","privé":True}
        response = requests.post(self.SrvUrl+"/add_txt",json=payload, timeout=10)
        self.assertEqual(response.status_code,400)
        



if __name__ == '__main__':
    unittest.main()
