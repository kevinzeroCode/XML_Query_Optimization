"""
Contains the XMLGenerator class
"""
import xml.etree.ElementTree as ET
from src.dtd_element.dtd_element import DTDElement
from src.dtd_parser.dtd_parser import DTDParser
from src.xml_document.xml_document import XMLDocument


class XMLGenerator:
    """
    XMLGenerator uses parsed DTD elements and attributes
    from dtd_parser object and generates an XML document
    in the form of a XMLDocument object
    """
    def __init__(self, parser: DTDParser):
        self._parser = parser
        self._root_name = parser.get_root()
        self._xml_document = XMLDocument()

    def get_xml(self) -> XMLDocument:
        """
        Get the converted XMLDocument
        :return: Generated XML from the parsed DTD as an XMLDocument
        """
        return self._xml_document

    def generate_xml(self) -> XMLDocument:
        """
        Generate an XML tree from the given parser in the constructor
        :return: Generated XML tree as an XMLDocument
        """
        self._xml_document = XMLDocument()
        self._xml_document.init_with_root(self._root_name)

        self._add_attributes_for_element(self._root_name)
        self._add_child_elements_for_element(self._root_name)

        return self._xml_document

    def _add_attributes_for_element(self, element_name: str) -> None:
        """
        Generate the XML attributes for a given element, the element with that name
        must be the last element with such name added, because attributes are added
        to the last element only
        :param element_name: the element for which to generate attributes
        """
        if element_name in self._parser.attributes.keys():
            for attr in self._parser.attributes[element_name]:
                self._xml_document.add_attribute(element_name, (attr.attribute_name, attr.value))

    def _add_child_elements_for_element(self, element_name: str) -> None:
        """
        Add child XML elements to the last added element_name in the XML tree
        Iterate all the direct children and call recursive add for each one
        :param element_name: element name for which to add child elements
        """
        if element_name in self._parser.elements.keys():
            children = self._parser.elements[element_name]
            if children.element_name == "":
                for child in children.sub_elements:
                    self._recursive_add_children(element_name, child)

    def _recursive_add_children(self, parent: str, child: DTDElement) -> None:
        """
        For a given parent element and child element:
            If the child is a simple child (has no sub-children), add it to the parent
            If the child is complex (has sub-elements), recursively add its children
        :param parent: The element to which the children must be added
        :param child: the current child being parsed
        """
        if child.element_name != "":
            if child.element_name == "#PCDATA":
                return
            self._xml_document.add_element(parent, child.element_name, "")
            self._add_attributes_for_element(child.element_name)
            self._add_child_elements_for_element(child.element_name)
        else:
            for sub_child in child.sub_elements:
                self._recursive_add_children(parent, sub_child)

    def to_string(self) -> str:
        """
        Convert the XML tree to string
        :return: the xml as a string, non-formatted
        """
        return str(ET.tostring(self._xml_document.get_root(), encoding="unicode", method="xml"))
