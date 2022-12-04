from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, "[data-test='email-input'] [data-test='input-text']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[data-test='current-password-input'] input")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-test='login-submit-btn']")

