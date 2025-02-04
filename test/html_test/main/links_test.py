import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class NavBarLinks(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        self.driver = webdriver.Firefox(options=options)
        self.driver = webdriver.Firefox()

        self.driver.get("http://localhost:5000")

    def tearDown(self):
        self.driver.close()

    def test_main_title_link(self):
        self.driver.find_element_by_link_text("Bookshelf").click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "h3"), "Books")
        )

    def test_register_on_navbar(self):
        self.driver.find_element_by_link_text("Sign-up").click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "h3"), "Register")
        )

    def test_login_link_on_navbar(self):
        self.driver.find_element_by_link_text("Login").click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "h3"), "Login")
        )

    def test_books_link_on_navbar(self):
        self.driver.find_element_by_link_text("Books").click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "h3"), "Books")
        )


if __name__ == "__main__":
    unittest.main()
