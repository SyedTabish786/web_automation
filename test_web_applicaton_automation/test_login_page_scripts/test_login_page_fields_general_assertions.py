import allure
import pytest
from test_attributes.test_locators import locator

from Test_base.test_EnvironmentSetup import EnvironmentSetup
from test_data.test_value import data
from test_functions import test_allure_functions2
from test_functions import test_sellenium_assertions
from test_functions import test_sellinium_functions, test_selenium_exceptions, test_until_url_loaded
from test_pages.test_signup_page import login
from test_resources.test_screenshots_file_names import screenshots_names
from test_resources.test_passed_assertion_messages import passed_assertion_messages, failed_assertion_messages
from test_resources.test_element_attributes_names import element_attributes, element_attribute_values
from time import sleep


@pytest.mark.usefixtures("setup_teardown")
@allure.severity(allure.severity_level.BLOCKER)
class TestVWebPage(EnvironmentSetup):
    @allure.severity(allure.severity_level.CRITICAL)
    def test_assertion_web_page_title(self):
        driver = test_sellinium_functions.initialize_driver()
        try:

            test_sellinium_functions.open_page(driver, data.expected_login_page_url)
            actual_page_title = driver.title

            if actual_page_title == data.expected_title:
                test_sellenium_assertions.assert_always_true(passed_assertion_messages.title_assertion_passed)
            else:
                test_allure_functions2.AllureFunctions2(driver).attach_screenshot(
                    screenshots_names.title_assertion_failed)
                test_sellenium_assertions.assert_always_false(failed_assertion_messages.title_assertion_failed)

        except Exception as e:
            raise AssertionError(f"{e}")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_assertion_web_page_url(self):
        driver = test_sellinium_functions.initialize_driver()
        try:
            test_sellinium_functions.maximize_window(driver)
            test_sellinium_functions.open_page(driver, data.expected_login_page_url)
            actual_page_url = driver.current_url

            if actual_page_url == data.expected_login_page_url:
                test_sellenium_assertions.assert_always_true(passed_assertion_messages.page_url_assertion_passed)
            else:
                test_allure_functions2.AllureFunctions2(driver).attach_screenshot(
                    screenshots_names.url_assertion_failed)
                test_sellenium_assertions.assert_always_false(failed_assertion_messages.page_url_assertion_failed)

        except Exception as e:
            raise AssertionError(f"{e}")

    @allure.severity(allure.severity_level.NORMAL)
    def test_assertion_web_pagelogo(self):
        driver = test_sellinium_functions.initialize_driver()

        try:
            test_sellinium_functions.maximize_window(driver)
            test_sellinium_functions.open_page(driver, data.expected_login_page_url)

            login_page = login(driver)

            logo_displayed = test_sellinium_functions.get_element_attribute(login_page.logo,
                                                                            element_attributes.logo_attribute_src)

            if logo_displayed == data.expected_logo_source:
                test_sellenium_assertions.assert_always_true(passed_assertion_messages.page_logo_assertion_passed)

            else:

                test_allure_functions2.AllureFunctions2(driver).attach_screenshot(
                    screenshots_names.Page_Logo_assertion_fail)
                test_sellenium_assertions.assert_always_false(failed_assertion_messages.page_logo_assertion_failed)
        except Exception as e:
            raise AssertionError(f"{e}")

    @allure.severity(allure.severity_level.NORMAL)
    def test_login_form_input_fields(self):
        driver = test_sellinium_functions.initialize_driver()

        try:
            test_sellinium_functions.maximize_window(driver)
            test_sellinium_functions.open_page(driver, data.expected_login_page_url)
            login_page = login(driver)

            user_input_field_attribute = test_sellinium_functions.get_element_attribute(login_page.user_name,
                                                                                        element_attributes.user_input_field_attribute)
            test_selenium_exceptions.handle_stale_element_reference_exception(driver, login_page.user_name)
            if user_input_field_attribute == element_attribute_values.user_input_field_attribute_value:
                test_sellenium_assertions.assert_always_true(
                    passed_assertion_messages.user_input_field_attribute_assertion_passed)
            else:
                test_allure_functions2.AllureFunctions2(driver).attach_screenshot(
                    screenshots_names.user_input_field_attribute_assertion_failed)
                test_sellenium_assertions.assert_always_false(
                    failed_assertion_messages.user_input_field_attribute_assertion_failed)

                test_sellinium_functions.refresh_page(driver)
                login_page = login(driver)

                password_input_field_attribute = test_sellinium_functions.get_element_attribute(login_page.password,
                                                                                                element_attributes.password_input_field_attribute)
                test_selenium_exceptions.handle_stale_element_reference_exception(driver, login_page.password)
                if password_input_field_attribute == element_attribute_values.password_input_field_attribute_value:
                    test_sellenium_assertions.assert_always_true(
                        passed_assertion_messages.password_input_field_attribute_assertion_passed)

                else:
                    test_allure_functions2.AllureFunctions2(driver).attach_screenshot(
                        screenshots_names.password_input_field_attribute_assertion_failed)
                    test_sellenium_assertions.assert_always_false(
                        failed_assertion_messages.password_input_field_attribute_assertion_failed)

                login_page = login(driver)
                login_button_text = test_sellinium_functions.get_element_text(login_page.submit_button)

                test_selenium_exceptions.handle_stale_element_reference_exception(driver, login_page.submit_button)
                if login_button_text == element_attribute_values.login_button_text:
                    test_sellenium_assertions.assert_always_true(
                        passed_assertion_messages.login_button_text_assertion_passed)

                else:
                    test_allure_functions2.AllureFunctions2(driver).attach_screenshot(
                        screenshots_names.login_button_text_assertion_failed)
                    test_sellenium_assertions.assert_always_false(
                        failed_assertion_messages.login_button_text_assertion_failed)

        except Exception as e:
            raise AssertionError(f"{e}")


if __name__ == '__main__':
    pytest.main([__file__])
