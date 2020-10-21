from Resources.Locators import Locators
from Resources.PO.Account import Account
from Resources.PO.Cart import Cart
from Resources.PO.Checkout import Checkout
from Resources.PO.Home import HomePage
from Resources.PO.Login import Login
from Resources.PO.MyWishlist import MyWishlist
from Resources.PO.ThankYouPage import ThankYouPage
from Resources.TestData import TestData
from Tests.BaseTest import BaseTest


class Test_6(BaseTest):

    def setUp(self):
        super(Test_6, self).setUp()

    def test_2(self):
        self.homePage = HomePage(self.driver)
        self.homePage.click(Locators.HOME_ACCOUNT_BUTTON)
        self.homePage.click(Locators.HOME_MYACCOUNT_LINK)

        self.loginPage = Login(self.driver)
        self.loginPage.enter_text(Locators.CREATEACCOUNT_EMAIL)
        self.loginPage.enter_text(Locators.CREATEACCOUNT_PASSWORD)
        self.loginPage.click(Locators.LOGIN_LOGIN_BUTTON)

        self.account = Account(self.driver)
        self.account.click(Locators.ACCOUNT_MYWISHLIST_LINK)

        self.mywishlist = MyWishlist(self.driver)
        self.mywishlist.click(Locators.MYWISHLIST_ADDTOCART_BUTTON)

        self.cart = Cart(self.driver)
        self.cart.setSelectorVisibleText(Locators.CART_COUNTRY_SELECTOR, TestData.CART_COUNTRY_SELECTOR)
        self.cart.setSelectorVisibleText(Locators.CART_REGION_SELECTOR, TestData.CART_STATE_SELECTOR)
        self.cart.enter_text(Locators.CART_ZIPCODE_INPUT, TestData.CART_ZIP)
        self.cart.click(Locators.CART_ESTIMATE_LINK)
        self.assertIn(Locators.CART_SHIPPINGCOST, TestData.CART_FLAT_RATE)
        self.cart.click(Locators.CART_RATE_RADIO)
        self.cart.click(Locators.CART_UPDATETOTAL_BUTTON)
        self.cart.click(Locators.CART_PROCEEDTOCHECKOUT_BUTTON)

        self.checkout = Checkout(self.driver)
        self.checkout.enter_text(Locators.CHECKOUT_FIRSTNAME, TestData.CREATEACCOUNT_FISTNAME)
        self.checkout.enter_text(Locators.CHECKOUT_LASTNAME, TestData.CREATEACCOUNT_LASTNAME)
        self.checkout.enter_text(Locators.CHECKOUT_ADDRESS, TestData.CHECKOUT_ADDRESS)
        self.checkout.enter_text(Locators.CHECKOUT_CITY, TestData.CHECKOUT_CITY)
        self.checkout.setSelectorVisibleText(Locators.CART_REGION_SELECTOR, TestData.CART_STATE_SELECTOR)
        self.checkout.enter_text(Locators.CHECKOUT_ZIP, TestData.CART_ZIP)
        self.checkout.setSelectorVisibleText(Locators.CART_COUNTRY_SELECTOR, TestData.CART_COUNTRY_SELECTOR)
        self.checkout.enter_text(Locators.CHECKOUT_TELEPHONE, TestData.CHECKOUT_TELEPHONE)
        self.checkout.click(Locators.CHECKOUT_BILLINGINFO_CONTINUEBUTTON)
        self.checkout.click(Locators.CHECKOUT_SHIPPINGMETHOD_CONTINUEBUTTON)
        self.checkout.click(Locators.CHECKOUT_CHECKMONEY_RADIO)
        self.checkout.click(Locators.CHECKOUT_PAYMENTINFORMATION_CONTINUEBUTTONA)
        self.checkout.click(Locators.CHECKOUT_PLACEORDER)

        self.thankpage = ThankYouPage(self.driver)
        self.assertNotEqual(self.thankpage.getText(Locators.THANKYPAGE_ORDERNUMBER), "")

    def tearDown(self):
        super(Test_6, self).tearDown()
