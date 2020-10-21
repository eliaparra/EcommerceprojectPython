from Resources.PO.Home import HomePage
from Tests.BaseTest import BaseTest
from Resources.TestData import TestData
from Resources.Locators import Locators
from Resources.PO.Mobile import Mobile



class Test_4(BaseTest):

    def setUp(self):
        super(Test_4, self).setUp()

    def test_2(self):


        self.homePage = HomePage(self.driver)

        self.homePage.clickMobile();

        self.mobilePage = Mobile(self.driver)
        self.mobilePage.click(Locators.MOBILE_ADDTOCOMPARE_XPERIA)
        self.mobilePage.click(Locators.MOBILE_ADDTOCOMPARE_IPHONE)
        self.mobilePage.click(Locators.MOBILE_COMPARE_BUTTON)
        allWindows = self.driver.window_handles

        self.driver.switch_to_window(allWindows[1])
        self.assertIn(TestData.COMPARE_POPUP_HEADING.lower(), self.driver.find_element_by_tag_name("h1").text.lower())
        self.assertIn(self.driver.find_element_by_xpath("//*[@id='product_comparison']/tbody[1]/tr[1]/td[1]/h2/a").text,"SONY XPERIA")
        self.assertIn(self.driver.find_element_by_xpath("//*[@id='product_comparison']/tbody[1]/tr[1]/td[2]/h2/a").text,"IPHONE")


    def tearDown(self):
        super(Test_4, self).tearDown()