import unittest
from selenium import webdriver
import time


class TestPage(unittest.TestCase):
    def test_page1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector(".first_block .form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".first_block .form-control.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(".first_block .form-control.third")
        input3.send_keys("xxx@xxx.com")

        button = browser.find_element_by_css_selector("button")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text,"Congratulations! You have successfully registered!",'Wrong message!!!')

        time.sleep(10)
        browser.quit()

    def test_page2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector(".first_block .form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".first_block .form-control.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(".first_block .form-control.third")
        input3.send_keys("xxx@xxx.com")

        button = browser.find_element_by_css_selector("button")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text,"Congratulations! You have successfully registered!",'Wrong message!!!')

        time.sleep(10)
        browser.quit()

if __name__ == "__main__":
    unittest.main()