"""
XML generated from https://json-generator.com/
and convert with https://www.freeformatter.com/json-to-xml-converter.html#before-output
"""
import os
from uuid import UUID
from typing import List
from dataclasses import dataclass, fields, asdict
import xml.etree.ElementTree as ET
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
PATH_TO_XML_FILE = f"{BASE_DIR}/statics/random.xml"


@dataclass
class User:
    _id: str
    about: str
    address: str
    age: int
    balance: float
    company: str
    email: str
    eyeColor: str
    favoriteFruit: str
    gender: str
    guid: UUID
    isActive: bool
    name: str
    tags: list


class XmlParser:
    def __init__(self, path: str, dataclass: dataclass):
        if not os.path.isfile(path):
            print(f"ERROR: File {path} does not exist.")
        self.tree = ET.parse(path)
        print(f"INFO: File {path} has been parsed successfully.")
        self.dataclass = dataclass
        # self.dataclass_fields = {'_id': <class 'str'>, 'about': <class 'str'>, 'address': <class 'str'> ...}
        self.dataclass_fields = {field.name: field.type for field in fields(dataclass)}


    def create_dataclass(self):
        print(f"INFO: Starting parsing data into type {self.dataclass.__name__}.")
        root = self.tree.getroot()
        dataclasses = []
        for element in root:
            # Reading element one-be-one
            item_dict = {}

            for value in element:
                if value.tag in self.dataclass_fields.keys():
                    # Read the data's type
                    field_type = self.dataclass_fields[value.tag]
                    if field_type is list:
                        # Oh, it is a list, we must iterate through all the values
                        item_dict[value.tag] = self._iter_through_list(value)
                    else:
                        item_dict[value.tag] = field_type(value.text)

            dataclasses.append(
                self.dataclass(**item_dict)
            )
        return dataclasses

    def _iter_through_list(self, element):
        tmp_list = []
        for list_item in element:
            tmp_list.append(list_item.text)
        return tmp_list
