"""
Contains methods used for parsing DTD files
"""
import re
from src.dtd_attribute.dtd_attribute import DTDAttribute, DTDAttributeType, DTDAttributeValueType, \
    convert_dtd_attribute_type_from_string
from src.dtd_element.dtd_element import DTDElement, DTDElementCount

# The prefix of a valid DTD element tag
DTD_ELEMENT_TAG_PREFIX = "<!ELEMENT"

# The prefix of a valid DTD attribute tag
DTD_ATTRIBUTE_TAG_PREFIX = "<!ATTLIST"

# The prefix of a DTD comment
DTD_COMMENT_PREFIX = "<!--"

# IMPLIED attribute-value-type
DTD_ATTRIBUTE_VALUE_IMPLIED = "#IMPLIED"

# REQUIRED attribute-value-type
DTD_ATTRIBUTE_VALUE_REQUIRED = "#REQUIRED"

# FIXED attribute-value-type
DTD_ATTRIBUTE_VALUE_FIXED = "#FIXED"


def _get_token_name(token: str) -> str:
    """
    Get the first element of a token separated by white space on both sides
    :param token: string representing DTD element or attribute, e.g. <!ELEMENT ...>
    :return: element-name split from a DTD token
    """
    splitter = r'\s+'
    return list(filter(None, re.split(splitter, token, 2)[1:-1]))[0]


def _split_on_whitespace(token: str, splits: int) -> list:
    """
    Split a token (string) on white space a number of times
    :param token: the string to split on whitespace
    :param splits: how many splits to do
    :return: list of split substrings from the token
    """
    splitter = r'\s+'
    return list(re.split(splitter, token, splits))


def _get_element_name_from_token(token: str) -> (str, str):
    """
    Retrieve the element name from a DTD attribute tag
    :param token: DTD attribute tag, e.g: <!ATTLIST element-name attribute-name ... >
    :return: (element-name, remainder of the token after element name)
    """
    split_element_name = _split_on_whitespace(token, 2)[1:]
    element_name = split_element_name[0]
    token_after_element_name = split_element_name[1]
    return element_name, token_after_element_name


def _get_attribute_name_from_token(token_after_element_name: str) -> (str, str):
    """
    Retrieve the attribute name from a DTD attribute tag
    The argument is the cut DTD tag after the element-name
    :param token_after_element_name: DTD attribute tag, e.g: attribute-name ... >
    :return: (attribute-name, remainder of the token after attribute-name)
    """
    split_attribute_name = _split_on_whitespace(token_after_element_name, 1)
    attribute_name = split_attribute_name[0]
    token_after_attribute_name = split_attribute_name[1]
    return attribute_name, token_after_attribute_name


def _parse_enumerated_attribute(token_after_attribute_name: str) -> DTDAttribute:
    """
    Parse an enumerated attribute enumerated values and default value
    :param token_after_attribute_name: DTD attribute tag after the attribute name
        e.g: (value1|value2) "default-value">
    :return: DTDAttribute everything set, except attribute_name or element_name
    """
    attribute = DTDAttribute()
    attribute.attribute_type = DTDAttributeType.Enumerated
    attribute.value_type = DTDAttributeValueType.VALUE

    # Split on regex which matches all of the symbols ( ) > |
    enumerated_values = list(filter(None, re.split(r'[)(>|]+', token_after_attribute_name)))

    # The values prior to the last are all possible enumerated values
    attribute.enumerated_values = [value.strip('" ') for value in enumerated_values[:-1]]

    # The default value is the last in the list
    attribute.value = enumerated_values[-1].strip('" ')

    # In case the element has no default value but is IMPLIED
    # or REQUIRED attribute value is set to be empty
    if attribute.value == DTD_ATTRIBUTE_VALUE_IMPLIED or\
            attribute.value == DTD_ATTRIBUTE_VALUE_REQUIRED:
        attribute.value = ""

    return attribute


def _get_attribute_type_from_token(token_after_attribute_name: str) -> (str, str):
    """
    Retrieve the attribute type from a DTD attribute tag
    The argument is the cut DTD tag after the attribute-name
    :param token_after_attribute_name: cut DTD attribute tag after the attribute-name
    :return: (attribute-type, remainder of the token after attribute-type)
    """
    split_type = _split_on_whitespace(token_after_attribute_name, 1)
    attribute_type = convert_dtd_attribute_type_from_string(split_type[0])
    token_after_attribute_type = split_type[1]
    return attribute_type, token_after_attribute_type


