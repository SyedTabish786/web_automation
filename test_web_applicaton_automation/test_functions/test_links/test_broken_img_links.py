import pytest
import requests
from selenium.webdriver.common.by import By


def test_find_broken_images(self):
    # Get all images on the page
    images = self.image_page.get_all_images()

    # Initialize a list to store broken image links
    broken_images = []

    for image in images:
        src = image.get_attribute("src")

        # Check if the image source is valid
        if src:
            response = requests.get(src)
            if response.status_code != 200:
                broken_images.append(src)

    # Assert that there are no broken images
    self.assertEqual(len(broken_images), 0, f"Broken Images: {broken_images}")


def find_and_validate_broken_links(self, url):
    self.driver.get(url)
    links = self.driver.find_elements(By.TAG_NAME, 'a')
    broken_links = []

    for link in links:
        href = link.get_attribute('href')
        if href:
            response = requests.head(href)
            if response.status_code != 200:
                broken_links.append(href)

    assert not broken_links, f"Broken links found: {broken_links}"


if __name__ == '__main__':
    pytest.main([__file__])
