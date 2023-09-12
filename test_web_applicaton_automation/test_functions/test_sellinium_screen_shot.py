import os
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import WebDriverException
from PIL import Image

# Function to take a screenshot of the entire browser window
def capture_full_page_screenshot(driver: WebDriver, screenshot_name: str):
    try:
        driver.save_screenshot(screenshot_name)
    except WebDriverException as e:
        print(f"Failed to capture full page screenshot: {e}")

# Function to take a screenshot of a specific element
def capture_element_screenshot(element: WebElement, screenshot_name: str):
    try:
        element.screenshot(screenshot_name)
    except WebDriverException as e:
        print(f"Failed to capture element screenshot: {e}")

# Function to take a screenshot of the entire screen
def capture_screen_screenshot(screenshot_name: str):
    try:
        from mss import mss
        with mss() as sct:
            sct.shot(output=screenshot_name)
    except ImportError:
        print("mss library not installed. Install using 'pip install mss'.")

# Function to capture a full page screenshot and save it in a specified directory
def capture_full_page_screenshot_in_directory(driver: WebDriver, directory: str, screenshot_name: str):
    try:
        full_path = os.path.join(directory, screenshot_name)
        driver.save_screenshot(full_path)
        print(f"Full page screenshot saved to {full_path}")
    except WebDriverException as e:
        print(f"Failed to capture full page screenshot: {e}")

# Function to capture a screenshot of a specific element and save it in a specified directory
def capture_element_screenshot_in_directory(element: WebElement, directory: str, screenshot_name: str):
    try:
        full_path = os.path.join(directory, screenshot_name)
        element.screenshot(full_path)
        print(f"Element screenshot saved to {full_path}")
    except WebDriverException as e:
        print(f"Failed to capture element screenshot: {e}")

# Function to capture a screenshot of the entire screen and save it in a specified directory
def capture_screen_screenshot_in_directory(directory: str, screenshot_name: str):
    try:
        full_path = os.path.join(directory, screenshot_name)
        capture_screen_screenshot(full_path)
        print(f"Screen screenshot saved to {full_path}")
    except Exception as e:
        print(f"Failed to capture screen screenshot: {e}")

# Function to take a screenshot of the entire browser window and crop it to the specified element's dimensions
def capture_element_area_screenshot(driver: WebDriver, element: WebElement, screenshot_name: str):
    try:
        # Get the element's location and size
        location = element.location
        size = element.size
        end_x = location['x'] + size['width']
        end_y = location['y'] + size['height']

        # Capture the full page screenshot
        temp_screenshot_name = "temp_screenshot.png"
        driver.save_screenshot(temp_screenshot_name)

        # Crop the screenshot to the element's dimensions
        im = Image.open(temp_screenshot_name)
        im = im.crop((location['x'], location['y'], end_x, end_y))
        im.save(screenshot_name)

        # Delete the temporary screenshot
        os.remove(temp_screenshot_name)

        print(f"Element area screenshot saved to {screenshot_name}")
    except WebDriverException as e:
        print(f"Failed to capture element area screenshot: {e}")

# Example usage:
# if __name__ == "__main__":
#     driver = webdriver.Chrome()
#     driver.get("https://www.example.com")
#
#     # Capture full page screenshot
#     capture_full_page_screenshot(driver, "full_page_screenshot.png")
#
#     # Capture screenshot of a specific element
#     element = driver.find_element("xpath", "//div[@id='example_div']")
#     capture_element_screenshot(element, "element_screenshot.png")
#
#     # Capture screenshot of the entire screen (using mss library)
#     capture_screen_screenshot("screen_screenshot.png")
#
#     # Capture full page screenshot and save it in a specified directory
#     capture_full_page_screenshot_in_directory(driver, "screenshots", "full_page_screenshot.png")
#
#     # Capture screenshot of a specific element and save it in a specified directory
#     capture_element_screenshot_in_directory(element, "screenshots", "element_screenshot.png")
#
#     # Capture screenshot of the entire screen and save it in a specified directory
#     capture_screen_screenshot_in_directory("screenshots", "screen_screenshot.png")
#
#     # Capture screenshot of the entire browser window and crop it to the element's dimensions
#     capture_element_area_screenshot(driver, element, "element_area_screenshot.png")
#
#     driver.quit()
