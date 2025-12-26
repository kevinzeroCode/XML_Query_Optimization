import unittest
from src.dtd_parser.dtd_parser import DTDParser
from src.project_path.project_path import ProjectPath


class TestDTDParserFindRoot(unittest.TestCase):
    def setUp(self) -> None:
        self.dataPath = ProjectPath.get_project_data_dtd_path()

    def test_1element(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '1element.dtd')
        self.assertEqual(parser.get_root(), "note")

    def test_2nested_elements(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '2nested_elements.dtd')
        self.assertEqual(parser.get_root(), "note")

    def test_11elements_6attributes(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '11elements_6attributes.dtd')
        self.assertEqual(parser.get_root(), "Course_Catalog")

    def test_9elements_3attributes(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '9elements_3attributes.dtd')
        self.assertEqual(parser.get_root(), "games")

    def test_14elements_2attributes(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '14elements_2attributes.dtd')
        self.assertEqual(parser.get_root(), "Course_Catalog")
