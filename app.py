from services.factura_tributaria import FacturaTributariaService
from services.xml_filter import XMLFilterService
from utils.files import FileUtils

if __name__ == "__main__":

    # Init services
    factura_tributaria = FacturaTributariaService()
    xml_filter = XMLFilterService()

    factura_tributaria.bootstrap()
    page_range = factura_tributaria.get_page_range()
    page_counter = 0

    for page_number in page_range:
        factura_tributaria.open_application()
        factura_tributaria.switch_page(page_number)
        page_xml = factura_tributaria.get_page_xml()

        page_dic = xml_filter.turn_xml_to_dic(page_number, page_xml)
        client_list_unformatted = xml_filter.filter_page_respose(page_dic)
        client_list = xml_filter.retrive_clients_from_dic(client_list_unformatted)
        FileUtils.write_csv("resources/client_list.csv", client_list)
        page_counter = +1
    factura_tributaria.Termination()
