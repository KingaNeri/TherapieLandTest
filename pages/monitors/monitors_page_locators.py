from selenium.webdriver.common.by import By


class MonitorsPageLocators:
    ADD_NEW_MONITOR_BUTTON = (By.CSS_SELECTOR, "[data-test='action-button-icon-undefined']")
    ADD_NEW_COUNTING_MONITOR_PANEL = (By.CSS_SELECTOR, "[data-test='add-new-monitor-button']")
    ADD_NEW_SMILEY_MONITOR_PANEL = (By.XPATH, "//button/p[contains(text(), 'Smiley')]")

    ADD_NEW_COUNTING_MONITOR_IN_POPUP = (By.CSS_SELECTOR, "[data-test='counter-monitor-option']")
    ADD_NEW_SMILEY_MONITOR_IN_POPUP = (By.CSS_SELECTOR, "[data-test='emotion-monitor-option']")
    CREATE_MONITOR_NEXT_STEP_BUTTON = (By.CSS_SELECTOR, "[data-test='create-monitor-next-step-button']")

    NEW_MONITOR_NAME_INPUT = (By.CSS_SELECTOR, "[data-test='input-text']")

    HIGH_RECORD_OPTION = (By.XPATH, "//h3[contains(text(), 'High')]")
    LOW_RECORD_OPTION = (By.XPATH, "//h3[contains(text(), 'Low')]")

    ADD_BUTTON = (By.CSS_SELECTOR, "[data-test='create-monitor-add-monitor-button']")

    MONITOR_NAME = (By.CSS_SELECTOR, "[data-test='monitor-name-button'] span")
    STARTING_DATE = (By.CSS_SELECTOR, "[data-test='starting-date']")
    RECORDS_COUNTER = (By.CSS_SELECTOR, "[data-test='score-counter']")

    MONITOR_DETAIL_PANEL = (By.CSS_SELECTOR, ".monitor-detail")
    MONITOR_EMOTION_PANEL = (By.CSS_SELECTOR, ".monitor-panel-emotion")
    MONITOR_CHART = (By.CSS_SELECTOR, ".monitor-chart")
    MONITOR_CHART_DATE_FILTER = (By.CSS_SELECTOR, ".monitor-chart__date-filter")

    EMOTION_DATE_INPUT = (By.CSS_SELECTOR, "[data-test='input-date-picker'] input")

    SMILEY_BAD = (By.CSS_SELECTOR, "[data-test='emotion-smileyBad-button']")
    SMILEY_NEGATIVE = (By.CSS_SELECTOR, "[data-test='emotion-smileyOk-button']")
    SMILEY_GOOD = (By.CSS_SELECTOR, "[data-test='emotion-smileyGood-button']")
    SMILEY_GREAT = (By.CSS_SELECTOR, "[data-test='emotion-smileyGreat-button']")

    ADD_EMOTION_BUTTON = (By.CSS_SELECTOR, "[data-test='add-emotion-button']")

    MONITOR_ACTIONS_BUTTON = (By.CSS_SELECTOR, "[data-test='monitor-actions-button'] button")
    DELETE_DROPDOWN_OPTION = (By.CSS_SELECTOR, "[data-test='hamburger-option']")

    CONFIRM_MONITOR_DELETE_BUTTON = (By.CSS_SELECTOR, "[data-test='confirm-monitor-delete-button']")


    #(By.CSS_SELECTOR, "[data-test='']")

