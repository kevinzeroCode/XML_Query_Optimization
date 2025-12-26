import unittest
from src.dtd_parser.dtd_parser import DTDParser
from src.project_path.project_path import ProjectPath


class TestDTDParserParseTokensExceptions(unittest.TestCase):
    def setUp(self) -> None:
        self.dataPath = ProjectPath.get_project_data_dtd_path()

    def test_non_dtd_tags(self):
        parser = DTDParser()
        self.assertRaises(ValueError, parser.parse_file, self.dataPath / 'invalid_token.dtd')

    def test_invalid_element_children(self):
        parser = DTDParser()
        self.assertRaises(ValueError, parser.parse_file, self.dataPath / 'invalid_element_children.dtd')
