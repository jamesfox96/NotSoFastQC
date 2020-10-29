import argparse


def get_options():

    parser = argparse.ArgumentParser()
    parser.add_argument('-J', required=False, help="input FastQC file path")
    parser.add_argument('-O', required=False, help="output directory path")
    parser.add_argument('--all', required=False, action='store_true',
                        help="Generates reports for all QC report modules")
    parser.add_argument('-M', required=False, nargs='*', default=[],
                        help='Input the QC report modules of your choice separated by a space')
    return parser.parse_args()


def main():
    print("This is NotSoFastQC!")

    args = get_options()

    if args.all is False:
        print("all = False")
        for arg in args.M:
            print(arg)
    else:
        print("all == True")
        args.M = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for arg in args.M:
            print(arg)


if __name__ == '__main__':
    main()

