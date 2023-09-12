from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# Function to initialize the WebDriver (Chrome in this case)

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


def initialize_driver():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Add this line if you want to run Chrome in headless mode
    service = webdriver.chrome.service.Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver


# Function to maximize the browser window
def maximize_window(driver):
    driver.maximize_window()


# Function to open a web page
def open_page(driver, url):
    driver.get(url)


def navigate_to_url(url):
    """
    Navigate to a URL using Selenium WebDriver.

    Args:
        url (str): The URL to navigate to.
    """
    driver = webdriver.Chrome()  # You can use other browser drivers as well (e.g., Firefox, Edge)
    driver.get(url)
    # Optionally, you can add more logic here, such as assertions or interactions with the page.
    driver.quit()


# Function to find a web element by various locators


def locate_element(driver, locator_type, locator_value, timeout=10):
    """
    Locate a web element using different locator strategies.

    Args:
        driver (WebDriver): The WebDriver instance.
        locator_type (str): The type of locator to use (e.g., 'id', 'name', 'xpath', 'css').
        locator_value (str): The value of the locator.
        timeout (int): Maximum time to wait for the element to be located (default is 10 seconds).

    Returns:
        WebElement: The located WebElement object.
    """
    locator_type = locator_type.lower()

    if locator_type == 'id':
        locator = (By.ID, locator_value)
    elif locator_type == 'name':
        locator = (By.NAME, locator_value)
    elif locator_type == 'xpath':
        locator = (By.XPATH, locator_value)
    elif locator_type == 'css':
        locator = (By.CSS_SELECTOR, locator_value)
    else:
        raise ValueError("Invalid locator type. Supported types: 'id', 'name', 'xpath', 'css'")

    try:
        element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
        return element
    except:
        raise NoSuchElementException(f"Element not found using locator: {locator_type} = {locator_value}")


# Function to click on a web element
def click_element(element):
    element.click()


# Function to enter text into an input field
def enter_text(element, text):
    element.send_keys(text)


# Function to wait for an element to be visible
def wait_for_element_visible(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, value)))


# Function to wait for an element to be clickable
def wait_for_element_clickable(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))


# Function to check if an element is displayed
def is_element_displayed(element):
    return element.is_displayed()


# Function to get the text of an element
def get_element_text(element):
    return element.text


# Function to get the value of an attribute of an element
def get_element_attribute(element, attribute_name):
    return element.get_attribute(attribute_name)


# Function to clear the text in an input field
def clear_text(element):
    element.clear()


# Function to perform a mouse hover action
def hover_over_element(driver, element):
    from selenium.webdriver.common.action_chains import ActionChains
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()


# Function to handle alerts (accept or dismiss)
def handle_alert(driver, accept=True):
    if accept:
        driver.switch_to.alert.accept()
    else:
        driver.switch_to.alert.dismiss()


# Function to switch to a frame by index or name
def switch_to_frame(driver, identifier):
    driver.switch_to.frame(identifier)


# Function to switch back to the default content
def switch_to_default_content(driver):
    driver.switch_to.default_content()


# Function to close the browser
def close_browser(driver):
    driver.quit()


def refresh_page(driver):
    driver.refresh()
# Example usage:
# if __name__ == "__main__":
#     driver = initialize_driver()
#     open_page(driver, "https://www.example.com")
#     element = wait_for_element_visible(driver, By.ID, "element_id")
#     click_element(element)
#     enter_text(element, "Hello, Selenium!")
#     print(get_element_text(element))
#     close_browser(driver)
