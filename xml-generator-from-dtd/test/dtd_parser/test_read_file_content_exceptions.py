import unittest
from src.dtd_parser.dtd_parser import DTDParser
from src.project_path.project_path import ProjectPath


class TestDTDParserReadFileContentExceptions(unittest.TestCase):
    def setUp(self) -> None:
        self.dataPath = ProjectPath.get_project_data_dtd_path()

    def test_file_not_found(self):
        parser = DTDParser()
        self.assertRaises(FileNotFoundError, parser.parse_file, self.dataPath / '.file_does_not_exist_gibberish.dtd.')

    def test_non_dtd_tags(self):
        parser = DTDParser()
        self.assertRaises(ValueError, parser.parse_file, self.dataPath / 'non_dtd_tags.dtd')
