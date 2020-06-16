import unittest
from utils.appiumtool import get_driver


class TestCaseLogin(unittest.TestCase):

    def test_01_login_failed(self):
        driver= get_driver()
