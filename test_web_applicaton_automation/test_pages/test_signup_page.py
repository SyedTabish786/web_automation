from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from test_attributes.test_locators import locator


# login page locator defining


class login(object):

    def __init__(self, driver):
        wait = WebDriverWait(driver, 10)
        self.logo = wait.until(EC.element_to_be_clickable((By.XPATH, locator.page_logo)))

        self.driver = driver
        wait = WebDriverWait(driver, 10)
        self.user_name = wait.until(EC.element_to_be_clickable((By.XPATH, locator.user_name)))

        wait = WebDriverWait(driver, 10)
        self.password = wait.until(EC.element_to_be_clickable((By.XPATH, locator.password)))

        wait = WebDriverWait(driver, 10)
        self.submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, locator.login_button)))
