class GooglePage:
    def open(self, driver):
        driver.get("https://www.google.com")
    def get_title(self, driver):
        return driver.title