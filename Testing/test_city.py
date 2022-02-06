import unittest
from city_functions import city_country 

class TestCityFunctions(unittest.TestCase):
    def test_city_country(self):
        formatted = city_country("Cascavel", "Brasil")
        self.assertEqual(formatted, "Cascavel, Brasil")

unittest.main()
