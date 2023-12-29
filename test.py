#!/usr/bin/env python3

import sys
import unittest
from helpers import *
from vertexCover import *
from main import *


class MyTest(unittest.TestCase):

    def test_parse_input(self):
        line = 'add "a" (2,3) (4,5)'
        cmd, street_name, vertices = parse_input(line)
        self.assertEqual(cmd, 'add')
        self.assertEqual(street_name, 'a')
        self.assertEqual(vertices, ['(2,3)', '(4,5)'])


if __name__ == '__main__':
    unittest.main()
