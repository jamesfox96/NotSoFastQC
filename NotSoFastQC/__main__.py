import argparse
import os
from NotSoFastQC.utils import colours

EXIT_MESSAGE = '''\n===========================
                  \nINPUT ERROR: EXITING...
                  \n==========================='''


def get_options():

    parser = argparse.ArgumentParser()
    parser.add_argument('-I', required=True, help="input FastQC file path")
    parser.add_argument('-O', required=True, help="output directory path")
    parser.add_argument('--all', required=False, action='store_true',
                        help="Generates reports for all QC report modules")
    parser.add_argument('-M', required=False, nargs='*', default=[],
                        help='Input the QC report modules of your choice separated by a space')
    return parser.parse_args()


def validate_file(filename):

    path = os.path.abspath(filename)

    try:
        with open(path, 'r') as f:
            header = f.readline()
            if header.startswith("##FastQC"):
                print(f"{colours.CYAN}Valid FastQC file: ", path, f"{colours.END}")
                return path

            print(f"\n{colours.FAIL}", path, "\tFile is not FastQC format! ", EXIT_MESSAGE, f"{colours.END}")

    except IOError:
        print(f"\n{colours.FAIL}", path, "\nFile does not exist!", EXIT_MESSAGE, f"{colours.END}")

    exit()


def validate_dir(directory):

    path = os.path.abspath(directory)

    if os.path.isdir(path):
        print(f"{colours.CYAN}Valid output directory: ", path, f"{colours.END}")
        return path

    print(f"\n{colours.FAIL}", path, "\nDirectory does not exist!", EXIT_MESSAGE, f"{colours.END}")
    exit()


def main():

    print("This is NotSoFastQC!")

    args = get_options()

    if args.all is False:
        print("all = False")
        for arg in args.M:
            print(arg)
    else:
        print("all = True")
        args.M = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for arg in args.M:
            print(arg)

    fastqc = validate_file(args.I)
    dir = validate_dir(args.O)


if __name__ == '__main__':
    main()

