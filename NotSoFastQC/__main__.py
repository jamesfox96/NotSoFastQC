import argparse
import os
from NotSoFastQC.utils import TerminalLog as log
from NotSoFastQC.utils import FastQCManager, basic_statistics
from NotSoFastQC.modules import module_dict as md


def get_options():

    parser = argparse.ArgumentParser()
    parser.add_argument('-I', required=True, help="input FastQC file path")
    parser.add_argument('-O', required=True, help="output directory path")
    parser.add_argument('--all', required=False, action='store_true',
                        help="Generates reports for all QC report modules")
    parser.add_argument('-M', required=False, nargs='*', default=[], type=int,
                        help='Input the QC report module keys of your choice separated by a space')
    return parser.parse_args()


def validate_file(filename):

    path = os.path.abspath(filename)

    try:
        with open(path, 'r') as f:
            header = f.readline()
            if header.startswith("##FastQC"):
                log.confirm("Valid FastQC file: " + path)
                return path

            log.fail("\n" + path + "\nFile is not FastQC format!")

    except IOError:
        log.fail("\n" + path + "\nFile does not exist!")

    exit()


def validate_dir(directory):

    path = os.path.abspath(directory)

    if os.path.isdir(path):
        log.confirm("Valid output directory: " + path)
        return path

    log.fail("\n" + path + "\nDirectory does not exist!")
    exit()


def validate_modules(modules):

    valid_modules = []
    invalid_count = 0

    for module in modules:
        if module in md.keys():
            log.confirm("Module added - " + md.get(module))
            valid_modules.append(module)
        else:
            log.warning("INVALID MODULE KEY - '" + str(module) + "'")
            invalid_count += 1

    log.notify("Found " + str(invalid_count) + " invalid module key/s.")
    if invalid_count > 0:
        log.notify("\tConsult documentation for help on module keys.")

    return valid_modules


def main():

    args = get_options()

    log.bold("\n\nThis is NotSoFastQC!\n\tCreated by James Fox\n\n")

    log.notify("CONFIRMING INPUTS...")
    fastqc = validate_file(args.I)
    directory = validate_dir(args.O)

    if args.all is False:
        modules = validate_modules(args.M)
    else:
        modules = md.keys()
        log.confirm("All available modules added.")

    if len(modules) > 0:
        FastQCManager(fastqc, directory, modules)

    basic_statistics(fastqc)


if __name__ == '__main__':
    main()

