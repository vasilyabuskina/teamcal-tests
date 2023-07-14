from selenium.webdriver.common.by import By

class SchedulePage:

    teamcal_link = [By.XPATH, "//a[(text()='Teamcal Ai Makers')]"]
    request_demo_button = [By.XPATH, "//a[text()='Request Demo']"]

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def click_on_teamcal_link(self):
        self.wait_for_element_visibility(self.teamcal_link).click()
