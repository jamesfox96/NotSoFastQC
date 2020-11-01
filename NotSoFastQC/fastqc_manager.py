import re
import os
import csv
import shutil
from tabulate import tabulate
from NotSoFastQC.modules import module_dict as md
from NotSoFastQC.utils import TerminalLog as Log

ENTRY = ">>"
END_MODULE = ">>END_MODULE"

FILTER_TEXT = 0
HEADER = 1
ROWS = 2


class FastQCManager:

    def __init__(self, validated_args, overwrite):

        self.file = validated_args[0]
        self.directory = validated_args[1]
        self.modules = validated_args[2]

        Log.notify("STARTING MODULE REPORTS...\n")
        for module in self.modules:
            self.module_name = md.get(module)
            self.working_path = os.path.join(self.directory, self.module_name.replace(' ', '_'))
            self.build_directory(overwrite)

            data = self.pull_data(self.module_name)
            self.write_reports(data)

        self.basic_statistics()

    def write_reports(self, data):

        with open(os.path.join(self.working_path, "filter.txt"), 'w') as file:
            file.write(data[FILTER_TEXT])

        with open(os.path.join(self.working_path, "QC_report.txt"), 'w') as file:
            tsv_output = csv.writer(file, delimiter='\t')
            tsv_output.writerow(data[HEADER])
            for row in data[ROWS]:
                tsv_output.writerow(row)

        Log.confirm("Report files successfully created for module ["
                    + self.module_name + "]")

    def build_directory(self, overwrite):

        try:
            Log.notify("Building directory [" + self.working_path + "]...")
            os.mkdir(self.working_path)
        except FileExistsError:
            if overwrite:
                Log.warning("Directory already exists. [-D] selected, deleting existing directory...")
                shutil.rmtree(self.working_path)
                os.mkdir(self.working_path)
            else:
                Log.fail("\n Folder in output directory named [" + self.working_path + "] already exists."
                         "\n Please choose an empty working directory to avoid this problem or select "
                         "[-D] as a parameter to overwrite pre-existing files.")
                quit()

        Log.confirm("Directory [" + self.working_path + "] created.")

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
