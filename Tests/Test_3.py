from Resources.PO.Cart import Cart
from Resources.PO.Home import HomePage
from Tests.BaseTest import BaseTest
from Resources.TestData import TestData
from Resources.Locators import Locators
from Resources.PO.Mobile import Mobile
from Resources.PO.ProductPage import ProductPage


class Test_3(BaseTest):

    def setUp(self):
        super(Test_3, self).setUp()

    def test_2(self):
        self.homePage = HomePage(self.driver)


        self.homePage.clickMobile();

        self.mobilePage = Mobile(self.driver)
        self.mobilePage.click(Locators.MOBILE_ADDTOCART_XPERIA)

        self.cartPage = Cart(self.driver)
        self.cartPage.enter_text(Locators.CART_INPUT_QTY,TestData.CART_QTY)
        self.cartPage.click(Locators.CART_UPDATE_QTY)
        self.assertIn(TestData.CART_MAXIMUMQTY_ALLOWED,self.cartPage.getText(Locators.CART_ERROR_MSG))
        
        self.cartPage.click(Locators.CART_EMPTYCART_BUTTON)
        self.assertIn(TestData.CART_CARTEMPTY,self.cartPage.getText(Locators.CART_EMPTYCART_MST))

    def tearDown(self):
        super(Test_3, self).tearDown()