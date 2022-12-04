from pages.dashboard.dashboard_page import DashboardPage


class DashboardPageActions:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard_page = DashboardPage(driver)

    def open_monitors_tab(self):
        self.dashboard_page.monitors_tab.web_element.click()
