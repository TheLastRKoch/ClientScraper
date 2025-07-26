from environment import PAGE_COLUMN_LIST
from utils.files import FileUtils


class XMLFilterException(Exception):
    pass


class XMLFilterService:

    def turn_xml_to_dic(self, page_number, page_xml):
        page_dic = FileUtils.xml_to_dic(page_xml)
        if page_dic == {}:
            raise XMLFilterException("The dic page is empty")
        return page_dic

    def filter_page_respose(self, page_dic):
        client_list_unformatted = (
            page_dic.get("html", {})
            .get("body", {})
            .get("div", {})[0]
            .get("WG:R", {})
            .get("WG:F", {})
            .get("WC:UC", {})
            .get("WC:TC", {})
            .get("WC:TP", {})
            .get("WC:UC", {})
            .get("WC:UC", {})[0]
            .get("WC:DG", {})[1]
            .get("WG:DR", {})
        )
        return client_list_unformatted

    def retrive_clients_from_dic(self, client_list_unformatted):
        client_list = []
        for client_columns in client_list_unformatted:
            rows = []
            for column in client_columns.get("WG:DL", {}):
                rows.append(column.get("@VLB", 0))
            client_list.append(dict(zip(PAGE_COLUMN_LIST, rows)))
        return client_list
