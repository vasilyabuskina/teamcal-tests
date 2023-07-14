from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_element(self, locator):
        el = self.wait_for_element_visibility(locator)
        return self.driver.execute_script("arguments[0].scrollIntoView();", el)

    def accept_cookie(self):
        cookie_button = [By.ID, 'rcc-confirm-button']
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(cookie_button)).click()

    def fill(self, locator, value):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator)).send_keys(value)

    def select_from_dropdown(self, locator, value):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator)).send_keys(value)
        loc = [By.CLASS_NAME, 'select-search__select']
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(loc)).click()

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def wait_for_element_visibility(self, locator):
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return el

