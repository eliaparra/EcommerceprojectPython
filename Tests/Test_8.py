from Resources.Locators import Locators
from Resources.PO.Account import Account
from Resources.PO.Cart import Cart
from Resources.PO.Checkout import Checkout
from Resources.PO.Home import HomePage
from Resources.PO.Login import Login
from Resources.PO.MyOrders import MyOrders
from Resources.PO.ThankYouPage import ThankYouPage
from Tests.BaseTest import BaseTest
from Resources.TestData import TestData


class Test_8(BaseTest):

    def setUp(self):
        super(Test_8, self).setUp()

    def test_2(self):
        self.homePage = HomePage(self.driver)
        self.homePage.click(Locators.HOME_ACCOUNT_BUTTON)
        self.homePage.click(Locators.HOME_MYACCOUNT_LINK)

        self.loginPage = Login(self.driver)
        self.loginPage.enter_text(Locators.LOGIN_EMAIL, TestData.CREATEACCOUNT_EMAIL)
        self.loginPage.enter_text(Locators.LOGIN_PASSWORD, TestData.CREATEACCOUNT_PASSWORD)
        self.loginPage.click(Locators.LOGIN_LOGIN_BUTTON)

        self.account = Account(self.driver)
        self.account.click(Locators.ACCOUNT_REORDER_LINK)

        self.cart = Cart(self.driver)
        preGrandTotal = self.cart.getText(Locators.CART_GRANDTOTAL)
        self.cart.enter_text(Locators.CART_INPUT_QTY, TestData.CART_QTY)
        self.cart.click(Locators.CART_UPDATE_QTY)
        postGrandTotal = self.cart.getText(Locators.CART_GRANDTOTAL)
        self.assertNotEqual(preGrandTotal,postGrandTotal)
        self.cart.click(Locators.CART_PROCEEDTOCHECKOUT_BUTTON)

        self.checkout = Checkout(self.driver)
        self.checkout.click(Locators.CHECKOUT_BILLINGINFO_CONTINUEBUTTON)
        self.checkout.click(Locators.CHECKOUT_SHIPPINGMETHOD_CONTINUEBUTTON)
        self.checkout.click(Locators.CHECKOUT_CHECKMONEY_RADIO)
        self.checkout.click(Locators.CHECKOUT_PAYMENTINFORMATION_CONTINUEBUTTON)
        self.checkout.click(Locators.CHECKOUT_PLACEORDER)

        self.typ = ThankYouPage(self.driver)
        orderNumber = self.typ.getText(Locators.THANKYPAGE_ORDERNUMBER)
        self.assertIsNot(orderNumber, "")

    def tearDown(self):
        super(Test_8, self).tearDown()
