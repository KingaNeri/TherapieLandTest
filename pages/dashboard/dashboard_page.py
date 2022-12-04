from pages.components.basic_element import BasicElement
from pages.dashboard.dashboard_page_locators import DashboardPageLocators


class DashboardPage:

    def __init__(self, driver):
        self.driver = driver

    @property
    def monitors_tab(self):
        return BasicElement(self.driver, DashboardPageLocators.MONITORS_TAB)
