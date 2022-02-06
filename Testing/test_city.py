import unittest
from city_functions import city_country 

class TestCityFunctions(unittest.TestCase):
    def test_city_country_population(self):
        formatted = city_country("cascavel", "brasil", 300000)
        self.assertEqual(formatted, "Cascavel, Brasil - população 300000")
    def test_city_country(self):
        formatted = city_country("cascavel", "brasil")
        self.assertEqual(formatted, "Cascavel, Brasil")

unittest.main()
