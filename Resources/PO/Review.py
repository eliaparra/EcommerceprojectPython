from Resources.PO.BasePage import BasePage
from Resources.TestData import TestData

class Review(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL_REVIEW)