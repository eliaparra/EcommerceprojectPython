from Resources.PO.BasePage import BasePage
from Resources.Locators import Locators


class Mobile(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def getTitle(self):
        return self.getText(Locators.MOBILE_PAGE_TITLE)
