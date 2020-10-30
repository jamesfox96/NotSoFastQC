from NotSoFastQC.modules import module_dict as md
import re
from tabulate import tabulate
from NotSoFastQC.utils import TerminalLog as Log

ENTRY = ">>"
END_MODULE = ">>END_MODULE"

FILTER_TEXT = 0
HEADER = 1
ROWS = 2


class FastQCManager:

    def __init__(self, validated_args):

        self.file = validated_args[0]
        self.directory = validated_args[1]
        self.modules = validated_args[2]


        # if len(self.modules) > 0:
        #
        # for module in self.modules:
        #     tag = md.get(module)
        #     with open()

        self.basic_statistics()

    def pull_data(self, module_name):

        filter_text = ''
        header = []
        table = []

        with open(self.file) as f:
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

    def basic_statistics(self):

        data = self.pull_data("Basic Statistics")
        header = data[HEADER]
        rows = data[ROWS]

        Log.notify("\nBasic Statistics:\n")
        Log.bold(tabulate(rows, headers=header))
