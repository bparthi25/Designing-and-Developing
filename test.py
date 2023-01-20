import unittest
from datetime import datetime
from option_1 import *
from option_2 import *
from option_3 import *
from option_4 import *
from option_5 import *
from support import *

class Test(unittest.TestCase):
    def test_connect_db(self):
        test_db = connect_db("test.db")
        self.assertIsInstance(test_db, sqlite3.Connection)

    def test_query_option_1(self):
        connect_db("test.db")
    	/////code missing/////
    
    def test_query_option_2(self):
        connect_db("test.db")
	/////code missing/////
        

    def test_query_option_3(self):
        connect_db("test.db")
        /////code missing/////

    def test_query_option_4(self):
        connect_db("test.db")
      	/////code missing/////
    
    def test_query_option_5(self):
        connect_db("test.db")
	/////code missing/////
       