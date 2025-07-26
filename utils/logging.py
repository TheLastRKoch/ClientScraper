from environment import LOG_FILE_PATH
from utils.files import FileUtils
from datetime import datetime


class LoggingUtils:
    PINK = "\033[95m"
    BLUE = "\033[94m"
    LIGHTBLUE = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    UNDERLINE = "\033[4m"
    COMMON = "\033[0m"

    @classmethod
    def __get_time_standard(self):
        return datetime.now().strftime("%d-%b-%Y %H:%M:%S")

    @classmethod
    def custom_log(self, message, level, color):
        timestamp = self.__get_time_standard()
        log = f"{timestamp}\t|\t{level}\t|\t{message}\n"
        FileUtils.write_textfile(
            LOG_FILE_PATH,
            log
        )
        print(log)

    @classmethod
    def trace(self, message):
        self.custom_log(message, "Trace", self.UNDERLINE)

    @classmethod
    def info(self, message):
        self.custom_log(message, "Info", self.COMMON)

    @classmethod
    def warning(self, message):
        self.custom_log(message, "Warning", self.YELLOW)

    @classmethod
    def error(self, message):
        self.custom_log("Error: " + message, "Error", self.RED)
