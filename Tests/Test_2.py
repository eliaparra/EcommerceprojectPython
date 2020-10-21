from Resources.PO.Home import HomePage
from Tests.BaseTest import BaseTest
from Resources.TestData import TestData
from Resources.Locators import Locators
from Resources.PO.Mobile import Mobile
from Resources.PO.ProductPage import ProductPage


class Test_2(BaseTest):

    def setUp(self):
        super(Test_2, self).setUp()

    def test_2(self):
        self.homePage = HomePage(self.driver)


        self.homePage.clickMobile();

        self.mobilePage = Mobile(self.driver)
        XperiaPriceCategoryPage = self.mobilePage.getText(Locators.MOBILE_PRODUCT_PRICE)
        self.mobilePage.click(Locators.MOBILE_IMAGE_XPERIA)

        self.productPage = ProductPage(self.driver)
        XperiaPriceProductPage = self.productPage.getText(Locators.PP_MOBILE_PRICE)
        print(XperiaPriceCategoryPage)
        self.assertIn(XperiaPriceCategoryPage, XperiaPriceProductPage)

    def tearDown(self):
        super(Test_2, self).tearDown()