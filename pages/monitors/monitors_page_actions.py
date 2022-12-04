from pages.monitors.monitors_page import MonitorPage
from datetime import date
import time
from typing import Literal


class MonitorPageActions:
    def __init__(self, driver):
        self.driver = driver
        self.monitor_page = MonitorPage(driver)

    def add_new_smiley_monitor(self, through_button: bool = True, monitor_name : str ='Test Smiley Monitor',
                               high_record : bool = True):
        """
        Adds new smiley monitor based on parameters.
        :param through_button: bool - is new monitor created through + icon button (True) or through smiley panel option
            (available on empty state) (False)
        :param monitor_name: str - name of monitor that will be filled in input
        :param high_record: bool - is new smiley monitor created using smiley as high record (True)
            or as low record (False)
        """
        if through_button:
            self.monitor_page.add_new_monitor_button.web_element.click()
        else:
            self.monitor_page.add_new_smiley_monitor_panel.web_element.click()

        self.monitor_page.add_new_smiley_monitor_in_popup.web_element.click()
        self.monitor_page.create_monitor_next_step_button.web_element.click()

        self.monitor_page.new_monitor_name_input.web_element.send_keys(monitor_name)

        # high record is chosen by default
        if not high_record:
            self.monitor_page.low_record_option.web_element.click()

        self.monitor_page.add_button_popup.web_element.click()

    def delete_current_monitor(self):
        self.monitor_page.monitor_actions_button.web_element.click()
        self.monitor_page.delete_dropdown_option.web_element.click()
        self.monitor_page.confirm_monitor_delete_button.web_element.click()

    def get_monitor_name(self):
        return self.monitor_page.monitor_name.web_element.text

    def get_starting_date(self):
        return self.monitor_page.starting_date.web_element.text

    def get_records_number(self):
        time.sleep(1)
        text_element = self.monitor_page.records_counter.web_element.text
        # take just number from text
        return int(text_element.split("\n")[0])

    def is_monitor_detail_panel_visible(self):
        return self.monitor_page.monitor_detail_panel.is_visible()

    def is_monitor_emotion_panel_visible(self):
        return self.monitor_page.monitor_emotion_panel.is_visible()

    def is_monitor_chart_visible(self):
        return self.monitor_page.monitor_chart.is_visible()

    def is_monitor_chart_date_filter_visible(self):
        return self.monitor_page.monitor_chart_date_filter.is_visible()

    EMOTIONS = Literal['bad', 'negative', 'good', 'great']

    def add_new_smiley_entry(self, emotion: EMOTIONS = 'great', input_date: date = date.today()):
        """
        Adds new emotion entry to Smiley panel
        :param emotion: one of four emotion types defined in EMOTIONS Literal
        :param input_date: input date in format dd/mm/yyyy
        """
        time.sleep(2)
        date_string = input_date.strftime("%d/%m/%Y")
        self.monitor_page.emotion_date_input.web_element.clear()
        self.monitor_page.emotion_date_input.web_element.send_keys(date_string)
        self.monitor_page.records_counter.web_element.click()

        if emotion == 'bad':
            self.monitor_page.smiley_bad.web_element.click()
        elif emotion == 'negative':
            self.monitor_page.smiley_negative.web_element.click()
        elif emotion == 'good':
            self.monitor_page.smiley_good.web_element.click()
        else:
            self.monitor_page.smiley_great.web_element.click()

        self.monitor_page.add_emotion_button.web_element.click()
