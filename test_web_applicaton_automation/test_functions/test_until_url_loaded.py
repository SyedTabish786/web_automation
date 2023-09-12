from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_url_to_load(driver, expected_url, timeout=10):
    try:
        # Wait until the current URL matches the expected URL
        WebDriverWait(driver, timeout).until(EC.url_to_be(expected_url))
        print(f"URL '{expected_url}' is completely loaded.")
    except TimeoutError:
        print(f"Timed out waiting for the URL '{expected_url}' to load.")
    except Exception as e:
        print(f"An error occurred while waiting for the URL '{expected_url}' to load: {e}")
def assert_page_url(driver, expected_url, message=None):
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
#     driver = webdriver.Chrome()
#     driver.get("https://www.example.com")
#
#     # Call the function to wait for the URL 'https://www.example.com' to load completelywait_for_url_to_load(driver, "https://www.example.com")
#
#     # Perform further actions on the fully loaded page
#     element = driver.find_element_by_css_selector("#example-element")
#     element.click()
#
#     driver.quit()
