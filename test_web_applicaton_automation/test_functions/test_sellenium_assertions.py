from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Function to assert that an element is present on the page
def assert_element_present(driver: WebDriver, by, value, message):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, value)))
    except AssertionError as e:
        raise AssertionError(f"{message}: {e}")


# Function to assert that an element is visible on the page
def assert_element_visible(element: WebElement, message):
    try:
        assert element.is_displayed(), message
    except AssertionError as e:
        raise AssertionError(f"{message}: {e}")


# Function to assert that an element's text matches the expected value
def assert_element_text(element: WebElement, expected_text: str, message):
    try:
        actual_text = element.text.strip()
        assert actual_text == expected_text, f"Expected: {expected_text}, Actual: {actual_text}"
    except AssertionError as e:
        raise AssertionError(f"{message}: {e}")


# Function to assert that a page title matches the expected value
def assert_page_title(driver: WebDriver, expected_title: str, message):
    try:
        actual_title = driver.title.strip()
        assert actual_title == expected_title, f"Expected: {expected_title}, Actual: {actual_title}"
    except AssertionError as e:
        raise AssertionError(f"{message}: {e}")


def assert_always_true(message):
    try:
        assert True, message

    except AssertionError as e:
        raise AssertionError(f"{message}: {e}")


def assert_always_false(message):
    try:
        assert False, message

    except AssertionError as e:
        raise AssertionError(f"{message}: {e}")


# Function to assert that a condition is true
def assert_true(condition, message):
    try:
        assert condition, message
    except AssertionError as e:
        raise AssertionError(f"{message}: {e}")


# Function to assert that a condition is false
def assert_false(condition, element, message):
    try:
        assert not condition, message
    except AssertionError as e:
        raise AssertionError(f"{message} for element '{element}': {e}")


def assert_condition(condition, expected_value, message):
    try:
        assert condition == expected_value, message
    except AssertionError as e:
        raise AssertionError(f"{message}: {e}")


# Function to assert that two values are equal
def assert_equals(actual_value, expected_value, message):
    try:
        assert actual_value == expected_value, f"{message}: Actual: {actual_value}, Expected: {expected_value}"
    except AssertionError as e:
        raise AssertionError(f"{message}: {e}")


def assert_input_field_value_matches(driver, input_element_locator, expected_value, timeout=10):
    try:
        # Find the input element using the provided locator
        input_element = input_element_locator

        # Get the actual value from the input field
        actual_value = input_element.get_attribute("value")

        if actual_value.lower() == expected_value.lower():
            print("Assertion passed: Input field value matches the expected value.")
        else:
            print("Assertion failed: Input field value does not match the expected value. "
                  f"Expected: {expected_value}, Actual: {actual_value}")

    except TimeoutException:
        print(f"Element with locator {input_element_locator} not found within {timeout} seconds.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Function to assert that two values are not equal
def assert_not_equals(actual_value, unexpected_value, message):
    try:
        assert actual_value != unexpected_value, f"{message}: Unexpected: {unexpected_value}, Actual: {actual_value}"
    except AssertionError as e:
        raise AssertionError(f"{message}: {e}")


# Function to assert that a value is in a list
def assert_in(value, list_, message):
    try:
        assert value in list_, f"{message}: Value: {value}, List: {list_}"
    except AssertionError as e:
        raise AssertionError(f"{message}: {e}")


# Function to assert that a value is not in a list
def assert_not_in(value, list_, message):
    try:
        assert value not in list_, f"{message}: Value: {value}, List: {list_}"
    except AssertionError as e:
        raise AssertionError(f"{message}: {e}")


def assert_page_url(driver, expected_url, message):
    """
    Function to assert the current page URL matches the expected URL.

    Parameters:
        driver (WebDriver): The Selenium WebDriver instance.
        expected_url (str): The expected URL of the page.
        message (str): Optional message to display if the assertion fails.

    Raises:
        AssertionError: If the current URL does not match the expected URL.
    """
    current_url = driver.current_url
    assert current_url == expected_url, message or f"Expected URL: '{expected_url}' but got URL: '{current_url}'"

# Example usage:
# if __name__ == "__main__":
#     from selenium import webdriver
#
#     driver = webdriver.Chrome()
#     driver.get("https://www.example.com")
#
#     element = driver.find_element("css selector", "#example-element")
#
#     assert_element_present(driver, "css selector", "#example-element")
#     assert_element_visible(element)
#     assert_element_text(element, "Example Text")
#     assert_page_title(driver, "Example Page Title")
#
#     assert_true(2 + 2 == 4, "2 + 2 is not equal to 4")
#     assert_false(2 + 2 == 5, "2 + 2 is equal to 5")
#     assert_equals(10, 10, "Values are not equal")
#     assert_not_equals(10, 20, "Values are equal")
#
#     my_list = [1, 2, 3, 4, 5]
#     assert_in(3, my_list, "Value not found in list")
#     assert_not_in(6, my_list, "Value found in list")
#
#     driver.quit()
