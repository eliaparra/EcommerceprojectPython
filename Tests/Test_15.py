from Resources.Locators import Locators
from Resources.PO.CustomerInformationBack import CustomerInformationBack
from Resources.PO.CustomersBack import CustomersBack
from Resources.PO.LoginBack import LoginBack
from Resources.PO.ManageCustomersBack import ManageCustomersBack
from Resources.TestData import TestData
from Tests.BaseTest import BaseTest


class Test_15(BaseTest):

    def setUp(self):
        super(Test_15, self).setUp()

    def runTest(self):
        self.loginBack = LoginBack(self.driver)
        self.loginBack.enter_text(Locators.LOGINBACK_USERNAME_INPUT, TestData.LOGINBACK_USERNAME)
        self.loginBack.enter_text(Locators.LOGINBACK_PASSWORD_INPUT, TestData.LOGINBACK_PASSWORD)
        self.loginBack.click(Locators.LOGINBACK_LOGIN_BUTTON)

        self.customersBack = CustomersBack(self.driver)
        self.customersBack.click(Locators.CUSTOMERSBACK_CLOSEALERT)
        self.customersBack.click(Locators.CUSTOMERSBACK_CUSTOMERS_LINK)
        self.customersBack.click(Locators.CUSTOMERSBACK_MANAGECUSTOMERS_LINK)

        self.manageCustomersBack = ManageCustomersBack(self.driver)
        self.manageCustomersBack.click(Locators.MANAGECUSTOMERSBACK_FIRSTEDIT)

        self.customerInformationBack = CustomerInformationBack(self.driver)
        self.customerInformationBack.click(Locators.CUSTOMERINFOBACK_ACCOUNT_INFORMATION)
        self.assertFalse(self.customerInformationBack.is_enabled(Locators.CUSTOMERINFOBACK_WEBSITEASSOCIATED).is_enabled())
        self.assertFalse(self.customerInformationBack.is_enabled(Locators.CUSTOMERINFOBACK_CREATED_FROM).is_enabled())
        self.assertIs(self.customerInformationBack.getText(Locators.CUSTOMERINFOBACK_NEWPASS),"")

    def tearDown(self):
        super(Test_15, self).tearDown()
