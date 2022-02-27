import unittest
import adshopcart_methods as methods
import adshopcart_locators as locators


class AdShopCartPositiveTestCase(unittest.TestCase):


    @staticmethod
    def test_adshopcart():
        methods.setUp()
        methods.tearDown()
