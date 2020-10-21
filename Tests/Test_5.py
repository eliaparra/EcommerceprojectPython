from Resources.PO.Account import Account
from Resources.PO.CreateAccount import CreateAccount
from Resources.PO.Home import HomePage
from Resources.PO.Login import Login
from Resources.PO.MyWishlist import MyWishlist
from Resources.PO.ShareWishlist import ShareWishlist
from Resources.PO.Tv import Tv
from Tests.BaseTest import BaseTest
from Resources.TestData import TestData
from Resources.Locators import Locators


class Test_5(BaseTest):

    def setUp(self):
        super(Test_5, self).setUp()

    def test_2(self):
        self.homePage = HomePage(self.driver)
        self.homePage.click(Locators.HOME_ACCOUNT_BUTTON)
        self.homePage.click(Locators.HOME_MYACCOUNT_LINK)

        self.loginPage = Login(self.driver)
        self.loginPage.click(Locators.LOGIN_CREATEACCOUNT_BUTTON)

        self.createAccount = CreateAccount(self.driver)
        self.createAccount.enter_text(Locators.CREATEACCOUNT_FIRSTNAME, TestData.CREATEACCOUNT_FISTNAME)
        self.createAccount.enter_text(Locators.CREATEACCOUNT_MIDDLENAME, TestData.CREATEACCOUNT_MIDDLENAME)
        self.createAccount.enter_text(Locators.CREATEACCOUNT_LASTNAME, TestData.CREATEACCOUNT_LASTNAME)
        self.createAccount.enter_text(Locators.CREATEACCOUNT_EMAIL, TestData.CREATEACCOUNT_EMAIL)
        self.createAccount.enter_text(Locators.CREATEACCOUNT_PASSWORD, TestData.CREATEACCOUNT_PASSWORD)
        self.createAccount.enter_text(Locators.CREATEACCOUNT_CONFIRMPASSWORD, TestData.CREATEACCOUNT_PASSWORD)
        self.createAccount.click(Locators.CREATEACCOUNT_REGISTER_BUTTON)
        self.assertIn(self.createAccount.getText(Locators.ACCOUNT_MSG), TestData.ACCOUNT_MSG)

        self.account = Account(self.driver)
        self.account.click(Locators.ACCOUNT_TV_LINK)

        self.tv = Tv(self.driver)
        self.tv.click(Locators.TV_WISHLIST_LGLCD_LINK)

        self.mywishlist = MyWishlist(self.driver)
        self.mywishlist.click(Locators.MYWISHLIST_SHAREWISHLIST_BUTTON)

        self.sharemywishlist = ShareWishlist(self.driver)
        self.sharemywishlist.enter_text(Locators.SHAREWISHLIST_EMAIL, TestData.SHAREWISHLIST_EMAIL)
        self.sharemywishlist.click(Locators.SHAREWISHLIST_BUTTON)
        self.assertIn(self.mywishlist.getText(Locators.MYWISHLIST_MSG), TestData.SHAREWISHLIST_MSG)

    def tearDown(self):
        super(Test_5, self).tearDown()
