import os
import pydicom
from pydicom.tag import Tag
from collections import namedtuple
from pathlib import Path
import logging


Filter = namedtuple('Filter', ['id', 'description', 'value'])

ANON_LOG_FILE = "info.log"
logging.basicConfig(filename=ANON_LOG_FILE,
                    filemode='a',
                    format='%(asctime)s %(levelname)s \t %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)


def generate_tags(user_list):
    tags = {}
    for line in user_list:
        line = Filter(*line.split("\t"))
        tag = Tag([int(x, 16) for x in line.id.split(",")])  # Convert hex to int and get Tag
        tags[tag] = line.value
    return tags


def load_dicom_file(filepath):
    try:
        ds = pydicom.dcmread(os.path.join(filepath))
    except pydicom.errors.InvalidDicomError:
        print("invalid DICOM")
        logging.error("Invalid DICOM")
    return ds


def anonymise(ds, tags):
    for tag in tags.keys():
        try:
            value_cur = ds[tag].value
            value_new = tags[tag]

            print(f"{tag}: Found (replacing {value_cur} with {value_new})")
            logging.info(f"{tag}: Found (replacing {value_cur} with {value_new})")
            ds[tag].value = value_new
        except KeyError:
            print(f"{tag}: Not found (KeyError)")
            logging.error(f"{tag}: Not found (KeyError)")
        except AttributeError:
            print(f"{tag}: Not found (AttributeError)")
            logging.error(f"{tag}: Not found (AttributeError)")

    return ds


def start(filepath, tags):
    f = Path(filepath)
    ds = load_dicom_file(filepath)
    print(f"Opened file: {f}")
    logging.info(f"Opened file: {f}")

    ds_anon = anonymise(ds, tags)

    # TODO handle better
    savefile = os.path.join(f.parent, f"{f.stem}_anon.dcm")
    ds_anon.save_as(savefile)
    print(f"Saved file: {savefile}")
    logging.info(f"Saved file: {savefile}")
