from pydicom.tag import Tag
from collections import namedtuple
Filter = namedtuple('Filter', ['id', 'description', 'value'])


def generate_tags(user_list):
    tags = {}
    for line in user_list:
        line = Filter(*line.split("\t"))
        tag = Tag([int(x, 16) for x in line.id.split(",")])  # Convert hex to int and get Tag
        tags[tag] = line.value
    return tags


def anonymise(ds, tags):
    for tag in tags.keys():
        try:
            value_cur = ds[tag].value
            value_new = tags[tag]

            print(f"{tag}: Found (replacing {value_cur} with {value_new})")
            ds[tag].value = value_new
        except KeyError:
            print(f"{tag}: Not found (KeyError)")
        except AttributeError:
            print(f"{tag}: Not found (AttributeError)")

    return ds

