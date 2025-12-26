import unittest
from src.dtd_parser.dtd_parser import DTDParser
from src.project_path.project_path import ProjectPath


class TestDTDParserTokenizeElements(unittest.TestCase):
    def setUp(self) -> None:
        self.dataPath = ProjectPath.get_project_data_dtd_path()

    def test_1element(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '1element.dtd')
        self.assertEqual(len(parser._tokens), 1)

    def test_2nested_elements(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '2nested_elements.dtd')
        self.assertEqual(len(parser._tokens), 2)

    def test_5nested_elements(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '5nested_elements.dtd')
        self.assertEqual(len(parser._tokens), 5)

    def test_12elements(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '12elements.dtd')
        self.assertEqual(len(parser._tokens), 12)
