from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by_locator)).click()

    def assert_element_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

    def enter_text(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(by_locator)).clear()
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(by_locator)).send_keys(text)

    def is_enabled(self, by_locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by_locator))

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by_locator))
        return bool(element)

    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def getText(self, by_locator):

        element = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by_locator))
        return element.text

    def setSelectorVisibleText(self, by_locator, textoption):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(by_locator))
        select = Select(element)
        select.select_by_visible_text(textoption)

    def getItemText(self, by_locator, index):
        lista = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_all_elements_located(by_locator))
        return lista[index].text

    def selectItem(self, by_locator, index):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_all_elements_located(by_locator))[index].click()
        #self.driver.click(lista[index])

    def getAllItems(self, by_locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_all_elements_located(by_locator))