def _is_token_fixed(token_after_attribute_type: str) -> bool:
    """
    Determine if a token is of #FIXED type
    :param token_after_attribute_type: cut DTD attribute tag after the attribute-type
    :return: True if the token is if #FIXED type
    """
    return token_after_attribute_type.startswith(DTD_ATTRIBUTE_VALUE_FIXED)


def _is_token_required(token_after_attribute_type: str) -> bool:
    """
    Determine if a token is of #REQUIRED type
    :param token_after_attribute_type: cut DTD attribute tag after the attribute-type
    :return: True if the token is if #REQUIRED type
    """
    return token_after_attribute_type.startswith(DTD_ATTRIBUTE_VALUE_REQUIRED)


def _is_token_implied(token_after_attribute_type: str) -> bool:
    """
    Determine if a token is of #IMPLIED type
    :param token_after_attribute_type: cut DTD attribute tag after the attribute-type
    :return: True if the token is if #IMPLIED type
    """
    return token_after_attribute_type.startswith(DTD_ATTRIBUTE_VALUE_IMPLIED)


def _get_fixed_token_value(token_after_attribute_type: str) -> str:
    """
    Retrieve the value of a #FIXED DTD tag, which is the last part of the string before the >
    :param token_after_attribute_type: cut DTD attribute tag after the attribute-type
    :return: the value of a DTD tag
    """
    split_values = list(filter(None, re.split(r'[\s>]+', token_after_attribute_type)))
    value = split_values[1].strip('"')
    return value


def _get_default_token_value(token_after_attribute_type: str) -> str:
    """
    Retrieve the value of a default DTD tag, which is the last part of the string before the >
    :param token_after_attribute_type: cut DTD attribute tag after the attribute-type
    :return: the value of a DTD tag
    """
    split_values = list(filter(None, re.split(r'[>]+', token_after_attribute_type)))
    value = split_values[0].strip('"')
    return value


def _parse_non_enumerated_attribute(token_after_attribute_name: str) -> DTDAttribute:
    """
    Parse a NON-enumerated attribute enumerated values and default value
    :param token_after_attribute_name: DTD attribute tag after the attribute name
        e.g: (value1|value2) "default-value">
    :return: DTDAttribute everything set, except attribute_name or element_name
    """
    attribute = DTDAttribute()

    attribute_type, token_after_attribute_type = \
        _get_attribute_type_from_token(token_after_attribute_name)

    attribute.attribute_type = attribute_type

    if _is_token_fixed(token_after_attribute_type):
        attribute.value_type = DTDAttributeValueType.FIXED
        attribute.value = _get_fixed_token_value(token_after_attribute_type)
    elif _is_token_required(token_after_attribute_type):
        attribute.value_type = DTDAttributeValueType.REQUIRED
    elif _is_token_implied(token_after_attribute_type):
        attribute.value_type = DTDAttributeValueType.IMPLIED
    else:  # default value type
        attribute.value_type = DTDAttributeValueType.VALUE
        attribute.value = _get_default_token_value(token_after_attribute_type)

    return attribute


def _generate_child_tokens(token: str) -> list:
    """
    Given a DTD token, convert the child-elements list into a list of child-tokens.
    A child-token is either a DTD element name or one of the following symbols:
    * ? + ( )
    :param token: DTD element or attribute tag as a string
    :return: A list of child-tokens
    """
    splitter = r'\s'
    children_string = re.split(splitter, token, 2)
    children_string = list(filter(None, children_string))[2]
    children_string = children_string.strip(">")
    # child_token_splitter is a regex which splits the children string into tokens
    # a token is either a DTD element name or one of the following symbols:
    # * ? + ( ) ,
    child_token_splitter = r'[\+)(\,\*\?]|[^\+)(\,\*\?]+'
    child_tokens = re.findall(child_token_splitter, children_string)
    child_tokens = [x.strip(" ") for x in child_tokens]
    child_tokens = list(filter(None, child_tokens))

    return child_tokens


def _check_last_token_for_special_symbol(root: DTDElement, child_tokens: list) -> None:
    """
    Check the children list if there are any special symbols at the end:
    * at the end means the children-list can be repeated 0 or more times
    + at the end means the children-list can be repeated 1 or more times
    + at the end means the children-list can be repeated exactly 0 or 1 times
    :param root: represents the outermost parentheses of a child-element list
    :param child_tokens: list of child-tokens
    """
    if child_tokens[-1] == "+":
        root.occurrences = DTDElementCount.OneOrMore
        child_tokens.pop(-1)
    if child_tokens[-1] == "*":
        root.occurrences = DTDElementCount.ZeroOrMore
        child_tokens.pop(-1)
    if child_tokens[-1] == "?":
        root.occurrences = DTDElementCount.ZeroOrOne
        child_tokens.pop(-1)


