import unittest
import adshopcart_methods as methods
import adshopcart_locators as locators


class AdShopCartPositiveTestCase(unittest.TestCase):

    @staticmethod
    def test_adshopcart():
        methods.setUp()
        methods.check_homepage()
        methods.fill_contact_infor()
        methods.create_new_user()
        methods.log_out()
        methods.log_in()
        methods.check_user_created()
        methods.delete_a_new_user()
        methods.check_user_deleted()
        methods.tearDown()
