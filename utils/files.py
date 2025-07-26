import xmltodict
import csv


class UtilsFile:
    @classmethod
    def read_file(self, file_path):
        """Read and return the contents of a file as a string."""
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    @classmethod
    def write_textfile(self, file_path, data):
        """
        Write data to a text file.
        :param file_path: Path to the text file.
        :param data: String to write to the file.
        """
        with open(file_path, "a", newline="", encoding="utf-8") as f:
            f.write(data)

    @classmethod
    def write_csv(self, file_path, data):
        """
        Write data to a CSV file.
        :param file_path: Path to the CSV file.
        :param data: List of rows (each row is a list or tuple).
        """
        with open(file_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(data)

    @classmethod
    def xml_to_dic(self, xml_string):
        return xmltodict.parse(xml_string)
