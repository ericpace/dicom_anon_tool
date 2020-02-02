# DICOM Anonymisation Tool

This tool is designed to either:

1. Anonymise a single DICOM file, or
2. Anonymise a directory (recursively) of DICOM files

Anonymised files may be saved to a different directory, and may be renamed with `_anon` suffix.

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

To anonymise all DICOM files within directory named `original` and place output to 
a folder named `anonymised` using custom user tags and preserving the original filename

```
main.py /Users/me/dcm/original/ /Users/me/Desktop/anonymised/ -t "user_tags.csv" -i
```