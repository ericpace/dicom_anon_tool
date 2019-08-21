#! /usr/bin/python

import os
import csv
import argparse
import anonymiser as anon
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description='Anonymise DICOM images')
    parser.add_argument('source', type=str,
                        help='location of dicom file or folder to anonymise')
    parser.add_argument('-t', '--tagfile', default="user_tags.csv",
                        help='path to custom tags file')

    args = parser.parse_args()
    sourcepath = Path(args.source)


    data_elements = []
    with open(args.tagfile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            data_elements.append(row)

    my_tags = anon.generate_tags(data_elements)

    if sourcepath.is_dir():
        for root, dirs, files in os.walk(sourcepath):
            for file in files:
                anon.start(os.path.join(root, file), my_tags)
    else:
        anon.start(args.source, my_tags)


if __name__ == '__main__':
    main()
    print('finished')
