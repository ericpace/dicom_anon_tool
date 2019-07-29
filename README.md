# DICOM Anonymisation Tool

Anonymises a DICOM directory, writing a new DCM file in the same location.

The script has a default list of tags to anonymise, but the user may point to a custom list.


Usage: main.py [-h] [-t TAGFILE] source

Anonymise DICOM images

positional arguments:
  source                location of dicom file or folder to anonymise

optional arguments:
  -h, --help            show this help message and exit
  -t TAGFILE, --tagfile TAGFILE
                        path to custom tags file


