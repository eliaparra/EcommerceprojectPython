from Resources.Locators import Locators
from Resources.PO.CustomersBack import CustomersBack
from Resources.PO.EditReviewBack import EditReviewBack
from Resources.PO.Home import HomePage
from Resources.PO.LoginBack import LoginBack
from Resources.PO.Mobile import Mobile
from Resources.PO.PendingReviewsBack import PendingReviewsBack
from Resources.PO.Review import Review
from Resources.TestData import TestData
from Tests.BaseTest import BaseTest


class Test_12(BaseTest):

    def setUp(self):
        super(Test_12, self).setUp()

    def test_2(self):
        self.review = Review(self.driver)
        self.review.enter_text(Locators.REVIEWPAGE_REVIEW_FIELD, TestData.REVIEW_TEXT)
        self.review.enter_text(Locators.REVIEWPAGE_SUMMARY_FIELD, TestData.REVIEW_SUMMARY)
        self.review.enter_text(Locators.REVIEWPAGE_NICKNAME_FIELD, TestData.REVIEW_NICKNAME)
        self.review.click(Locators.REVIEWPAGE_SUBMIT_BUTTON)

        self.loginBack = LoginBack(self.driver)
        self.loginBack.enter_text(Locators.LOGINBACK_USERNAME_INPUT, TestData.LOGINBACK_USERNAME)
        self.loginBack.enter_text(Locators.LOGINBACK_PASSWORD_INPUT, TestData.LOGINBACK_PASSWORD)
        self.loginBack.click(Locators.LOGINBACK_LOGIN_BUTTON)

        self.customersBack = CustomersBack(self.driver)
        self.customersBack.click(Locators.CUSTOMERSBACK_CLOSEALERT)
        self.customersBack.click(Locators.CUSTOMERSBACK_CATALOG_LINK)
        self.customersBack.click(Locators.CUSTOMERSBACK_REVIEWS_AND_RATINGS)
        self.customersBack.click(Locators.CUSTOMERSBACK_CUSTOMER_REVIEWS)
        self.customersBack.click(Locators.CUSTOMERSBACK_PENDING_REVIEWS)

        self.pendingReviewsBack = PendingReviewsBack(self.driver)
        self.pendingReviewsBack.click(Locators.PENDINGREVIEWSBACK_REVIEW_ID)
        self.pendingReviewsBack.click(Locators.PENDINGREVIEWSBACK_EDIT_LINK)

        self.editReviewBack = EditReviewBack(self.driver)
        self.editReviewBack.setSelectorVisibleText(Locators.EDITREVIEWBACK_STATUS, "Approved")
        self.editReviewBack.click(Locators.EDITREVIEWBACK_SAVE_REVIEW)

        self.homePage = HomePage(self.driver)
        self.homePage.click(Locators.HOME_MOBILE_LINK)

        self.mobile = Mobile(self.driver)
        self.mobile.click(Locators.MOBILE_IMAGE_XPERIA)
        self.mobile.click(Locators.MOBILE_REVIEW_TAB)

        self.assertIn(self.mobile.getText(Locators.MOBILE_REVIEW_COMMENT).upper(), TestData.REVIEW_SUMMARY.upper())



    def tearDown(self):
        super(Test_12, self).tearDown()
