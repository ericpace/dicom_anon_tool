import os
from collections import namedtuple
import anonymiser as anon
import pydicom
from pathlib import Path
from pydicom.data import get_testdata_files
from pydicom.tag import Tag


Point = namedtuple('Point', ['x', 'y'])
Filter = namedtuple('Filter', ['id', 'description', 'value'])

filepath = "/Users/ericpace/Desktop/Work/PHY1/PHY1.Seq12.Ser11.Img0.dcm"
# filepath = get_testdata_files("rtplan.dcm")[0]
# filepath = "test_anon.dcm"
ds = pydicom.dcmread(filepath)

path = Path(filepath)

# TODO Add argparse to handle:
# 1. Input filename or file directory
# 2. Output filename or file directory
# 3. Location of user tags or void to use default list

# TODO Add logging function
# TODO Use Path properly



with open("user_tags.txt") as f:
    # Read each line
    data_elements = f.read().splitlines()


my_tags = anon.generate_tags(data_elements)

ds_anon = anon.anonymise(ds, my_tags)

ds_anon.save_as(os.path.join(path.parent, f"{path.stem}_anon.dcm"))



print('finished')