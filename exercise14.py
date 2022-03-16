# 11-1 and 11-2
import unittest

from city_functions import city_country


class CitiesTestCase(unittest.TestCase):

    def test_city_country(self):
        santiago_chile = city_country('santiago', 'chile')
        self.assertEqual(santiago_chile, 'Santiago, Chile')

    def test_city_country_population(self):
        santiago_chile = city_country('santiago', 'chile', population=5000000)
        self.assertEqual(santiago_chile, 'Santiago, Chile - population 5000000')


unittest.main()


# 11-3
import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.colin = Employee('colin', 'herbst', 100000)

    def test_give_default_raise(self):
        self.colin.give_raise()
        self.assertEqual(self.colin.salary, 105000)

    def test_give_custom_raise(self):
        self.colin.give_raise(10000)
        self.assertEqual(self.colin.salary, 110000)
        
        
unittest.main()
