from Resources.PO.Account import Account
from Resources.PO.Cart import Cart
from Resources.PO.Checkout import Checkout
from Resources.PO.CreateAccount import CreateAccount
from Resources.PO.Home import HomePage
from Resources.PO.Mobile import Mobile
from Resources.PO.MyWishlist import MyWishlist
from Resources.PO.ShareWishlist import ShareWishlist
from Resources.PO.ThankYouPage import ThankYouPage
from Resources.PO.Tv import Tv
from Tests.BaseTest import BaseTest
from Resources.TestData import TestData
from Resources.Locators import Locators


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