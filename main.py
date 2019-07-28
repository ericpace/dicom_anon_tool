import os
import argparse
from collections import namedtuple
import anonymiser as anon
import pydicom
from pathlib import Path

parser = argparse.ArgumentParser(description='Anonymise DICOM images')
parser.add_argument('source', metavar='S', type=str,
                    help='location of dicom file to anonymise')
parser.add_argument('-d', '--destination',
                    help='location where to save anonymised DICOM file')
parser.add_argument('-t', '--tagfile', default="user_tags.txt",
                    help='path to custom tags file')

args = parser.parse_args()

print(args.source, args.destination, args.tagfile)
Point = namedtuple('Point', ['x', 'y'])
Filter = namedtuple('Filter', ['id', 'description', 'value'])

# Other filepaths for testing
# filepath = "/Users/ericpace/Desktop/Work/PHY1/PHY1.Seq12.Ser11.Img0.dcm"
# filepath = get_testdata_files("rtplan.dcm")[0]
# filepath = "test_anon.dcm"


ds = pydicom.dcmread(args.source)

path = Path(args.source)

# TODO Add argparse to handle:
# 1. Input filename or file directory
# 2. Output filename or file directory
# 3. Location of user tags or void to use default list

# TODO Add logging function
# TODO Use Path properly


with open(args.tagfile) as f:
    # Read each line
    data_elements = f.read().splitlines()


my_tags = anon.generate_tags(data_elements)

ds_anon = anon.anonymise(ds, my_tags)

# TODO handle better
if not args.destination:
    ds_anon.save_as(os.path.join(path.parent, f"{path.stem}_anon.dcm"))
else:
    ds_anon.save_as(args.destination)


print('finished')
