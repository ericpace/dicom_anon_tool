# DICOM Anonymisation Tool

Anonymises a DICOM directory, writing a new DCM file in the same location.

The script has a default list of tags to anonymise, but the user may point to a custom list.

```
usage: main.py [-h] [-t TAGFILE] [-i] source destination

Anonymise DICOM images

positional arguments:
  source                location of dicom file or folder to anonymise
  destination           Destination folder to save anonymised images

optional arguments:
  -h, --help            show this help message and exit
  -t TAGFILE, --tagfile TAGFILE
                        path to custom tags file
  -i, --intact          Leave filenames unchanged
```

## Usage example

```
main.py /Users/me//dcm/original/ /Users/me/Desktop/anonymised/ -t "user_tags.csv" -i
```