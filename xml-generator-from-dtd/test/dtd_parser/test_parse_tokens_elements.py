import unittest
from src.dtd_parser.dtd_parser import DTDParser
from src.project_path.project_path import ProjectPath
from src.dtd_element.dtd_element import DTDElementCount


class TestDTDParserParseTokensElements(unittest.TestCase):
    def setUp(self) -> None:
        self.dataPath = ProjectPath.get_project_data_dtd_path()

    def test_1element(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '1element.dtd')
        self.assertEqual(len(parser.elements["note"].sub_elements), 1)
        self.assertEqual(parser.elements["note"].element_name, "")
        self.assertEqual(parser.elements["note"].sub_elements[0].element_name, "#PCDATA")
        self.assertEqual(parser.elements["note"].sub_elements[0].sub_elements, [])

    def test_1comment_1element(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '1comment_1element.dtd')
        self.assertEqual(len(parser.elements.keys()), 1)

    def test_1complex_element(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '1complex_element.dtd')
        self.assertEqual(len(parser.elements["Department"].sub_elements), 3)
        self.assertEqual(parser.elements["Department"].element_name, "")

        self.assertEqual(parser.elements["Department"].sub_elements[0].element_name, "Title")
        self.assertEqual(parser.elements["Department"].sub_elements[0].occurrences, DTDElementCount.OnlyOne)
        self.assertEqual(parser.elements["Department"].sub_elements[0].sub_elements, [])

        self.assertEqual(parser.elements["Department"].sub_elements[1].element_name, "Course")
        self.assertEqual(parser.elements["Department"].sub_elements[1].occurrences, DTDElementCount.OneOrMore)
        self.assertEqual(parser.elements["Department"].sub_elements[1].sub_elements, [])

        self.assertEqual(parser.elements["Department"].sub_elements[2].element_name, "Lecturer")
        self.assertEqual(parser.elements["Department"].sub_elements[2].occurrences, DTDElementCount.ZeroOrOne)
        self.assertEqual(parser.elements["Department"].sub_elements[2].sub_elements, [])

    def test_nested_child_elements(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / 'nested_child_elements.dtd')
        self.assertEqual(len(parser.elements["D"].sub_elements), 2)
        self.assertEqual(parser.elements["D"].element_name, "")
        self.assertEqual(parser.elements["D"].occurrences, DTDElementCount.OneOrMore)

        self.assertEqual(parser.elements["D"].sub_elements[0].element_name, "A")
        self.assertEqual(parser.elements["D"].sub_elements[0].occurrences, DTDElementCount.ZeroOrOne)
        self.assertEqual(parser.elements["D"].sub_elements[0].sub_elements, [])

        self.assertEqual(len(parser.elements["D"].sub_elements[1].sub_elements), 2)
        self.assertEqual(parser.elements["D"].sub_elements[1].occurrences, DTDElementCount.ZeroOrMore)
        self.assertEqual(parser.elements["D"].sub_elements[1].element_name, "")

        self.assertEqual(parser.elements["D"].sub_elements[1].sub_elements[0].element_name, "B")
        self.assertEqual(parser.elements["D"].sub_elements[1].sub_elements[0].occurrences, DTDElementCount.OneOrMore)

    def test_complex_elements(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / 'complex_elements.dtd')
        self.assertEqual(len(parser.elements["Course_Catalog"].sub_elements), 1)
        self.assertEqual(len(parser.elements["Department"].sub_elements), 3)
        self.assertEqual(len(parser.elements["game"].sub_elements), 2)
