import pytest
from selenium.webdriver import Chrome
from pages.login.login_page_actions import LoginPageActions
from pages.dashboard.dashboard_page_actions import DashboardPageActions
from pages.monitors.monitors_page_actions import MonitorPageActions
import config.config as config
from pytest_check import check
from datetime import date, timedelta


class TestSmileyMonitor:

    @pytest.fixture(autouse=True)
    def browser(self):
        driver = Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        yield driver
        driver.quit()

    @pytest.fixture()
    def setup(self, browser):
        """
        Login and open Monitors tab - setup for all tests
        """
        self.login_page_actions = LoginPageActions(browser)
        self.login_page_actions.load()
        self.login_page_actions.fill_email_input(config.TEST_USERNAME_CLEAN)
        self.login_page_actions.fill_password_input(config.TEST_PASSWORD)
        self.login_page_actions.click_login_button()
        self.dashboard_page_actions = DashboardPageActions(browser)
        self.dashboard_page_actions.open_monitors_tab()

    @pytest.fixture()
    def cleanup(self, browser):
        """
        Delete created monitor - cleanup for all tests
        """
        yield
        self.monitors_page_actions = MonitorPageActions(browser)
        self.monitors_page_actions.delete_current_monitor()

    @pytest.mark.parametrize("through_add_button", [True, False])
    # through add button (True) or through clicking smiley panel option (False)
    def test_user_can_create_new_smiley_monitor_from_clean_state(self, setup, cleanup, browser, through_add_button):
        self.monitors_page_actions = MonitorPageActions(browser)
        self.monitors_page_actions.add_new_smiley_monitor(through_add_button)

        check.is_true(self.monitors_page_actions.is_monitor_chart_visible())
        check.is_true(self.monitors_page_actions.is_monitor_detail_panel_visible())
        check.is_true(self.monitors_page_actions.is_monitor_emotion_panel_visible())
        check.is_true(self.monitors_page_actions.is_monitor_chart_date_filter_visible())

    @pytest.mark.parametrize("monitor_name", ["Test smiley monitor name", "Test smiley monitor name with numbers 123",
                                              "Test smiley monitor with special signs.@!"])
    def test_user_can_name_smiley_monitor_when_creating(self, setup, cleanup, browser, monitor_name):
        self.monitors_page_actions = MonitorPageActions(browser)
        self.monitors_page_actions.add_new_smiley_monitor(monitor_name=monitor_name)

        check.is_in(monitor_name.upper(), self.monitors_page_actions.get_monitor_name())

    @pytest.mark.parametrize("high_record", [True, False])
    # using high record (True) or low record (False)
    def test_user_can_choose_high_or_low_record_when_creating_smiley_monitor(self, setup, cleanup, browser, high_record):
        self.monitors_page_actions = MonitorPageActions(browser)
        self.monitors_page_actions.add_new_smiley_monitor(high_record=high_record)

    def test_user_can_see_starting_date_of_monitor(self, setup, cleanup, browser):
        self.monitors_page_actions = MonitorPageActions(browser)
        self.monitors_page_actions.add_new_smiley_monitor()

        check.is_in(date.today().strftime("%d/%m/%Y"), self.monitors_page_actions.get_starting_date())

    def test_user_can_add_new_emotions_entries(self, setup, cleanup, browser):
        self.monitors_page_actions = MonitorPageActions(browser)
        self.monitors_page_actions.add_new_smiley_monitor()
        self.monitors_page_actions.add_new_smiley_entry(emotion='good')
        check.equal(1, self.monitors_page_actions.get_records_number())

        yesterday_date = date.today() - timedelta(days=1)
        self.monitors_page_actions.add_new_smiley_entry(emotion='great', input_date=yesterday_date)
        check.equal(2, self.monitors_page_actions.get_records_number())

        two_days_ago_date = date.today() - timedelta(days=2)
        self.monitors_page_actions.add_new_smiley_entry(emotion='negative', input_date=two_days_ago_date)
        check.equal(3, self.monitors_page_actions.get_records_number())

        three_days_ago_date = date.today() - timedelta(days=3)
        self.monitors_page_actions.add_new_smiley_entry(emotion='bad', input_date=three_days_ago_date)
        check.equal(4, self.monitors_page_actions.get_records_number())
        # here it is a bit hard to verify graph, it could be tested by visual testing tool like Percy maybe?
