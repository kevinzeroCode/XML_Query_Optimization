import unittest
from src.dtd_parser.dtd_parser import DTDParser
from src.project_path.project_path import ProjectPath


class TestDTDParserFindRootExceptions(unittest.TestCase):
    def setUp(self) -> None:
        self.dataPath = ProjectPath.get_project_data_dtd_path()

    def test_no_root(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / 'no_root.dtd')
        self.assertRaises(ValueError, parser.get_root)