def _validate_child_tokens_for_parentheses(child_tokens: list, token: str) -> None:
    """
    Check if the child-token list has valid starting and ending tokens ( )
    to initialize the root DTDElement
    :param child_tokens: list of child-tokens
    :param token: DTD element or attribute tag as a string
    """
    if child_tokens[0] != "(" or child_tokens[-1] != ")":
        raise ValueError("Invalid DTD element {}".format(token))


class DTDParser:
    """ DTD Parser
    A class which allows parsing of DTD, which is in the form of a string.
    The class can read the DTD from a file or the DTD can be directly passed
    as a string.
    To parse DTD from a file:
        parser = DTDParser()
        parser.parse_file('my_dtd_file.dtd')
    To parse DTD from a string:
        parser = DTDParser()
        parser.parse_string(my_dtd_string)
    """
    def __init__(self):
        # If the DTD is read from a file, _path stores that file's path
        self._path = ""

        # Contains the DTD as a string before being parsed
        self._content = ""

        # Dictionary of <element, parent-count>; parent-count is
        # the number of parents an element has
        self._parents_count = dict()

        # List of all DTD tags, be it element or attribute tag
        self._tokens = []

        # Dictionary of <element-name, attribute-list>;
        # attribute-list is a list storing all attributes, which
        # belong to element-name
        self.attributes = dict()

        # Dictionary of <element-name, element-children>;
        # element-children is a tree whose node is a DTDElement obj
        self.elements = dict()

    def parse_file(self, path) -> None:
        """
        Load a file from a path and parse its content
        :param path: path to the file to load
        """
        self._reset_state()
        self._path = path

        self._read_file_content()
        self._tokenize_content()
        self._parse_tokens()

    def parse_string(self, dtd_string: str) -> None:
        """
        Load a file from a path and parse its content
        :param dtd_string: a string containing DTD
        """
        self._reset_state()
        self._path = ""
        self._content = dtd_string

        self._tokenize_content()
        self._parse_tokens()

    def _reset_state(self) -> None:
        """
        CLear the object state in order to allow a new file to be loaded
        """
        self._path = None
        self._content = ""
        self._tokens = []
        self.elements = dict()
        self.attributes = dict()

    def _read_file_content(self) -> None:
        """
        Read the content of the file pointed by _path as a string
        """
        with open(self._path, "r", encoding="utf8") as file:
            self._content = file.read()

    def _tokenize_content(self) -> None:
        """
        Convert the content of the file to tokens which can then be parsed as
        valid elements or attributes.
        A token is each string enclosed in < and >
        Example token: <!ELEMENT note EMPTY>
        """
        self._validate_content()

        # xml_tags_regex matches every XML tag separately
        xml_tags_regex = r'<.*?>'
        self._tokens = re.findall(xml_tags_regex, self._content)

    def _parse_tokens(self) -> None:
        """
        Convert tokens (strings) into objects
        DTD Elements are converted into a dictionary with
            key: element name
            value: list of names of child elements
        DTD attributes are stored in a dictionary with
            key: element name, which this attribute belongs to
            value: list of DTDAttribute objects representing the parsed attributes
        """
        for token in self._tokens:
            if token.startswith(DTD_ELEMENT_TAG_PREFIX):
                self._add_element(token)
            elif token.startswith(DTD_ATTRIBUTE_TAG_PREFIX):
                self._add_attribute(token)
            elif token.startswith(DTD_COMMENT_PREFIX):
                pass
            else:
                raise ValueError("The content of file {} is invalid. Invalid token found: {}"
                                 .format(self._path, token))

    def _validate_content(self) -> None:
        """
        Validate the read content of a file to make sure it's
        valid DTD-looking file. A DTD-looking file is a file which consists
        of xml-tags, aka all the content is enclosed in < and >
        e.g <a><b></a>
        This does not check for closing tags or if the DTD tags are valid
        """
        if self._content == "":
            raise ValueError("There is no content to parse from file {}".format(self._path))

        # xml_file_regex matches a string consisting of xml tags
        xml_file_regex = r'^\s*<(.*?>\s*<)*.*?>\s*$'
        if not re.match(xml_file_regex, self._content):
            raise ValueError("The content of file {} is invalid DTD".format(self._path))

    def _add_element_to_parents_count(self, element_name: str) -> None:
        """
        Add a DTD element to the hashtable of <element, parent_count>
        Keeping count of the parents an element can have allows us
        to later determine which element is the root, if such exists.
        :param element_name: the element to add
        """
        if element_name not in self._parents_count.keys():
            self._parents_count[element_name] = 0

    def _add_element(self, token: str) -> None:
        """
        Parse a string, which is a DTD element, into a key-value pair
            key: element name
            value: child elements of this element
        :param token: string representing DTD element, e.g. <!ELEMENT ...>
        """
        element_name = _get_token_name(token)
        self._add_element_to_parents_count(element_name)
        children = self._get_token_children(token)
        self.elements[element_name] = children

    def _add_attribute(self, token: str) -> None:
        """
        Parse a string, which is a DTD attribute, into a key-value pair
            key: element name, which this attribute belongs to
            value: DTDAttribute object (the parsed attribute)
        :param token: string representing a DTD attribute, e.g. <!ATTLIST ...>
        """
        element_name, token_after_element_name = _get_element_name_from_token(token)
        attribute_name, token_after_attribute_name = \
            _get_attribute_name_from_token(token_after_element_name)

        if token_after_attribute_name.startswith('('):
            attribute = _parse_enumerated_attribute(token_after_attribute_name)
        else:
            attribute = _parse_non_enumerated_attribute(token_after_attribute_name)

        attribute.element_name = element_name
        attribute.attribute_name = attribute_name

        self._add_attribute_to_attributes_dictionary(attribute)

    def _add_attribute_to_attributes_dictionary(self, attribute: DTDAttribute) -> None:
        """
        Add and attribute to the self.attributes dictionary
        :param attribute: the attribute to add
        """
        if attribute.element_name not in self.attributes.keys():
            self.attributes[attribute.element_name] = []
        self.attributes[attribute.element_name].append(attribute)

    def _get_token_children(self, token: str) -> DTDElement:
        """
        Parse the child elements of a DTD element.
        Child elements are after the second whitespace
        :param token: string representing DTD element, e.g. <!ELEMENT ...>
        :return: list of all children of a DTD element
        """
        child_tokens = _generate_child_tokens(token)

        root = DTDElement()
        _check_last_token_for_special_symbol(root, child_tokens)

        if child_tokens[0] == "EMPTY":
            root.element_name = "EMPTY"
            return root

        _validate_child_tokens_for_parentheses(child_tokens, token)

        root = self._generate_children_tree_from_child_tokens(root, child_tokens)

        return root

    def _generate_children_tree_from_child_tokens(self, root: DTDElement,
                                                  child_tokens: list) -> DTDElement:
        """
        Given a root DTD element, which represents the outermost parentheses of
        a child-element list, and the parsed children list to child-tokens -
        Generate a tree of children (DTDElement objects) which represents the hierarchy of elements
        under the parent element.
        :param root: The root of the DTD children,
            represents the opening and closing parentheses ( )
        :param child_tokens: List of child-tokens, either a child element name or + ? * ( )
        :return: returns tree with the root with the children added to it
        """
        current_element = root
        parents_stack = []
        # Remove starting and ending parentheses, because the root is created manually
        child_tokens.pop(0)
        child_tokens.pop(-1)

        for child_token in child_tokens:
            if child_token == ",":
                pass
            elif child_token == "*":
                current_element.sub_elements[-1].occurrences = DTDElementCount.ZeroOrMore
            elif child_token == "+":
                current_element.sub_elements[-1].occurrences = DTDElementCount.OneOrMore
            elif child_token == "?":
                current_element.sub_elements[-1].occurrences = DTDElementCount.ZeroOrOne
            elif child_token == "(":
                new_child = DTDElement()
                current_element.sub_elements.append(new_child)
                parents_stack.append(current_element)
                current_element = current_element.sub_elements[-1]
            elif child_token == ")":
                current_element = parents_stack[-1]
                parents_stack.pop(-1)
            else:
                self._add_element_to_parents_count(child_token)
                self._parents_count[child_token] += 1
                new_child = DTDElement(child_token)
                current_element.sub_elements.append(new_child)

        return root

    def get_root(self) -> str:
        """
        Find the root element of the DTD
        :return: the name of the root element of the DTD, if such exists
        """
        for x in self._parents_count.keys():
            if self._parents_count[x] == 0:
                return x
        raise ValueError("No root exists for the provided DTD")

        # def _debug_print_attributes(self) -> None:
        #     """
        #     Print debug information about the attributes parsed on stdout
        #     """
        #     for i in self.attributes.keys():
        #         for k in self.attributes[i]:
        #             k._debug_print()
        #
        # def _debug_print_elements(self) -> None:
        #     """
        #     Print debug information about the elements parsed on stdout
        #     """
        #     for i in self.elements.keys():
        #         print("Element: " + i + ", Children: ", end="")
        #         print(self.elements[i])
