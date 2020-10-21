from Resources.Locators import Locators
from Resources.PO.AdvanceSearch import AdvanceSearch
from Resources.PO.AdvanceSearchResult import AdvanceSearchResult
from Resources.PO.Home import HomePage
from Resources.TestData import TestData
from Tests.BaseTest import BaseTest


class Test_14(BaseTest):

    def setUp(self):
        super(Test_14, self).setUp()

    def test_2(self):
        global p
        self.home = HomePage(self.driver)
        self.home.click(Locators.HOME_ADVANCE_SEARCH)

        self.advanceSearch = AdvanceSearch(self.driver)
        self.advanceSearch.enter_text(Locators.ADVANCESEARCH_PRICE, "0")
        self.advanceSearch.enter_text(Locators.ADVANCESEARCH_PRICETO, TestData.ADVANCESEARCH_PRICETO1)
        self.advanceSearch.click(Locators.ADVANCESEARCH_SEARCH_BUTTON)

        self.advanceSearchResult = AdvanceSearchResult(self.driver)
        lista1 = self.advanceSearch.getAllItems(Locators.ADVANCESEARCH_PRODUCT_NAME)
        lista2 = self.advanceSearchResult.getAllItems(Locators.ADVANCESEARCH_PRODUCT_PRICE)
        for p in range(len(lista1)):
            print(lista1[p].text)
        for q in range(len(lista2)):
            print(lista2[p].text)

        self.driver.back()

        self.advanceSearch.enter_text(Locators.ADVANCESEARCH_PRICE, TestData.ADVANCESEARCH_PRICE2)
        self.advanceSearch.enter_text(Locators.ADVANCESEARCH_PRICETO, TestData.ADVANCESEARCH_PRICETO2)
        self.advanceSearch.click(Locators.ADVANCESEARCH_SEARCH_BUTTON)
        lista1 = self.advanceSearch.getAllItems(Locators.ADVANCESEARCH_PRODUCT_NAME)
        lista2 = self.advanceSearchResult.getAllItems(Locators.ADVANCESEARCH_PRODUCT_PRICE)
        for p in range(len(lista1)):
            print(lista1[p].text)
        for q in range(len(lista2)):
            print(lista2[p].text)

    def tearDown(self):
        super(Test_14, self).tearDown()
