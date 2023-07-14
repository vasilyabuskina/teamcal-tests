import pytest
from conftest import driver
from pages.schedule_page import SchedulePage


class TestSchedule:

    def test_click_on_next_days_arrow_shows_next_days(self, driver):
        schedule_page = SchedulePage(driver)
        schedule_page.click_on_next_days_arrow()
        # b1 = schedule_page.wait_for_element_visibility(schedule_page.first_date_button)
        # b2 = schedule_page.wait_for_element_visibility(schedule_page.second_date_button)
        # assert b1.text == b2.text

    def test_click_on_teamcal_link_leads_to_teamcal_website(self, driver):
        schedule_page = SchedulePage(driver)
        schedule_page.click_on_teamcal_link()
        schedule_page.switch_to_new_window()
        schedule_page.wait_for_element_visibility(schedule_page.request_demo_button)
        assert driver.current_url == 'https://teamcal.ai/'
