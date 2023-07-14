from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SchedulePage(BasePage):

    teamcal_link = [By.XPATH, "//a[(text()='Teamcal Ai Makers')]"]
    next_days_arrow = [By.XPATH, "//span[@id = 'next-days']"]
    request_demo_button = [By.XPATH, "//a[text()='Request Demo']"]

    first_date_button = [By.CSS_SELECTOR, ".timeslot-days:nth-child(1) a.date-selector"]
    second_date_button = [By.CSS_SELECTOR, ".timeslot-days:nth-child(2) a.date-selector"]

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def click_on_teamcal_link(self):
        self.wait_for_element_visibility(self.teamcal_link).click()

    def click_on_next_days_arrow(self):
        self.wait_for_element_visibility(self.next_days_arrow).click()
