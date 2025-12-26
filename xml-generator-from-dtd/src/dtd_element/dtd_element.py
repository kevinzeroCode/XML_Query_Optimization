from enum import IntEnum


class DTDElementCount(IntEnum):
    """
    DTDElementCount determines how many times an element can be used
    This
    """
    OnlyOne = 1
    OneOrMore = 2
    ZeroOrMore = 3
    ZeroOrOne = 4


class DTDElement:
    """
    DTDAttribute represents a DTD attribute as a name and how many
    times it can occur. The information about the children is kept
    in the DTD parser.
    """
    def __init__(self, element_name: str = "", occurrences: DTDElementCount = DTDElementCount.OnlyOne):
        self.element_name = element_name
        self.occurrences = occurrences
        self.sub_elements = []

    # def _debug_print(self):
    #     print("Element: " + self.element_name)
    #     print("Occurrences: " + self.occurrences.name)
    #     print("Sub elements:" + str(len(self.sub_elements)))
    #     print()
