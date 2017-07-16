import os
import sys
import unittest

BASE_PATH = os.path.abspath('..')
sys.path.insert(1, BASE_PATH)


from robots import *
from encuentros import *
from grupos import *
from ganadores import *
#from tests import *

def main():
    unittest.main()

if __name__ == '__main__':
    main()
    