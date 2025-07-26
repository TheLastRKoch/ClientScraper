from utils.webdriver import webdriverUtils
from utils.prompt import PromptUtils

# TODO: Move this to the env
SHOT_WAIT = 1
MEDIUM_WAIT = 3
LONG_WAIT = 5


class FacturaTributariaService:
    def __init__(self):
        self.automation = webdriverUtils()

    def bootstrap(self):
        self.automation.navigate(
            url=r"https://facturatributaria.com",
            # TODO: Move this to the env
            title="La solución para su facturación electrónica",
            read_timeout=SHOT_WAIT,
        )

        # TODO: Move this to the env
        PromptUtils.wait_for_user("Please authenticate")

        self.automation.navigate(
            url=r"https://app.facturatributaria.com/Eos.wgx",
            read_timeout=SHOT_WAIT,
        )

        # TODO: Move this to the env
        PromptUtils.wait_for_user(
            "Please follow the next steps:\n- Go to the clients page\n- Select view all"
        )

    def get_page_range(self):
        user_resp = PromptUtils.ask_user(
            "Please type the number of pages to extract [1-10]"
        )
        start, end = map(int, user_resp.split("-"))
        return range(start, end + 1)

    def open_application(self):
        self.automation.navigate(
            url=r"https://app.facturatributaria.com/Eos.wgx",
            read_timeout=SHOT_WAIT,
        )

    def get_page_xml(self):
        self.automation.navigate(
            "https://app.facturatributaria.com/Route/2.1003048.4/kit/en-GB/CRF_TEMA/1048574.49148.926/0/CRF_TEMA/content.Eos.wgx?vwginstance=0",
            read_timeout=SHOT_WAIT,
        )
        PromptUtils.wait(3)
        page_response = self.automation.get_source()

        if not page_response:
            raise Exception("No client response found in the requests.")
        return page_response

    def switch_page(self, page_number):
        # TODO: Move this to the env
        new_page_button = self.automation.get_element_by_ID("TRG_paging_100")
        self.automation.type_text(new_page_button, page_number)
        PromptUtils.wait(5)

    def Termination(self):
        self.automation.close()