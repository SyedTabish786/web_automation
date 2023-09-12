from selenium.webdriver.common.by import By


class SeleniumLocators:
    @staticmethod
    def by_id(id_value):
        return (By.ID, id_value)

    @staticmethod
    def by_name(name_value):
        return (By.NAME, name_value)

    @staticmethod
    def by_xpath(xpath_expression):
        return (By.XPATH, xpath_expression)

    @staticmethod
    def by_link_text(link_text):
        return (By.LINK_TEXT, link_text)

    @staticmethod
    def by_partial_link_text(partial_link_text):
        return (By.PARTIAL_LINK_TEXT, partial_link_text)

    @staticmethod
    def by_tag_name(tag_name):
        return (By.TAG_NAME, tag_name)

    @staticmethod
    def by_class_name(class_name):
        return (By.CLASS_NAME, class_name)

    @staticmethod
    def by_css_selector(css_selector):
        return (By.CSS_SELECTOR, css_selector)
