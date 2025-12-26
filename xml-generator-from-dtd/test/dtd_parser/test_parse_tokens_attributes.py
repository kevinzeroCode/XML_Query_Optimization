import unittest
from src.dtd_parser.dtd_parser import DTDParser
from src.project_path.project_path import ProjectPath
from src.dtd_attribute.dtd_attribute import DTDAttributeType, DTDAttributeValueType


def count_attributes(attributes: dict) -> int:
    return sum(len(attributes[attr]) for attr in attributes.keys())


class TestDTDParserParseTokensAttributes(unittest.TestCase):
    def setUp(self) -> None:
        self.dataPath = ProjectPath.get_project_data_dtd_path()

    def test_1element(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '1element.dtd')
        self.assertEqual(len(parser.elements), 1)
        self.assertEqual(count_attributes(parser.attributes), 0)

    def test_1element_1attribute(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '1element_1attribute.dtd')
        self.assertEqual(len(parser.elements), 1)
        self.assertEqual(count_attributes(parser.attributes), 1)

        self.assertEqual(parser.attributes["square"][0].attribute_name, "width")
        self.assertEqual(parser.attributes["square"][0].value, "0")
        self.assertEqual(parser.attributes["square"][0].attribute_type, DTDAttributeType.CDATA)
        self.assertEqual(parser.attributes["square"][0].value_type, DTDAttributeValueType.VALUE)

    def test_9elements_3attributes(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '9elements_3attributes.dtd')
        self.assertEqual(len(parser.elements.keys()), 9)
        self.assertEqual(count_attributes(parser.attributes), 3)

        self.assertEqual(parser.attributes["game"][0].value_type, DTDAttributeValueType.REQUIRED)
        self.assertEqual(len(parser.attributes["score"]), 2)

    def test_11elements_6attributes(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '11elements_6attributes.dtd')
        self.assertEqual(len(parser.elements.keys()), 11)
        self.assertEqual(count_attributes(parser.attributes), 6)

