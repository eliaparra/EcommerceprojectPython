import time

from Resources.Locators import Locators
from Resources.PO.CustomersBack import CustomersBack
from Resources.PO.LoginBack import LoginBack
from Resources.PO.SalesInvoiceBack import SalesInvoiceBack
from Resources.TestData import TestData
from Tests.BaseTest import BaseTest


class Test_13(BaseTest):

    def setUp(self):
        super(Test_13, self).setUp()

    def test_2(self):
        self.loginback = LoginBack(self.driver)
        self.loginback.enter_text(Locators.LOGINBACK_USERNAME_INPUT, TestData.LOGINBACK_USERNAME)
        self.loginback.enter_text(Locators.LOGINBACK_PASSWORD_INPUT, TestData.LOGINBACK_PASSWORD)
        self.loginback.click(Locators.LOGINBACK_LOGIN_BUTTON)

        self.customersBack = CustomersBack(self.driver)
        self.customersBack.click(Locators.CUSTOMERSBACK_CLOSEALERT)
        self.customersBack.click(Locators.CUSTOMERSBACK_SALES_LINK)
        self.customersBack.click(Locators.CUSTOMERSBACK_INVOICES_LINK)

        self.salesinvoicesback = SalesInvoiceBack(self.driver)
        self.salesinvoicesback.click(Locators.INVOICESBACK_INVOICE_DATE)
        time.sleep(2.5)
        self.assertIn(self.salesinvoicesback.getText(Locators.INVOICESBACK_DATE_FIRST_ROW), TestData.INVOICESBACK_DATE1)
        self.salesinvoicesback.click(Locators.INVOICESBACK_INVOICE_DATE)
        time.sleep(2.5)
        self.assertIn(self.salesinvoicesback.getText(Locators.INVOICESBACK_DATE_FIRST_ROW), TestData.INVOICESBACK_DATE2)

    def tearDown(self):
        super(Test_13, self).tearDown()
