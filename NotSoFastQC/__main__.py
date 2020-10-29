import argparse


def get_options():

    parser = argparse.ArgumentParser()
    parser.add_argument('-I', '--input', required=False, help="input FastQC file path")
    parser.add_argument('-O', '--output', required=False, help="output directory path")
    parser.add_argument('-A', '--all', required=False, action='store_true',
                        help="Generates reports for all QC report modules")
    parser.add_argument('-M', '--modules', required=False,
                        help='Input the QC report modules of your choice, separated by a comma \',\':'
                             '\r\t1 - Per base sequence quality score'
                             '\r\t2 - Per tile sequence quality'
                             '\r\t3 - Per sequence quality scores'
                             '\r\t4 - Per base sequence content'
                             '\r\t5 - Per sequence GC content'
                             '\r\t6 - Per base N content'
                             '\r\t7 - Sequence Length Distribution'
                             '\r\t8 - Sequence Duplication Levels'
                             '\r\t9 - Overrepresented sequences'
                             '\r\t10 - Adapter Content'
                             '\r\t11 - K-mer Content'
                        )
    return parser.parse_args()


def main():
    print("This is NotSoFastQC!")

    args = get_options()


if __name__ == '__main__':
    main()

