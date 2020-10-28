import argparse


def get_options():

    parser = argparse.ArgumentParser()
    parser.add_argument('-I', '--input', required=True, help="input FastQC file path")
    parser.add_argument('-O', '--output', required=True, help="output directory path")
    parser.add_argument('-A', '--all', required=False, action='store_true', help="input file path")
    parser.add_argument('-A', '--all', required=False, action='store_true', help="input file path")


def main():
    print("This is NotSoFastQC!")


if __name__ == '__main__':
    main()