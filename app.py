from services.factura_tributaria import FacturaTributariaService
from services.xml_filter import XMLFilterService


if __name__ == "__main__":

    # Init services
    factura_tributaria = FacturaTributariaService()
    xml_filter = XMLFilterService()

    factura_tributaria.init_site()

    factura_tributaria.open_application()
    factura_tributaria.switch_page(1)
    page_xml = factura_tributaria.get_page_xml()

    page_dic = xml_filter.turn_xml_to_dic(1, page_xml)
    client_list_unformatted = xml_filter.filter_page_respose(page_dic)
    client_list = xml_filter.retrive_clients_from_dic(client_list_unformatted)
    print(client_list)

    factura_tributaria.open_application()
    factura_tributaria.switch_page(2)
    page_xml = factura_tributaria.get_page_xml()

    # Process XML request
    page_dic = xml_filter.turn_xml_to_dic(2, page_xml)
    client_list_unformatted = xml_filter.filter_page_respose(page_dic)
    client_list = xml_filter.retrive_clients_from_dic(client_list_unformatted)
    print(client_list)
