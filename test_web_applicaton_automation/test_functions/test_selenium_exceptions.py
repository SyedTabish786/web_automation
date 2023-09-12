from selenium.common.exceptions import TimeoutException, NoSuchElementException, \
    ElementNotVisibleException, ElementNotSelectableException, StaleElementReferenceException, \
    ElementClickInterceptedException, WebDriverException, InvalidSessionIdException
from selenium.webdriver.support.wait import WebDriverWait


def handle_selenium_exceptions(driver, exception_class, *args, timeout=10):
    exception_handlers = {
        TimeoutException: lambda: handle_timeout_exception(driver, timeout),
        NoSuchElementException: lambda: handle_no_such_element_exception(driver, *args),
        ElementNotVisibleException: lambda: handle_element_not_visible_exception(driver, *args),
        ElementNotSelectableException: lambda: handle_element_not_selectable_exception(driver, *args),
        StaleElementReferenceException: lambda: handle_stale_element_reference_exception(driver, *args),
        ElementClickInterceptedException: lambda: handle_element_click_intercepted_exception(driver, *args),
        WebDriverException: lambda: handle_web_driver_exception(driver, exception_class),
        InvalidSessionIdException: lambda: handle_invalid_session_assertion_error(driver)
    }

    try:
        if exception_class in exception_handlers:
            exception_handlers[exception_class]()
        else:
            print(f"Unhandled exception: {exception_class}")
    except Exception as e:
        print(f"Exception occurred: {e}")


def handle_timeout_exception(driver, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(lambda x: False)
    except TimeoutException as e:
        print(f"Timeout occurred: {e}")


def handle_no_such_element_exception(driver, by, value):
    try:
        driver.find_element(by, value)
    except NoSuchElementException as e:
        print(f"Element not found: {e}")


def handle_element_not_visible_exception(driver, element):
    try:
        element.is_displayed()
    except ElementNotVisibleException as e:
        print(f"Element not visible: {e}")


def handle_element_not_selectable_exception(driver, element):
    try:
        element.is_enabled()
    except ElementNotSelectableException as e:
        print(f"Element not selectable: {e}")


def handle_invalid_session_assertion_error(driver):
    try:
        raise AssertionError(f"AssertionError: {InvalidSessionIdException()}")
    except AssertionError as e:
        if "InvalidSessionIdException" in str(e):
            print(f"Caught AssertionError with InvalidSessionIdException: {e}")


def handle_stale_element_reference_exception(driver, element):
    try:
        element.is_enabled()
    except StaleElementReferenceException as e:
        print(f"Stale element reference: {e}")


def handle_element_click_intercepted_exception(driver, element):
    try:
        element.click()
    except ElementClickInterceptedException as e:
        print(f"Element click intercepted: {e}")


# Below function working perfectly in main script
def handle_web_driver_exception(driver, exception_class):
    try:
        if isinstance(driver, exception_class):
            print(f"WebDriver exception occurred: {driver}")
    except WebDriverException as e:
        print(f"WebDriver exception occurred: {e}")
