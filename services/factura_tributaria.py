from utils.webdriver import webdriverUtils
from utils.prompt import PromptUtils
from environment import (
    PAGE_LOGIN_TITLE,
    PAGE_REQUEST_AUTH,
    PAGE_FOLLOW_STEPS,
    PAGE_HOMEPAGE_URL,
    PAGE_PAGE_RANGE,
    PAGE_APP_URL,
    PAGE_XML_URL,
    PAGE_PAGING_ID,
    SHOT_WAIT,
    MEDIUM_WAIT,
    LONG_WAIT,
)


class FacturaTributariaException(Exception):
    pass


class FacturaTributariaService:
    def __init__(self):
        self.automation = webdriverUtils()

    def bootstrap(self):
        self.automation.navigate(
            url=PAGE_HOMEPAGE_URL,
            title=PAGE_LOGIN_TITLE,
            read_timeout=SHOT_WAIT,
        )

        PromptUtils.wait_for_user(PAGE_REQUEST_AUTH)

        self.automation.navigate(
            url=PAGE_APP_URL,
            read_timeout=SHOT_WAIT,
        )

        PromptUtils.wait_for_user(PAGE_FOLLOW_STEPS)

    def get_page_range(self):
        user_resp = PromptUtils.ask_user(PAGE_PAGE_RANGE)
        start, end = map(int, user_resp.split("-"))
        return range(start, end + 1)

    def open_application(self):
        self.automation.navigate(
            url=PAGE_APP_URL,
            read_timeout=SHOT_WAIT,
        )

    def get_page_xml(self):
        self.automation.navigate(
            PAGE_XML_URL,
            read_timeout=SHOT_WAIT,
        )
        PromptUtils.wait(MEDIUM_WAIT)
        page_response = self.automation.get_source()

        if not page_response:
            raise Exception("No client response found in the requests.")
        return page_response

    def switch_page(self, page_number):
        new_page_button = self.automation.get_element_by_ID(PAGE_PAGING_ID)
        self.automation.type_text(new_page_button, page_number)
        PromptUtils.wait(LONG_WAIT)

    def Termination(self):
        self.automation.close()
