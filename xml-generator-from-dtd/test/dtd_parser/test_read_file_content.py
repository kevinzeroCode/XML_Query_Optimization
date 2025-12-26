import unittest
from src.dtd_parser.dtd_parser import DTDParser
from src.project_path.project_path import ProjectPath


class TestDTDParserReadFileContent(unittest.TestCase):
    def setUp(self) -> None:
        self.dataPath = ProjectPath.get_project_data_dtd_path()

    def test_1element(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '1element.dtd')
        self.assertEqual(parser._content.strip(), "<!ELEMENT note (#PCDATA)>")

    def test_2nested_elements(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '2nested_elements.dtd')
        self.assertEqual(parser._content.strip(), "<!ELEMENT note (heading)>\n<!ELEMENT heading (#PCDATA)>")

    def test_1element_1attribute(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '1element_1attribute.dtd')
        self.assertEqual(parser._content.strip(), "<!ELEMENT square EMPTY>\n<!ATTLIST square width CDATA \"0\">")
