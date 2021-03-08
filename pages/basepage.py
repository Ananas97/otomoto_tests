class BasePage(object):
    """This class is the parent class for all the pages in a test application."""
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def load(self):
        self.driver.get(self.url)
    #def click_element(self):
    #def wait_until_visible(self):
    #def find_elements(self):
    #def send_keys(self):
    #def assert_
