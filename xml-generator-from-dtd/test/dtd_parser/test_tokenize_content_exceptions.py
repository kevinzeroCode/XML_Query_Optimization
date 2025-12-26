import unittest
from src.dtd_parser.dtd_parser import DTDParser
from src.project_path.project_path import ProjectPath


class TestDTDParserTokenizeExceptions(unittest.TestCase):
    def setUp(self) -> None:
        self.dataPath = ProjectPath.get_project_data_dtd_path()

    def test_empty_file(self):
        parser = DTDParser()
        self.assertRaises(ValueError, parser.parse_file, self.dataPath / 'empty_file.dtd')
        self.assertEqual(len(parser._tokens), 0)
        self.assertEqual(parser._content, "")

    def test_dtd_mixed_with_text(self):
        parser = DTDParser()
        self.assertRaises(ValueError, parser.parse_file, self.dataPath / 'dtd_mixed_with_text.txt')
        self.assertEqual(len(parser._tokens), 0)
