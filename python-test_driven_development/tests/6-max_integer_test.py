#!/usr/bin/python3
"""
Unittest for the function max_integer.
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Classe de tests pour la fonction max_integer"""

    # Test avec une liste normale
    def test_normal_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    # Test avec le maximum au milieu
    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    # Test avec un seul élément
    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    # Test avec une liste vide
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    # Test avec des nombres négatifs
    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    # Test avec des nombres positifs et négatifs
    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-10, 5, 3, -2]), 5)

    # Test avec des nombres identiques
    def test_same_numbers(self):
        self.assertEqual(max_integer([2, 2, 2]), 2)

