import unittest
from src.dtd_parser.dtd_parser import DTDParser
from src.project_path.project_path import ProjectPath


class TestDTDParserParseString(unittest.TestCase):
    def test_1element(self):
        parser = DTDParser()
        parser.parse_string('<!ELEMENT note (#PCDATA)>')
        self.assertEqual(len(parser._tokens), 1)

    def test_1element_1attribute(self):
        parser = DTDParser()
        parser.parse_string('<!ELEMENT square EMPTY><!ATTLIST square width CDATA "0">')
        self.assertEqual(len(parser._tokens), 2)
