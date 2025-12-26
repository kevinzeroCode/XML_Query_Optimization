import unittest
from src.dtd_parser.dtd_parser import DTDParser
from src.project_path.project_path import ProjectPath


class TestDTDParserTokenizeAttributes(unittest.TestCase):
    def setUp(self) -> None:
        self.dataPath = ProjectPath.get_project_data_dtd_path()

    def test_1element_1attribute(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '1element_1attribute.dtd')
        self.assertEqual(len(parser._tokens), 2)

    def test_1element_6attributes(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '1element_6attributes.dtd')
        self.assertEqual(len(parser._tokens), 7)

    def test_1element_2attributes(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '1element_2attributes.dtd')
        self.assertEqual(len(parser._tokens), 3)

    def test_9elements_3attributes(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '9elements_3attributes.dtd')
        self.assertEqual(len(parser._tokens), 12)

    def test_11elements_6attributes(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '11elements_6attributes.dtd')
        self.assertEqual(len(parser._tokens), 17)
