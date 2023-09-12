from test_attributes.test_locators import locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC







class Home(object):
    def __init__(self, driver):
        self.driver = driver
        wait = WebDriverWait (driver, 10)
        self.drop_menu = wait.until(EC.element_to_be_clickable((By.XPATH, locator.login_drop)))


