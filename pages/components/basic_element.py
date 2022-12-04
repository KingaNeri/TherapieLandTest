class BasicElement:

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.element = None

    @property
    def web_element(self):
        if not self.element:
            self.element = self.driver.find_element(*self.locator)
        return self.element

    def is_visible(self):
        try:
            element = self.web_element
            if element is not None:
                return True
            return False
        except Exception as e:
            return False
