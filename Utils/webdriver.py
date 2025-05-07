from selenium import webdriver


class WebDriver:
    def __init__(self, driver_path=None):
        if driver_path:
            self.driver = webdriver.Edge(executable_path=driver_path)
        else:
            self.driver = webdriver.Edge()

    def go_to(self, url):
        self.driver.get(url)

    def find(self, by, value):
        return self.driver.find_element(by, value)

    def find_various(self, by, value):
        return self.driver.find_elements(by, value)

    def quit(self, url):
        self.driver.get(url)
