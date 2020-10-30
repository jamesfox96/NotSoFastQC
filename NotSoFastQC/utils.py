from NotSoFastQC.modules import module_dict as md
import re
from tabulate import tabulate
from platform import system

if "win" in system().lower():
    try:
        from ctypes import windll
        kernel32 = windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    except ImportError:
        print("\nImport error whilst attempting to import module[windll]. This should not cause a problem"
              " if using unix-based platforms. Contact author for help")


EXIT_MESSAGE = '''\n===========================
                  \nINPUT ERROR: EXITING...
                  \n==========================='''

ENTRY = ">>"
END_MODULE = ">>END_MODULE"
FILTER_TEXT = 0
HEADER = 1
ROWS = 2


class Colours:
    BOLD = '\033[1m'
    CYAN = '\033[36m'
    PASS = '\033[32m'
    WARNING = '\033[33m'
    FAIL = '\033[31m'
    END = '\033[0m'


class TerminalLog:

    @staticmethod
    def bold(message):
        print(Colours.BOLD, message, Colours.END)

    @staticmethod
    def notify(message):
        print(Colours.CYAN, message, Colours.END)

    @staticmethod
    def confirm(message):
        print(Colours.PASS, message, Colours.END)

    @staticmethod
    def warning(message):
        print(Colours.WARNING, message, Colours.END)

    @staticmethod
    def fail(message):
        print(Colours.FAIL, message, EXIT_MESSAGE, Colours.END)


class FastQCManager:

    def __init__(self, file, directory, modules):
        print("FastQCManager")
        self.file = file
        self.directory = directory
        self.modules = modules

        # for module in self.modules:
        #     tag = md.get(module)
        #     with open()


def pull_data(file, module_name):

    filter_text = ''
    header = []
    table = []

    with open(file) as f:
        for line in f:
            line = line.lower()
            if line.startswith(ENTRY + module_name.lower()):
                filter_text = re.sub(ENTRY + module_name.lower() + '[\t]', '', line).strip('\n')
                break
        for line in f:
            if line.startswith(END_MODULE):
                break
            if line.startswith('#'):
                line = line.replace('#', '')
                header = line.replace('\n', '').split('\t')
            else:
                table.append(line.replace('\n', '').split('\t'))

    # print(table)
    return filter_text, header, table


def basic_statistics(file):

    data = pull_data(file, "Basic Statistics")
    header = data[HEADER]
    rows = data[ROWS]

    TerminalLog.notify("\nBasic Statistics:")
    TerminalLog.bold(tabulate(rows, headers=header))
