class ss(object):

    def __init__(self, driver):
        self.driver = driver

    def screenshot(self, path):
        directory = ("G:/automation/test_vcm_automation/Reports/allure-report")
        self.driver.get_screenshot_as_file(directory + path)
