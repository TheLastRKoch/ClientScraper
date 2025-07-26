from time import sleep
import re

from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver


class webdriverUtils:
    def __init__(self):
        chrome_options = Options()

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=chrome_options
        )

        self.driver.maximize_window()

    def navigate(self, url, title=None, read_timeout=1):
        self.driver.get(url)

        self.wait(read_timeout)

        if title:
            if not (
                title := self.get_page_title(
                    r"<title>[\w\W]+{title}[\w\W]+<\/title>".format(title=title)
                )
            ):
                raise NoSuchElementException(f"The page {title} could not be found.")

    def close(self):
        self.driver.quit()

    def wait_for_prompt(self, title):
        if title:
            print(title + "\n\n")
        input("Press any key to continue to continue...")

    def wait(self, seconds):
        sleep(seconds)

    def get_page_title(self, title_pattern):
        match = re.search(
            title_pattern,
            self.driver.page_source,
            re.MULTILINE,
        )
        if match:
            return match
        return None

    def get_element_by_ID(self, query):
        return self.driver.find_element(By.ID, query)

    def get_element_by_xpath(self, query):
        return self.driver.find_element(By.XPATH, query)

    def type_text(self, element, text):
        element.clear()
        element.send_keys(text, Keys.ENTER)

    def click_element(self, element):
        element.click()

    def get_source(self):
        return self.driver.page_source

    def get_screenshot(self):
        return self.driver.get_screenshot_as_base64()

    def get_cookies(self):
        return self.driver.get_cookies()
