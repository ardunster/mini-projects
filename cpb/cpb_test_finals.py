x#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 18:31:58 2020

@author: adunster
"""

import unittest
import cpb_final
import cpb_final_2

class TestFinal1(unittest.TestCase):
    
    def test_is_prime(self):
        self.assertTrue(cpb_final.is_prime(3))
        self.assertTrue(cpb_final.is_prime(5))
        self.assertTrue(cpb_final.is_prime(7))
        self.assertTrue(cpb_final.is_prime(11))
        self.assertTrue(cpb_final.is_prime(109))
        self.assertTrue(cpb_final.is_prime(199))
        self.assertTrue(cpb_final.is_prime(277))
        self.assertFalse(cpb_final.is_prime(4))
        self.assertFalse(cpb_final.is_prime(25))
        self.assertFalse(cpb_final.is_prime(18))
        self.assertFalse(cpb_final.is_prime(110))
        self.assertFalse(cpb_final.is_prime(278))
        
    def test_next_prime(self):
        expected_result = 97
        act_result = next(cpb_final.next_prime(90))
        self.assertEqual(act_result, expected_result)
        expected_result2 = 277
        act_result2 = next(cpb_final.next_prime(275))
        self.assertEqual(act_result2, expected_result2)

class TestFinal2(unittest.TestCase):
    
    def test_factorize(self):
        factors_4432 = [2, 277, 2, 2, 2]
        self.assertEqual(cpb_final_2.factorize(4432).sort(), factors_4432.sort())
        factors_100 = [2, 2, 5, 5]
        self.assertEqual(cpb_final_2.factorize(100).sort(), factors_100.sort())
        factors_16384 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        self.assertEqual(cpb_final_2.factorize(16384).sort(), factors_16384.sort())



if __name__ == '__main__':
    unittest.main()
