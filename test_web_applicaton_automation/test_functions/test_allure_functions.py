import subprocess

import allure
import pytest


def run_tests_with_allure_report(self, output_dir="allure-results"):
    # Run the tests with Allure reporting using pytest and allure-pytest plugin
    command = self.command = f"pytest --alluredir={output_dir}"
    subprocess.run(command, shell=True)


def generate_allure_report(output_dir="allure-results", report_dir="allure-report"):
    # Generate the Allure report using the allure command-line tool
    command = f"allure generate {output_dir} -o {report_dir}"
    subprocess.run(command, shell=True)


def open_allure_report(report_dir="allure-report"):
    # Open the Allure report in a web browser
    command = f"allure open {report_dir}"
    subprocess.run(command, shell=True)


# Function to attach a screenshot to the Allure report
def attach_screenshot_to_allure(screenshot_path, name="Screenshot"):
    allure.attach.file(screenshot_path, name=name, attachment_type=allure.attachment_type.PNG)


# Function to attach text to the Allure report
def attach_text_to_allure(text, name="Text Attachment", attachment_type=allure.attachment_type.TEXT):
    allure.attach(text, name=name, attachment_type=attachment_type)


# Function to attach a URL to the Allure report
def attach_url_to_allure(url, name="URL"):
    allure.attach(url, name=name, attachment_type=allure.attachment_type.URI_LIST)


# Example usage:
# if __name__ == "__main__":
#     run_tests_with_allure_report()
#
#     # Attach a screenshot to the Allure report
#     # screenshot_file = "screenshot.png"
#     # ... Perform some test steps ...
#     # Save the screenshot
#     # driver.save_screenshot(screenshot_file)
#     # Attach the screenshot to Allure
#     attach_screenshot_to_allure(screenshot_file, name="Homepage Screenshot")
#
#     # Attach some text information to the Allure report
#     text_data = "This is additional information for the test."
#     attach_text_to_allure(text_data, name="Additional Information")
#
#     generate_allure_report()
#     open_allure_report()
if __name__ == '__main__':
    pytest.main([__file__])
