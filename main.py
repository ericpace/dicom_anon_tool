import os
import argparse
from collections import namedtuple
import anonymiser as anon
import pydicom
from pathlib import Path


# Other filepaths for testing
# filepath = "/Users/ericpace/Desktop/Work/PHY1/PHY1.Seq12.Ser11.Img0.dcm"
# filepath = get_testdata_files("rtplan.dcm")[0]
# filepath = "test_anon.dcm"


parser = argparse.ArgumentParser(description='Anonymise DICOM images')
parser.add_argument('source', metavar='S', type=str,
                    help='location of dicom file to anonymise')
# parser.add_argument('-d', '--destination',
#                     help='location where to save anonymised DICOM file')
parser.add_argument('-t', '--tagfile', default="user_tags.txt",
                    help='path to custom tags file')

args = parser.parse_args()
sourcepath = Path(args.source)

Filter = namedtuple('Filter', ['id', 'description', 'value'])

with open(args.tagfile) as f:
    # Read each line
    data_elements = f.read().splitlines()

my_tags = anon.generate_tags(data_elements)

if sourcepath.is_dir():
    for root, dirs, files in os.walk(sourcepath):
        for file in files:
            anon.start(os.path.join(root, file), my_tags)
else:
    anon.start(args.source, my_tags)

print('finished')
