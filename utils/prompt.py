from time import sleep
import os


class PromptUtils:
    @classmethod
    def clear(self):
        os.system("clear")

    @classmethod
    def ask_user(self, title):
        return input(title + "\n")

    @classmethod
    def wait_for_user(self, title):
        if title:
            print(title + "\n\n")
        input("Press any key to continue to continue...")

    @classmethod
    def wait(self, seconds):
        sleep(seconds)
