import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_invalid_age(self):
        self.assertEqual(self.zoo.get_ticket_price(-4), "Age must be more than zero")

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(8), 50)
       
    def test_teen_ticket_price(self):
       self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_adult_ticket_price(self):
       self.assertEqual(self.zoo.get_ticket_price(40), 150)
    
    def test_senior_ticket_price(self):
       self.assertEqual(self.zoo.get_ticket_price(93), 100)

if __name__ == '__main__':
    unittest.main()