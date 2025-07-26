import xmltodict
import csv


class FileUtils:
    @classmethod
    def read_file(self, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    @classmethod
    def write_textfile(self, file_path, data):
        with open(file_path, "a", newline="", encoding="utf-8") as f:
            f.write(data)

    @classmethod
    def write_csv(self, file_path, data):
        keys = data[0].keys()

        with open(file_path, 'a', newline='') as file:
            dict_writer = csv.DictWriter(file, keys)
            dict_writer.writerows(data)

    @classmethod
    def xml_to_dic(self, xml_string):
        return xmltodict.parse(xml_string)
