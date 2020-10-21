import unittest

from Resources.PO.Home import HomePage
from Tests.BaseTest import BaseTest
from Resources.TestData import TestData
from Resources.Locators import Locators
from Resources.PO.Mobile import Mobile


class Test_1(BaseTest):

    def setUp(self):
        super(Test_1, self).setUp()

    def runTest(self):
        self.homePage = HomePage(self.driver)

        self.assertIn(TestData.HOME_TITLE, self.homePage.getTitle())
        self.homePage.clickMobile();

        self.mobilePage = Mobile(self.driver)
        self.assertIn(TestData.MOBILE_TITLE, self.mobilePage.getTitle())
        self.mobilePage.setSelectorVisibleText(Locators.DROPDOWN, "Name")
        self.assertIn(TestData.FIRST_PRODUCT_NAME, self.mobilePage.getItemText((Locators.PRODUCT_NAME), 0))

    def tearDown(self):
        super(Test_1, self).tearDown()


if __name__ == "__main__":
    unittest.main()
