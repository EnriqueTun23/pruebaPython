# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 11:17:49 2022

@author: quiqu
"""

# !python -m unittest prueba_test

import unittest

import random

from prueba import conver_hash, parse_data


class TestPrueba(unittest.TestCase):
    
    
    
    # prueba unitaria que se hashea culquier resultado
    
    def test_hash(self):
        
        self.assertAlmostEqual(conver_hash(get_random_bytes()), str)
        self.assertAlmostEqual(conver_hash(5), str)
        self.assertAlmostEqual(conver_hash('data'), str)
    
    def test_parse_data(self):
        self.assertAlmostEqual(parse_data(get_object()), get_object())
        self.assertAlmostEqual(parse_data({}), dict)

        

def get_random_bytes():
    """
        fake data
    """
    size = random.randrange(1, 1000)

    for _ in range(size):
        yield random.getrandbits(8)

def get_object():
    """
        fake data
    """
    
    test_obj = {
            "name": 'ejemplo',
            "languages": [
                    {
                        "name": "ejemeplo"
                    },
            ],
            "region": 'info'
        }
    print(type(test_obj))
    return test_obj

if __name__ == '__main__':
    unittest.main()