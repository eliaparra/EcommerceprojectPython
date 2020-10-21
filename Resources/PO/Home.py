from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Resources.PO.BasePage import BasePage
from Resources.TestData import TestData
from Resources.Locators import Locators


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL_FRONT)

    def getTitle(self):
        return self.getText(Locators.PAGE_TITLE)

    def clickMobile(self):
        self.click(Locators.HOME_MOBILE_LINK)


