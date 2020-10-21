from Resources.Locators import Locators
from Resources.PO.Account import Account
from Resources.PO.Home import HomePage
from Resources.PO.Login import Login
from Resources.PO.MyOrders import MyOrders
from Tests.BaseTest import BaseTest
from Resources.TestData import TestData


class Test_7(BaseTest):

    def setUp(self):
        super(Test_7, self).setUp()

    def runTest(self):
        self.homePage = HomePage(self.driver)
        self.homePage.click(Locators.HOME_ACCOUNT_BUTTON)
        self.homePage.click(Locators.HOME_MYACCOUNT_LINK)

        self.loginPage = Login(self.driver)
        self.loginPage.enter_text(Locators.LOGIN_EMAIL, TestData.CREATEACCOUNT_EMAIL)
        self.loginPage.enter_text(Locators.LOGIN_PASSWORD, TestData.CREATEACCOUNT_PASSWORD)
        self.loginPage.click(Locators.LOGIN_LOGIN_BUTTON)

        self.account = Account(self.driver)
        self.account.click(Locators.ACCOUNT_MYORDERS_LINK)

        self.myorders = MyOrders(self.driver)
        self.assertIn(self.myorders.getText(Locators.MYORDERS_STATUSFIRSTORDER), TestData.MYORDERS_PENDING_STATUS)
        self.myorders.click(Locators.MYORDERS_VIEWORDER_LINK)
        self.myorders.click(Locators.MYORDERS_FIRSTORDER)

    def tearDown(self):
        super(Test_7, self).tearDown()
