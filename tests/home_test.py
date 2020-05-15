import unittest
from pandas import DataFrame
from my_lambdata.home_class import Home


# OBJECTIVE: test the price_sq_ft() function from the my_lambdata/home_class.py file
class TestHome(unittest.TestCase):
    def test_price_sq_ft(self):
        # expect that it is a positive number
        house = Home('House', 3000, 'Dallas', 300000)
        price = Home.price_sq_ft(house)
        self.assertEqual(price, 100)
        
if __name__ == "__main__":
    unittest.main()