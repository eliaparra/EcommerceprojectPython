from Resources.Locators import Locators
from Resources.PO.CustomersBack import CustomersBack
from Resources.PO.LoginBack import LoginBack
from Resources.PO.OrdersBack import OrdersBack
from Resources.TestData import TestData
from Tests.BaseTest import BaseTest


class Test_11(BaseTest):

    def setUp(self):
        super(Test_11, self).setUp()

    def runTest(self):
        self.loginBack = LoginBack(self.driver)
        self.loginBack.enter_text(Locators.LOGINBACK_USERNAME_INPUT, TestData.LOGINBACK_USERNAME)
        self.loginBack.enter_text(Locators.LOGINBACK_PASSWORD_INPUT, TestData.LOGINBACK_PASSWORD)
        self.loginBack.click(Locators.LOGINBACK_LOGIN_BUTTON)

        self.customersBack = CustomersBack(self.driver)
        self.customersBack.click(Locators.CUSTOMERSBACK_CLOSEALERT)
        self.customersBack.click(Locators.CUSTOMERSBACK_SALES_LINK)
        self.customersBack.click(Locators.CUSTOMERSBACK_ORDERS_LINK)

        self.ordersBack = OrdersBack(self.driver)
        self.ordersBack.setSelectorVisibleText(Locators.ORDERSBACK_STATUS_SELECTOR, "Canceled")
        self.ordersBack.click(Locators.ORDERSBACK_SEARCH_BUTTON)
        self.ordersBack.selectItem(Locators.ORDERSBACK_ORDERS_CHECKBOX, 0)
        self.ordersBack.setSelectorVisibleText(Locators.ORDERSBACK_ACTIONS_SELECTOR, TestData.ORDERSBACK_ACTIONS)
        self.ordersBack.click(Locators.ORDERSBACK_SUBMIT_BUTTON)
        self.assertIn(self.ordersBack.getText(Locators.ORDERSBACK_MSGS), TestData.ORDERSBACK_ERROR_MSG)
        self.ordersBack.setSelectorVisibleText(Locators.ORDERSBACK_STATUS_SELECTOR, "Complete")
        self.ordersBack.click(Locators.ORDERSBACK_SEARCH_BUTTON)
        self.ordersBack.selectItem(Locators.ORDERSBACK_ORDERS_CHECKBOX, 0)

    def tearDown(self):
        super(Test_11, self).tearDown()
