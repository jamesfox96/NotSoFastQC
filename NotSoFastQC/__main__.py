import argparse
import os
from NotSoFastQC.utils import TerminalLog as Log
from NotSoFastQC.modules import module_dict as md
from NotSoFastQC.fastqc_manager import FastQCManager


def get_options():

    parser = argparse.ArgumentParser()
    parser.add_argument('-I', required=True, help="input FastQC file path")
    parser.add_argument('-O', required=True, help="output directory path")
    parser.add_argument('--all', required=False, action='store_true',
                        help="Generates reports for all QC report modules")
    parser.add_argument('-M', required=False, nargs='*', default=[], type=int,
                        help='Input the QC report module keys of your choice separated by a space')
    parser.add_argument('-D', required=False, default=False, action='store_true',
                        help="Determine whether you want to overwrite existing files in output directory")
    return parser.parse_args()


def validate_file(filename):

    path = os.path.abspath(filename)

    try:
        with open(path, 'r') as f:
            header = f.readline()
            if header.startswith("##FastQC"):
                Log.confirm("Valid FastQC file: " + path)
                return path

            Log.fail("\n" + path + "\nFile is not FastQC format!")

    except IOError:
        Log.fail("\n" + path + "\nFile does not exist!")

    exit()


def validate_dir(directory):

    path = os.path.abspath(directory)

    if os.path.isdir(path):
        Log.confirm("Valid output directory: " + path)
        return path

    Log.fail("\n" + path + "\nDirectory does not exist!")
    exit()


def validate_modules(modules):

    valid_modules = []
    invalid_count = 0

    for module in modules:
        if module in md.keys():
            Log.confirm("Module added - [" + str(module) + "] " + md.get(module))
            valid_modules.append(module)
        else:
            Log.warning("INVALID MODULE KEY [" + str(module) + "] REMOVED")
            invalid_count += 1

    if invalid_count > 0:
        Log.warning("Found " + str(invalid_count) + " invalid module key/s.")
        Log.notify("\tConsult documentation for help on module keys.")
    else:
        Log.confirm("Found no invalid module keys")

    return valid_modules


def run_validation(args):

    Log.notify("CONFIRMING INPUTS...\n")
    fastqc = validate_file(args.I)
    directory = validate_dir(args.O)

    if args.all is False:
        modules = validate_modules(args.M)
    else:
        modules = md.keys()
        Log.confirm("All available modules added.")

    Log.notify("VALIDATION COMPLETE...\n\n")

    return fastqc, directory, modules


def main():

    args = get_options()

    Log.start()

    validated_args = run_validation(args)
    FastQCManager(validated_args, args.D)

    Log.complete()


if __name__ == '__main__':
    main()
