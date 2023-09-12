import subprocess

import allure


class AllureFunctions2(object):
    def __init__(self, driver):
        self.driver = driver

    def run_tests_with_allure_report(self, output_dir="allure-results"):
        command = f"pytest --alluredir={output_dir}"
        subprocess.run(command, shell=True)

    def generate_allure_report(self, output_dir="allure-results", report_dir="allure-report"):
        command = f"allure generate {output_dir} -o {report_dir}"
        subprocess.run(command, shell=True)

    def open_allure_report(self, report_dir="allure-report"):
        command = f"allure open {report_dir}"
        subprocess.run(command, shell=True)

    @staticmethod
    def attach_screenshot_to_allure(screenshot_path, name="Screenshot"):
        allure.attach.file(screenshot_path, name=name, attachment_type=allure.attachment_type.PNG)

    @staticmethod
    def attach_text_to_allure(text, name="Text Attachment", attachment_type=allure.attachment_type.TEXT):
        allure.attach(text, name=name, attachment_type=attachment_type)

    @staticmethod
    def attach_url_to_allure(url, name="URL"):
        allure.attach(url, name=name, attachment_type=allure.attachment_type.URI_LIST)

    def attach_screenshot(self, screenshot_name="Screenshot"):
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name=screenshot_name, attachment_type=allure.attachment_type.PNG)
