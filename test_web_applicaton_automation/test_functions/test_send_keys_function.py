from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def send_keys_by_id(driver, element_id, keys_to_send, timeout=10):
    """
    Send keys to a web element using its ID.
    """
    try:
        element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, element_id)))
        element.clear()
        element.send_keys(keys_to_send)
    except Exception as e:
        print(f"Error: {e}")


def send_keys_by_xpath(driver, element_xpath, keys_to_send, timeout=10):
    """
    Send keys to a web element using its XPath.
    """
    try:
        element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, element_xpath)))
        element.clear()
        element.send_keys(keys_to_send)
    except Exception as e:
        print(f"Error: {e}")

# Usage example:
# from selenium import webdriver
#
# # Assuming you have a 'driver' instance representing the browser driver
# driver = webdriver.Chrome()
# url = "https://www.example.com"
# driver.get(url)
#
# # Sending keys using element ID
# element_id = "username_input"
# keys_to_send = "your_username"
# send_keys_by_id(driver, element_id, keys_to_send)
#
# # Sending keys using element XPath
# element_xpath = "//input[@id='password_input']"
# keys_to_send = "your_password"
# send_keys_by_xpath(driver, element_xpath, keys_to_send)
#
# # Remember to close the browser when you are done
# driver.quit()
