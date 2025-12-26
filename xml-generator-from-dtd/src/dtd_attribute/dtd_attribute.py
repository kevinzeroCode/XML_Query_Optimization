from enum import IntEnum


class DTDAttributeValueType(IntEnum):
    """
    Defines the attribute-value of a DTD Attribute
    """
    NONE = 0
    VALUE = 1
    REQUIRED = 2
    IMPLIED = 3
    FIXED = 4


class DTDAttributeType(IntEnum):
    """
    Defines the attribute-type of a DTD Attribute
    """
    NONE = 0
    CDATA = 1
    Enumerated = 2
    ID = 3
    IDREF = 4
    IDREFS = 5
    NMTOKEN = 6
    NMTOKENS = 7
    ENTITY = 8
    ENTITIES = 9
    NOTATION = 10
    xml = 11


def convert_dtd_attribute_type_from_string(attribute_type: str) -> DTDAttributeType:
    return DTDAttributeType[attribute_type]


class DTDAttribute:
    """
    DTDAttribute represents a DTD attribute as per specification.
    The meaning of each field can be found on the following link:
    https://www.w3schools.com/xml/xml_dtd_attributes.asp
    Exception is the field self.value_type which is attribute-value according
    to the specification. The actual value, if such exists is stored in self.value
    """
    def __init__(self, element_name: str = "", attribute_name: str = "",
                 attribute_type: DTDAttributeType = DTDAttributeType.NONE,
                 value_type: DTDAttributeValueType = DTDAttributeValueType.NONE, value: str = ""):
        self.element_name = element_name
        self.attribute_name = attribute_name
        self.attribute_type = attribute_type
        self.value_type = value_type
        self.value = value
        self.enumerated_values = []

    # def _debug_print(self):
    #     print("Element: " + self.element_name)
    #     print("Attribute: " + self.attribute_name)
    #     print("Attribute Type: " + self.attribute_type.name)
    #     print("Value Type: " + self.value_type.name)
    #     print("Value: " + self.value)
    #     if self.attribute_type == DTDAttributeType.Enumerated:
    #         print("Enumerated values")
    #         print(self.enumerated_values)
    #     print()
