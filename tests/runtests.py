import os
import sys
import unittest

BASE_PATH = os.path.abspath('..')
sys.path.insert(1, BASE_PATH)

from grupos import TestGrupos
from tests import *

def main():
    unittest.main()

if __name__ == '__main__':
    main()