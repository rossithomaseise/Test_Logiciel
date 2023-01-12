"""  Test user server """
 
import unittest
import shlex
import time
import subprocess
import requests

class TestUserSrv(unittest.TestCase):
    """ Class for unit test"""
    srv_sub_process = None

    TestPort = "8888"
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
        response = requests.post(self.SrvUrl+"/login",json={"username":"value1", "password":"value2"}, timeout=10)
        self.assertEqual(response.status_code,200)

if __name__ == '__main__':
    unittest.main()
