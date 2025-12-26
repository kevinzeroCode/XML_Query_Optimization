import unittest
from src.dtd_parser.dtd_parser import DTDParser
from src.project_path.project_path import ProjectPath
from src.xml_generator.xml_generator import XMLGenerator


class TestXMLGenerator(unittest.TestCase):
    def setUp(self) -> None:
        self.dataPath = ProjectPath.get_project_data_dtd_path()

    def test_1element(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '1element.dtd')
        generator = XMLGenerator(parser)
        generator.generate_xml()
        self.assertEqual(generator.to_string(), '<note />')
        self.assertEqual(generator.get_xml().get_root().tag, 'note')

    def test_2nested_elements(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '2nested_elements.dtd')
        generator = XMLGenerator(parser)
        generator.generate_xml()
        self.assertEqual(generator.to_string(), '<note><heading /></note>')

    def test_1element_1attribute(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '1element_1attribute.dtd')
        generator = XMLGenerator(parser)
        generator.generate_xml()
        self.assertEqual(generator.to_string(), '<square width="0" />')

    def test_5nested_elements(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '5nested_elements.dtd')
        generator = XMLGenerator(parser)
        generator.generate_xml()
        self.assertEqual(generator.to_string(), '<note><to /><from /><heading /><body /></note>')

    def test_1element_6attributes(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '1element_6attributes.dtd')
        generator = XMLGenerator(parser)
        generator.generate_xml()
        self.assertEqual(generator.to_string(), '<square width="0" number="" fax="" company="Microsoft" type="cash" '
                                                'title="Mr or Mrs" />')

    def test_11elements_6attributes(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '11elements_6attributes.dtd')
        generator = XMLGenerator(parser)
        generator.generate_xml()
        self.assertEqual(generator.to_string(), '<Course_Catalog Year="2017-2018"><Department Code=""><Title '
                                                '/><Course Number=""><Title /><Description><Courseref Number="" '
                                                '/></Description></Course><Lecturer InstrID=""><First_Name '
                                                '/><Middle_Initial /><Last_Name '
                                                '/></Lecturer></Department></Course_Catalog>')

    def test_9elements_3attributes(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '9elements_3attributes.dtd')
        generator = XMLGenerator(parser)
        generator.generate_xml()
        self.assertEqual(generator.to_string(), '<games><game score=""><home-team /><ex-team /><scores><score time="" '
                                                'type=""><player /></score></scores><yellows><player '
                                                '/></yellows><reds><player /></reds></game></games>')

    def test_14elements_2attributes(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / '14elements_2attributes.dtd')
        generator = XMLGenerator(parser)
        generator.generate_xml()
        self.assertEqual(generator.to_string(), '<Course_Catalog><Department Code=""><Title '
                                                '/><Chair><Professor><First_Name /><Middle_Initial /><Last_Name '
                                                '/></Professor></Chair><Course CourseNumber=""><Title /><Description '
                                                '/><Instructors><Lecturer><First_Name /><Middle_Initial /><Last_Name '
                                                '/></Lecturer><Professor><First_Name /><Middle_Initial /><Last_Name '
                                                '/></Professor></Instructors><Prerequisites><Prereq '
                                                '/></Prerequisites></Course></Department></Course_Catalog>')

    def test_nested_child_elements(self):
        parser = DTDParser()
        parser.parse_file(self.dataPath / 'nested_child_elements.dtd')
        generator = XMLGenerator(parser)
        generator.generate_xml()
        self.assertEqual(generator.to_string(), '<D><A /><B /><C /></D>')
