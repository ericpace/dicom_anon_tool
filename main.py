import os
from collections import namedtuple
import anonymiser as anon
import pydicom
from pydicom.data import get_testdata_files
from pydicom.tag import Tag


Point = namedtuple('Point', ['x', 'y'])
Filter = namedtuple('Filter', ['id', 'description', 'value'])

# filename = "/Users/ericpace/Desktop/Work/PHY1/PHY1.Seq12.Ser11.Img0.dcm"
# filename = get_testdata_files("rtplan.dcm")[0]
filename = "test_anon.dcm"
ds = pydicom.dcmread(filename)




with open("user_tags.txt") as f:
    # Read each line
    data_elements = f.read().splitlines()


my_tags = anon.generate_tags(data_elements)

ds_anon = anon.anonymise(ds, my_tags)

ds_anon.save_as("test_anon.dcm")



print('finished')