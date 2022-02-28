import unittest
import methods
import adshopcart_locators as locators


class AdShopCartPositiveTestCase(unittest.TestCase):

    @staticmethod
    def test_adshopcart():
        methods.setUp()
        methods.tearDown()