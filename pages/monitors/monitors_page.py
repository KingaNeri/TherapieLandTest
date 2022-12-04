from pages.components.basic_element import BasicElement
from pages.monitors.monitors_page_locators import MonitorsPageLocators


class MonitorPage:

    def __init__(self, driver):
        self.driver = driver

    @property
    def add_new_monitor_button(self):
        return BasicElement(self.driver, MonitorsPageLocators.ADD_NEW_MONITOR_BUTTON)

    @property
    def add_new_counting_monitor_panel(self):
        return BasicElement(self.driver, MonitorsPageLocators.ADD_NEW_COUNTING_MONITOR_PANEL)

    @property
    def add_new_smiley_monitor_panel(self):
        return BasicElement(self.driver, MonitorsPageLocators.ADD_NEW_SMILEY_MONITOR_PANEL)

    @property
    def add_new_counting_monitor_in_popup(self):
        return BasicElement(self.driver, MonitorsPageLocators.ADD_NEW_COUNTING_MONITOR_IN_POPUP)

    @property
    def add_new_smiley_monitor_in_popup(self):
        return BasicElement(self.driver, MonitorsPageLocators.ADD_NEW_SMILEY_MONITOR_IN_POPUP)

    @property
    def create_monitor_next_step_button(self):
        return BasicElement(self.driver, MonitorsPageLocators.CREATE_MONITOR_NEXT_STEP_BUTTON)

    @property
    def new_monitor_name_input(self):
        return BasicElement(self.driver, MonitorsPageLocators.NEW_MONITOR_NAME_INPUT)

    @property
    def high_record_option(self):
        return BasicElement(self.driver, MonitorsPageLocators.HIGH_RECORD_OPTION)

    @property
    def low_record_option(self):
        return BasicElement(self.driver, MonitorsPageLocators.LOW_RECORD_OPTION)

    @property
    def add_button_popup(self):
        return BasicElement(self.driver, MonitorsPageLocators.ADD_BUTTON)

    @property
    def starting_date(self):
        return BasicElement(self.driver, MonitorsPageLocators.STARTING_DATE)

    @property
    def records_counter(self):
        return BasicElement(self.driver, MonitorsPageLocators.RECORDS_COUNTER)

    @property
    def monitor_name(self):
        return BasicElement(self.driver, MonitorsPageLocators.MONITOR_NAME)

    @property
    def monitor_detail_panel(self):
        return BasicElement(self.driver, MonitorsPageLocators.MONITOR_DETAIL_PANEL)

    @property
    def monitor_emotion_panel(self):
        return BasicElement(self.driver, MonitorsPageLocators.MONITOR_EMOTION_PANEL)

    @property
    def monitor_chart(self):
        return BasicElement(self.driver, MonitorsPageLocators.MONITOR_CHART)

    @property
    def monitor_chart_date_filter(self):
        return BasicElement(self.driver, MonitorsPageLocators.MONITOR_CHART_DATE_FILTER)

    @property
    def monitor_actions_button(self):
        return BasicElement(self.driver, MonitorsPageLocators.MONITOR_ACTIONS_BUTTON)

    @property
    def delete_dropdown_option(self):
        return BasicElement(self.driver, MonitorsPageLocators.DELETE_DROPDOWN_OPTION)

    @property
    def confirm_monitor_delete_button(self):
        return BasicElement(self.driver, MonitorsPageLocators.CONFIRM_MONITOR_DELETE_BUTTON)

    @property
    def emotion_date_input(self):
        return BasicElement(self.driver, MonitorsPageLocators.EMOTION_DATE_INPUT)

    @property
    def smiley_bad(self):
        return BasicElement(self.driver, MonitorsPageLocators.SMILEY_BAD)

    @property
    def smiley_negative(self):
        return BasicElement(self.driver, MonitorsPageLocators.SMILEY_NEGATIVE)

    @property
    def smiley_good(self):
        return BasicElement(self.driver, MonitorsPageLocators.SMILEY_GOOD)

    @property
    def smiley_great(self):
        return BasicElement(self.driver, MonitorsPageLocators.SMILEY_GREAT)

    @property
    def add_emotion_button(self):
        return BasicElement(self.driver, MonitorsPageLocators.ADD_EMOTION_BUTTON)