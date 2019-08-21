import os
import pydicom
from pydicom.tag import Tag
from collections import namedtuple
from pathlib import Path
import logging
from datetime import datetime


Filter = namedtuple('Filter', ['id', 'description', 'value', 'long_desc'])

ANON_LOG_FILE = f"{datetime.today().strftime('%Y-%m-%d_%H')}.log"
logging.basicConfig(filename=ANON_LOG_FILE,
                    filemode='a',
                    format='%(asctime)s %(levelname)s \t %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)


def generate_tags(user_list):
    tags = []
    for line in user_list:
        line = Filter(*line)
        tag = Tag([int(x, 16) for x in line.id.split(",")])  # Convert hex to int and get Tag
        tags.append(Filter(tag, line.description, line.value, line.long_desc))
    return tags


def load_dicom_file(filepath):
    try:
        return pydicom.dcmread(os.path.join(filepath))
    except pydicom.errors.InvalidDicomError:
        logging.error("Invalid DICOM")
        return None


def anonymise(ds, tags):
    for tag in tags:
        try:
            value_cur = ds[tag.id].value
            value_new = tag.value

            logging.info(f"{tag.id} {tag.description}: \t Found (replacing {value_cur} with {value_new})")
            ds[tag.id].value = value_new
        except KeyError:
            logging.error(f"{tag.id} {tag.description}: \t Not found (KeyError)")
        except AttributeError:
            logging.error(f"{tag.id} {tag.description}: \t Not found (AttributeError)")

    return ds


def start(filepath, tags):
    f = Path(filepath)
    ds = load_dicom_file(filepath)

    if ds:
        print(f"Open file: {f}")
        logging.info(f"Opened file: {f}")
        ds_anon = anonymise(ds, tags)

        # TODO handle better
        savefile = os.path.join(f.parent, f"{f.stem}_anon.dcm")
        ds_anon.save_as(savefile)
        print(f"Save file: {savefile}")
        logging.info(f"Saved file: {savefile}\n\n")
