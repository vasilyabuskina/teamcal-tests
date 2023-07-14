import pytest
from pages.schedule_page import SchedulePage


class TestSchedule:

    def test_click_on_teamcal_link_leads_to_teamcal_website(self, driver):
        schedule_page = SchedulePage(driver)
        schedule_page.click_on_teamcal_link()
        text = schedule_page.wait_for_element_visibility(schedule_page.request_demo_button).text
        assert text == "Meeting Scheduling"
