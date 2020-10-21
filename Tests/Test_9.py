from Resources.Locators import Locators
from Resources.PO.Cart import Cart
from Resources.PO.Home import HomePage
from Resources.PO.Mobile import Mobile
from Resources.TestData import TestData
from Tests.BaseTest import BaseTest


class Test_9(BaseTest):

    def setUp(self):
        super(Test_9, self).setUp()

    def test_2(self):
        self.homePage = HomePage(self.driver)
        self.homePage.click(Locators.HOME_MOBILE_LINK)

        self.mobile = Mobile(self.driver)
        self.mobile.click(Locators.MOBILE_ADDTOCART_IPHONE)

        self.cart = Cart(self.driver)
        pricebeforecoupon = self.cart.getText(Locators.CART_GRANDTOTAL)
        self.cart.enter_text(Locators.CART_COUPONCODE_INPUT, TestData.CART_COUPONCODE)
        priceaftercoupon = self.cart.getText(Locators.CART_GRANDTOTAL)
        self.assertEqual(float(pricebeforecoupon[1:]) * (1-TestData.CART_DISCOUNT), float(priceaftercoupon[1:]))


    def tearDown(self):
        super(Test_9, self).tearDown()