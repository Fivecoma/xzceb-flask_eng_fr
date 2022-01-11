import unittest

from translator import frenchToEnglish, englishToFrench

class TestF2E(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Bonjour')
    def test2(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

class TestE2F(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(englishToFrench('Hello'), 'Hello')
    def test2(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

unittest.main()