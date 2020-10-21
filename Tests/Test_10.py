from Resources.PO.Account import Account
from Resources.PO.Cart import Cart
from Resources.PO.Checkout import Checkout
from Resources.PO.CreateAccount import CreateAccount
from Resources.PO.CustomersBack import CustomersBack
from Resources.PO.Home import HomePage
from Resources.PO.LoginBack import LoginBack
from Resources.PO.Mobile import Mobile
from Resources.PO.MyWishlist import MyWishlist
from Resources.PO.OrdersBack import OrdersBack
from Resources.PO.ShareWishlist import ShareWishlist
from Resources.PO.ThankYouPage import ThankYouPage
from Resources.PO.Tv import Tv
from Tests.BaseTest import BaseTest
from Resources.TestData import TestData
from Resources.Locators import Locators


class Test_10(BaseTest):

    def setUp(self):
        super(Test_10, self).setUp()

    def test_2(self):
        self.loginBack = LoginBack(self.driver)
        self.loginBack.enter_text(Locators.LOGINBACK_USERNAME_INPUT, TestData.LOGINBACK_USERNAME)
        self.loginBack.enter_text(Locators.LOGINBACK_PASSWORD_INPUT, TestData.LOGINBACK_PASSWORD)
        self.loginBack.click(Locators.LOGINBACK_LOGIN_BUTTON)

        self.customersBack = CustomersBack(self.driver)
        self.customersBack.click(Locators.CUSTOMERSBACK_CLOSEALERT)
        self.customersBack.click(Locators.CUSTOMERSBACK_SALES_LINK)
        self.customersBack.click(Locators.CUSTOMERSBACK_ORDERS_LINK)

        self.ordersBack = OrdersBack(self.driver)
        self.ordersBack.setSelectorVisibleText(Locators.ORDERSBACK_FORMAT_SELECTOR, TestData.ORDERSBACK_FORMAT)
        self.ordersBack.click(Locators.ORDERSBACK_EXPORT_BUTTON)

    def tearDown(self):
        super(Test_10, self).tearDown()