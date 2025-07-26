from services.factura_tributaria import FacturaTributariaService
from services.xml_filter import XMLFilterService
from utils.files import FileUtils
from utils.logging import LoggingUtils as log

if __name__ == "__main__":

    # Init services
    factura_tributaria = FacturaTributariaService()
    xml_filter = XMLFilterService()

    log.info("Process started")
    log.info("Opening Webdriver")
    factura_tributaria.bootstrap()
    page_range = factura_tributaria.get_page_range()
    log.info(f"user selected {str(page_range)}")
    page_counter = 0

    for page_number in page_range:
        log.info(f"Start downloading page {page_number}")
        factura_tributaria.open_application()
        factura_tributaria.switch_page(page_number)
        page_xml = factura_tributaria.get_page_xml()
        page_dic = xml_filter.turn_xml_to_dic(page_number, page_xml)
        client_list_unformatted = xml_filter.filter_page_respose(page_dic)
        client_list = xml_filter.retrive_clients_from_dic(client_list_unformatted)
        log.info(f"Stop downloading page {page_number}")
        log.info(f"Start saving page {page_number} result into csv")
        FileUtils.write_csv("resources/client_list.csv", client_list)
        log.info(f"Stop saving page {page_number} result into csv")
        page_counter = +1
    factura_tributaria.Termination()
