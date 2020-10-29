import argparse


def get_options():

    parser = argparse.ArgumentParser()
    parser.add_argument('-I', '--input', required=True, help="input FastQC file path")
    parser.add_argument('-O', '--output', required=True, help="output directory path")
    parser.add_argument('-A', '--all', required=False, action='store_true',
                        help="Generates reports for all QC report modules")
    parser.add_argument('-M', '--modules', required=False,
                        help='''Input the QC report modules of your choice, separated by a comma \',\':'
                             '\n\t1 - Per base sequence quality score'
                             '\n\t2 - Per tile sequence quality'
                             '\n\t3 - Per sequence quality scores'
                             '\n\t4 - Per base sequence content'
                             '\n\t5 - Per sequence GC content'
                             '\n\t6 - Per base N content'
                             '\n\t7 - Sequence Length Distribution'
                             '\n\t8 - Sequence Duplication Levels'
                             '\n\t9 - Overrepresented sequences'
                             '\n\t10 - Adapter Content'
                             '\n\t11 - K-mer Content'''
                        )
    return parser.parse_args()


def main():
    print("This is NotSoFastQC!")

    args = get_options()


if __name__ == '__main__':
    main()

