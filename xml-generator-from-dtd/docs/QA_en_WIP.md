# XML Generator from DTD

## Authors

Ivan Luchev (https://github.com/luchev)

Lyuboslav Karev (https://github.com/lyubolp)

Faculty of mathematics and informatics Sofia University

Course: Software quality assurance

## Project description

The project is a web application which allows the user to input a valid DTD file and generate XML corresponding to that DTD, opening it in a web code editor for the user to continue editing.

Some specifically formatted DTDs have the option to be used as a template for a Wikipedia page. If the user has such a DTD, they can specify a Wiki page and what info they want to pull from that page. When generating the XML in this case it will also be filled with the information from the Wiki page.

## Introduction to the QA part of the project

The project is written in **python**. The testing is done using the python module **unittest**. In total there are **47 unit-tests**, which test all of the 9 modules in the project. The overall code coverage is **90%**, as 9/7 of the modules have 100% coverage. The remaining 2 files have untested methods, but they are not used anywhere in the project and exist only to complete the API the components, these methods belong to, provide. The testing done is **white-box testing**, because the project is very complex and there are a lot of staged of computation, which remain unknown to the end users. However all of these stages of the project have to work correctly so the user can use the final finished product effectively. Having so many hidden methods and overall computations in many hidden layers it would be incredibly hard to find bugs had we used black-box testing, because there are tens of methods being called between what the user sees as a GUI and the data being read and parsed. Hence we check the correctness of the program on each possible layer.

Test results: https://qa-xml-test-results.netlify.com/

## How were the tests written

The tests were written so they cover every possible path in the code execution, if we model the code as a graph from functions, methods, classes and if-else blocks. The tests start from the simplest and most basic methods like reading a file and checking its content and gradually build up to more complex methods, which rely on the simpler ones, such as generating a whole XML tree from parsed DTD objects. Most of these methods are protected/private and they are not usually accessible from outside the class/package they are in, however python allows us to break the encapsulation and have full access to protected/private methods and data fields. If we look at the program as a list of functionalities A -> B -> C -> ... (e.g read file -> check file content for errors -> parse content as DTD -> ...), first the functionality A is being tested, then B is tested (which relies on the correctness of A) and so on. Each possible middle point of the program execution is tested in order. To achieve this we have used the call-stack of the functionalities, to determine which function calls which. Here's an example of one such call-stack. On it we can see the functions at the bottom do not depend on anything else, so they are the first to be tested for correctness. Once we are certain they are covered and work properly we can start with the next set of functions (on the upper level in the graph), which depend on these basic functions, which we have already tested. This way going up the graph we check that each level works correctly before moving up to the next (more complex) one. This can be seen as doing a Width first traversal of the graph starting from the leaves and moving to the root.

![](https://imgur.com/NrSWhrN.png)

https://imgur.com/OCRNiWV

https://imgur.com/rjh86MX

https://imgur.com/NrSWhrN

## Achieving full data coverage

To make sure that we have tested every possible functionality and all possible input for the application we split the input into equivalence classes, which cover all the possible inputs the program can get. Because our program works with files/strings, which must represent valid DTD documents, in general we have the following equivalence classes:

- file, which doesn't exist
- empty file
- file with invalid data
- file with partially valid data
- file with completely valid data

These classes also apply when the input is a string, because the first thing our program does is read the file to a string. Furthermore, to test certain a functionality we need to split these equivalence classes into sub-classes.  For example the above equivalence classes are important when reading a file/string. However after we have the string and we make sure it is from the class with completely valid data, we have to continue more specific testing, in particular - splitting the data into valid tags (DTD element/attribute tags). This means that the class 'completely valid data' can be split even more into:

- 1 DTD element
- 1 DTD attribute
- 1 element and 1 attribute
- multiple elements and 1 attribute
- 1 element and multiple attributes
- multiple elements and multiple attributes

and so on.

This way on each level of the call-stack we split the tests into different classes to make sure every possible input to that level is tested.

## Achieving full code coverage

To make sure the program has full code coverage, we have used **coverage.py**, to generate information about the lines which are covered by the tests and which aren't.

Code coverage results: https://qa-xml-coverage.netlify.com/

## Conclusion

All functionalities necessary for the project to function properly have been extensively tested. Some functionalities, which are not used by the project are left untested, however these functionalities are only there to complete the API of certain classes/interfaces of the program. This way we achieve 100% code coverage for the application and 90% code coverage for the code as a whole.

Всички функционалности необходими на проекта да работи и всички функционалности, които проектът използва са тествани. Някой функционалности, които не се използват са оставени нетествани, но те съществуват, за да имат пълнота интерфейсите на софтуера. По този начин постигаме 100% покритие на проекта с тестове и 90% покритие на кода.

## Detailed test description

### dtd_parser

#### test_read_file_content

##### test_1element

| Description            | Test reading a DTD file with 1 DTD element       |                                                              |
| ---------------------- | ------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                             |                                                              |
| **Test step**          | **Description**                                  | **Expected result**                                          |
| 1                      | Create DTD parser object                         | A new DTD parser object is created                           |
| 2                      | Read file 1element.dtd                           | The file 1element.dtd is read into the object memory         |
| 3                      | Verify the content of the file is read correctly | The file content read from the file in the object is the same as the actual file |

##### test_2nested_elements

| Description            | Test reading a DTD file with 2 nested in each other DTD elements |                                                              |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                         |                                                              |
| **Test step**          | **Description**                                              | **Expected result**                                          |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                           |
| 2                      | Read file 2nested_elements.dtd                               | The file 2nested_elements.dtd is read into the object memory |
| 3                      | Verify the content of the file is read correctly             | The file content read from the file in the object is the same as the actual file |

##### test_1element_1attribute

| Description            | Test reading a DTD file with 1 element and 1 attribute |                                                              |
| ---------------------- | ------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                   |                                                              |
| **Test step**          | **Description**                                        | **Expected result**                                          |
| 1                      | Create DTD parser object                               | A new DTD parser object is created                           |
| 2                      | Read file 1element_1attribute.dtd                      | The file 1element_1attribute.dtd is read into the object memory |
| 3                      | Verify the content of the file is read correctly       | The file content read from the file in the object is the same as the actual file |

#### test_read_file_content_exceptions

##### test_non_dtd_tags

| Description            | Test reading a file which has invalid DTD tags               |                                                              |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                         |                                                              |
| **Test step**          | **Description**                                              | **Expected result**                                          |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                           |
| 2                      | Verify that reading file invalid_token.dtd raises a Value Error | Reading the file invalid_token.dtd the DTD parser raises a Value Error |

##### test_invalid_element_children

| Description            | Test reading a DTD file which has invalid children elements  |                                                              |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                         |                                                              |
| **Test step**          | **Description**                                              | **Expected result**                                          |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                           |
| 2                      | Verify that reading file invalid_element_children.dtd raises a Value Error | Reading the file invalid_element_children.dtd the DTD parser raises a Value Error |

#### test_tokenize_content_elements

##### test_1element

| Description            | Test generating DTD tokens from a file with 1 element |                                                      |
| ---------------------- | ----------------------------------------------------- | ---------------------------------------------------- |
| **Initial conditions** | None                                                  |                                                      |
| **Test step**          | **Description**                                       | **Expected result**                                  |
| 1                      | Create DTD parser object                              | A new DTD parser object is created                   |
| 2                      | Read file 1element.dtd                                | The file 1element.dtd is read into the object memory |
| 3                      | Verify the parser has generated 1 DTD tokens          | The parser has generated 1 DTD tokens                |

##### test_2nested_elements

| Description            | Test generating DTD tokens from a file with 2 element |                                                              |
| ---------------------- | ----------------------------------------------------- | ------------------------------------------------------------ |
| **Initial conditions** | None                                                  |                                                              |
| **Test step**          | **Description**                                       | **Expected result**                                          |
| 1                      | Create DTD parser object                              | A new DTD parser object is created                           |
| 2                      | Read file 2nested_elements.dtd                        | The file 2nested_elements.dtd is read into the object memory |
| 3                      | Verify the parser has generated 2 DTD tokens          | The parser has generated 2 DTD tokens                        |

##### test_5nested_elements

| Description            | Test generating DTD tokens from a file with 5 element |                                                              |
| ---------------------- | ----------------------------------------------------- | ------------------------------------------------------------ |
| **Initial conditions** | None                                                  |                                                              |
| **Test step**          | **Description**                                       | **Expected result**                                          |
| 1                      | Create DTD parser object                              | A new DTD parser object is created                           |
| 2                      | Read file 5nested_elements.dtd                        | The file 5nested_elements.dtd is read into the object memory |
| 3                      | Verify the parser has generated 5 DTD tokens          | The parser has generated 5 DTD tokens                        |

##### test_12elements

| Description            | Test generating DTD tokens from a file with 12 element |                                                        |
| ---------------------- | ------------------------------------------------------ | ------------------------------------------------------ |
| **Initial conditions** | None                                                   |                                                        |
| **Test step**          | **Description**                                        | **Expected result**                                    |
| 1                      | Create DTD parser object                               | A new DTD parser object is created                     |
| 2                      | Read file 12elements.dtd                               | The file 12elements.dtd is read into the object memory |
| 3                      | Verify the parser has generated 12 DTD tokens          | The parser has generated 12 DTD tokens                 |

#### test_tokenize_content_attributes

##### test_1element_1attribute

| Description            | Test generating DTD tokens from a file with 1 element and 1 attribute |                                                              |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                         |                                                              |
| **Test step**          | **Description**                                              | **Expected result**                                          |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                           |
| 2                      | Read file 1element_1attribute.dtd                            | The file 1element_1attribute.dtd is read into the object memory |
| 3                      | Verify the parser has generated 2 DTD tokens                 | The parser has generated 2 DTD tokens                        |

##### test_1element_6attributes

| Description            | Test generating DTD tokens from a file with 1 element and 6 attributes |                                                              |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                         |                                                              |
| **Test step**          | **Description**                                              | **Expected result**                                          |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                           |
| 2                      | Read file 1element_6attributes.dtd                           | The file 1element_6attributes.dtd is read into the object memory |
| 3                      | Verify the parser has generated 7 DTD tokens                 | The parser has generated 7 DTD tokens                        |

##### test_1element_2attributes

| Description            | Test generating DTD tokens from a file with 1 element and 2 attributes |                                                              |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                         |                                                              |
| **Test step**          | **Description**                                              | **Expected result**                                          |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                           |
| 2                      | Read file 1element_2attributes.dtd                           | The file 1element_2attributes.dtd is read into the object memory |
| 3                      | Verify the parser has generated 3 DTD tokens                 | The parser has generated 3 DTD tokens                        |

##### test_9elements_3attributes

| Description            | Test generating DTD tokens from a file with 9 elements and 3 attributes |                                                              |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                         |                                                              |
| **Test step**          | **Description**                                              | **Expected result**                                          |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                           |
| 2                      | Read file 9elements_3attributes.dtd                          | The file 9elements_3attributes.dtd is read into the object memory |
| 3                      | Verify the parser has generated 12 DTD tokens                | The parser has generated 12 DTD tokens                       |

##### test_11elements_6attributes

| Description            | Test generating DTD tokens from a file with 11 elements and 6 attributes |                                                              |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                         |                                                              |
| **Test step**          | **Description**                                              | **Expected result**                                          |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                           |
| 2                      | Read file 11elements_6attributes.dtd                         | The file 11elements_6attributes.dtd is read into the object memory |
| 3                      | Verify the parser has generated 17 DTD tokens                | The parser has generated 17 DTD tokens                       |

#### test_tokenize_content_exceptions

##### test_empty_file

| Description            | Test raising exception from generating DTD tokens from an empty file |                                                        |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------ |
| **Initial conditions** | None                                                         |                                                        |
| **Test step**          | **Description**                                              | **Expected result**                                    |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                     |
| 2                      | Read file empty_file.dtd                                     | The file empty_file.dtd is read into the object memory |
| 3                      | Verify the parser has generated 0 DTD tokens                 | The parser has generated 0 DTD tokens                  |
| 4                      | Verify the parser has read no content from the file          | The parser has read an empty string as file content    |

##### test_dtd_mixed_with_text

| Description            | Test raising exception from generating DTD tokens from an empty file |                                                              |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                         |                                                              |
| **Test step**          | **Description**                                              | **Expected result**                                          |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                           |
| 2                      | Read file dtd_mixed_with_text.dtd                            | The file dtd_mixed_with_text.dtd is read into the object memory |
| 3                      | Verify the parser has generated 0 DTD tokens                 | The parser has generated 0 DTD tokens                        |

#### test_parse_tokens_elements

##### test_1element

| Description            | Test parsing the DTD tokens to DTD objects from a file with 1 DTD element |                                                            |
| ---------------------- | ------------------------------------------------------------ | ---------------------------------------------------------- |
| **Initial conditions** | None                                                         |                                                            |
| **Test step**          | **Description**                                              | **Expected result**                                        |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                         |
| 2                      | Read file 1element.dtd                                       | The file 1element.dtd is read into the object memory       |
| 3                      | Verify the element note has 1 sub-element                    | The element note has 1 sub-element                         |
| 4                      | Verify the element note has empty element-name               | The element note has empty string for an element-name      |
| 5                      | Verify the element note's first child has name #PCDATA       | The element note's first child element is #PCDATA          |
| 6                      | Verify the element note's first child has no sub-elements    | The element note's first child element has no sub-elements |

##### test_1comment_1element

| Description            | Test parsing the DTD tokens to DTD objects from a file with 1 DTD element and 1 comment |                                                             |
| ---------------------- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| **Initial conditions** | None                                                         |                                                             |
| **Test step**          | **Description**                                              | **Expected result**                                         |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                          |
| 2                      | Read file 1element.dtd                                       | The file 1element.dtd is read into the object memory        |
| 3                      | Verify the parser has generated 1 element                    | The parser has parsed 1 element and has ignored the comment |

##### test_1complex_element

| Description            | Test parsing the DTD tokens to DTD objects from a file with 1 complex DTD element |                                                              |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                         |                                                              |
| **Test step**          | **Description**                                              | **Expected result**                                          |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                           |
| 2                      | Read file 1complex_element.dtd                               | The file 1complex_element.dtd is read into the object memory |
| 3                      | Verify the element note has 3 sub-element                    | The element note has 3 sub-element                           |
| 4                      | Verify the element note has empty element-name               | The element note has empty string for an element-name        |
| 5                      | Verify the element note's first child has name "Title"       | The element note's first child element is "Title"            |
| 6                      | Verify the element note's first child occurs only once       | The element note's first child occurs only once              |
| 7                      | Verify the element note's first child has no sub-elements    | The element note's first child element has no sub-elements   |
| 8                      | Verify the element note's second child has name "Course"     | The element note's second child element is "Course"          |
| 9                      | Verify the element note's second child occurs one or more times | The element note's second child occurs one or more times     |
| 10                     | Verify the element note's second child has no sub-elements   | The element note's second child element has no sub-elements  |
| 11                     | Verify the element note's third child has name "Lecturer"    | The element note's third child element is "Lecturer"         |
| 12                     | Verify the element note's third child occurs zero or more times | The element note's third child occurs zero or more times     |
| 13                     | Verify the element note's third child has no sub-elements    | The element note's third child element has no sub-elements   |

##### test_nested_child_elements

| Description            | Test parsing the DTD tokens to DTD objects from a file with nested child DTD elements |                                                              |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                         |                                                              |
| **Test step**          | **Description**                                              | **Expected result**                                          |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                           |
| 2                      | Read file nested_child_elements.dtd                          | The file nested_child_elements.dtd is read into the object memory |
| 3                      | Verify the element note has 2 sub-elements                   | The element note has 2 sub-elements                          |
| 4                      | Verify the element note has empty element-name               | The element note has empty string for an element-name        |
| 5                      | Verify the element note occurs one more mote times.          | The element note occurs one more mote times.                 |
| 6                      | Verify the element note's first child has name "A"           | The element note's first child element is "A"                |
| 7                      | Verify the element note's first child occurs zero or one time | The element note's first child occurs zero or one time       |
| 8                      | Verify the element note's first child has no sub-elements    | The element note's first child element has no sub-elements   |
| 8                      | Verify the element note's second child has two sub-elements  | The element note's second child has two sub-elements         |
| 9                      | Verify the element note's second child occurs zero or one time | The element note's second child occurs zero or one time      |
| 10                     | Verify the element note's second child has empty element-name | The element note's second child has empty element-name       |
| 11                     | Verify the element note's second child's first sub-element has name "B" | The element note's second child's first sub-element has name "B" |
| 12                     | Verify the element note's second child's first sub-element occurs one or mote times | The element note's second child's first sub-element occurs one or mote times |

##### test_complex_elements

| Description            | Test parsing the DTD tokens to DTD objects from a file with complex DTD elements |                                                              |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                         |                                                              |
| **Test step**          | **Description**                                              | **Expected result**                                          |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                           |
| 2                      | Read file complex_elements.dtd                               | The file complex_elements.dtd is read into the object memory |
| 3                      | Verify the element with name "Course_Catalog" has 1 sub-element | The element with name "Course_Catalog" has 1 sub-element     |
| 4                      | Verify the element with name "Department" has 3 sub-elements | The element with name "Department" has 3 sub-elements        |
| 5                      | Verify the element with name "game" has 2 sub-elements       | The element with name "game" has 2 sub-elements              |

#### test_parse_tokens_attributes

##### test_1element

| Description            | Test parsing the DTD tokens to DTD objects from a file with 1 DTD element and 0 attributes |                                                      |
| ---------------------- | ------------------------------------------------------------ | ---------------------------------------------------- |
| **Initial conditions** | None                                                         |                                                      |
| **Test step**          | **Description**                                              | **Expected result**                                  |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                   |
| 2                      | Read file 1element.dtd                                       | The file 1element.dtd is read into the object memory |
| 3                      | Verify the parsed object has 1 element                       | The parsed object has 1 element                      |

##### test_1element_1attribute

| Description            | Test parsing the DTD tokens to DTD objects from a file with 1 DTD element and 1 DTD attribute |                                                              |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                         |                                                              |
| **Test step**          | **Description**                                              | **Expected result**                                          |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                           |
| 2                      | Read file 1element_1attribute.dtd                            | The file 1element_1attribute.dtd is read into the object memory |
| 3                      | Verify the parsed object has 1 element                       | The parsed object has 1 element                              |
| 4                      | Verify the parser has 1 attribute in total                   | The parser has 1 attribute in total                          |
| 5                      | Verify the element's first attribute has name "width"        | The element's first attribute has name "width"               |
| 6                      | Verify the element's first attribute has value "0"           | Тhe element's first attribute has value "0"                  |
| 7                      | Verify the element's first attribute is of CDATA type        | The element's first attribute is of CDATA type               |
| 8                      | Verify the element's first attribute's value is of VALUE type | The element's first attribute's value is of VALUE type       |

##### test_9elements_3attributes

| Description            | Test parsing the DTD tokens to DTD objects from a file with 9 DTD elements and 3 DTD attributes |                                                              |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                         |                                                              |
| **Test step**          | **Description**                                              | **Expected result**                                          |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                           |
| 2                      | Read file 9elements_3attributes.dtd                          | The file 9elements_3attributes.dtd is read into the object memory |
| 3                      | Verify the parsed object has 9 elements                      | The parsed object has 9 elements                             |
| 4                      | Verify the parser has 3 attributes in total                  | The parser has 3 attributes in total                         |
| 5                      | Verify the first attribute with name "game" has a value type "REQUIRED" | The first attribute with name "game" has a value type "REQUIRED" |
| 6                      | Verify the attributes with name "score" are 2                | Тhe attributes with name "score" are 2                       |

##### test_11elements_6attributes

| Description            | Test parsing the DTD tokens to DTD objects from a file with 11 DTD elements and 6 DTD attributes |                                                              |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                         |                                                              |
| **Test step**          | **Description**                                              | **Expected result**                                          |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                           |
| 2                      | Read file 11elements_6attributes.dtd                         | The file 11elements_6attributes.dtd is read into the object memory |
| 3                      | Verify the parsed object has 11 elements                     | The parsed object has 11 elements                            |
| 4                      | Verify the parser has 6 attributes in total                  | The parser has 6 attributes in total                         |

#### test_parse_tokens_exceptions

##### test_non_dtd_tags

| Description            | Test parsing invalid DTD tokens    |                                    |
| ---------------------- | ---------------------------------- | ---------------------------------- |
| **Initial conditions** | None                               |                                    |
| **Test step**          | **Description**                    | **Expected result**                |
| 1                      | Create DTD parser object           | A new DTD parser object is created |
| 2                      | Try to read file invalid_token.dtd | The parser throws a `ValueError`   |

##### test_invalid_element_children

| Description            | Test parsing invalid DTD children elements    |                                    |
| ---------------------- | --------------------------------------------- | ---------------------------------- |
| **Initial conditions** | None                                          |                                    |
| **Test step**          | **Description**                               | **Expected result**                |
| 1                      | Create DTD parser object                      | A new DTD parser object is created |
| 2                      | Try to read file invalid_element_children.dtd | The parser throws a `ValueError`   |

#### test_root_finding

##### test_no_root

| Description            | Test parsing DTD file with no root |                                    |
| ---------------------- | ---------------------------------- | ---------------------------------- |
| **Initial conditions** | None                               |                                    |
| **Test step**          | **Description**                    | **Expected result**                |
| 1                      | Create DTD parser object           | A new DTD parser object is created |
| 2                      | Try to read file no_root.dtd       | The parser throws a `ValueError`   |

#### test_root_finding_exceptions

##### test_1element

| Description            | Test parsing DTD file and getting the root |                                                      |
| ---------------------- | ------------------------------------------ | ---------------------------------------------------- |
| **Initial conditions** | None                                       |                                                      |
| **Test step**          | **Description**                            | **Expected result**                                  |
| 1                      | Create DTD parser object                   | A new DTD parser object is created                   |
| 2                      | Try to read file 1element.dtd              | The file 1element.dtd is read into the object memory |
| 3                      | Verify the root's name is "note"           | The root's name is "note"                            |

##### test_2nested_elements

| Description            | Test parsing DTD file with 2 nested elements and getting the root |                                                              |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                         |                                                              |
| **Test step**          | **Description**                                              | **Expected result**                                          |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                           |
| 2                      | Try to read file 2nested_elements.dtd                        | The file 2nested_elements.dtd is read into the object memory |
| 3                      | Verify the root's name is "note"                             | The root's name is "note"                                    |

##### test_11elements_6attributes

| Description            | Test parsing DTD file with 11 elements, 6 attributes and getting the root |                                                              |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                         |                                                              |
| **Test step**          | **Description**                                              | **Expected result**                                          |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                           |
| 2                      | Try to read file 11elements_6attributes.dtd                  | The file 11elements_6attributes.dtd is read into the object memory |
| 3                      | Verify the root's name is "Course_Catalog"                   | The root's name is "Course_Catalog"                          |

##### test_9elements_3attributes

| Description            | Test parsing DTD file with 9 elements, 3 attributes and getting the root |                                                              |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                         |                                                              |
| **Test step**          | **Description**                                              | **Expected result**                                          |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                           |
| 2                      | Try to read file 9elements_3attributes.dtd                   | The file 9elements_3attributes.dtd is read into the object memory |
| 3                      | Verify the root's name is "games"                            | The root's name is "games"                                   |

##### test_14elements_2attributes

| Description            | Test parsing DTD file with 14 elements, 2 attributes and getting the root |                                                              |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                         |                                                              |
| **Test step**          | **Description**                                              | **Expected result**                                          |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created                           |
| 2                      | Try to read file 14elements_2attributes.dtd                  | The file 14elements_2attributes.dtd is read into the object memory |
| 3                      | Verify the root's name is "Course_Catalog"                   | The root's name is "Course_Catalog"                          |

#### test_parse_string

##### test_1element

| Description            | Test parsing DTD file string                        |                                             |
| ---------------------- | --------------------------------------------------- | ------------------------------------------- |
| **Initial conditions** | None                                                |                                             |
| **Test step**          | **Description**                                     | **Expected result**                         |
| 1                      | Create DTD parser object                            | A new DTD parser object is created          |
| 2                      | Try to parse the string "<!ELEMENT note (#PCDATA)>" | The string is loaded into the object memory |
| 3                      | Verify the elements and attributes count is 1       | The elements and attributes count is 1      |

##### test_1element_1attribute

| Description            | Test parsing DTD file string                                 |                                             |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------- |
| **Initial conditions** | None                                                         |                                             |
| **Test step**          | **Description**                                              | **Expected result**                         |
| 1                      | Create DTD parser object                                     | A new DTD parser object is created          |
| 2                      | Try to parse the string "<!ELEMENT square EMPTY><!ATTLIST square width CDATA "0">" | The string is loaded into the object memory |
| 3                      | Verify the elements and attributes count is 2                | The elements and attributes count is 2      |

### wiki_api

#### test_wiki_api

##### test_get_text

| Description            | Test getting the text from an Wikipedia article              |                                                           |
| ---------------------- | ------------------------------------------------------------ | --------------------------------------------------------- |
| **Initial conditions** | None                                                         |                                                           |
| **Test step**          | **Description**                                              | **Expected result**                                       |
| 1                      | Send a request for the needed article                        | A `Content` object is created in the memory               |
| 2                      | Verify that the content is split correctly and the content is accurate | The content is split correctly and the content is accurate |

##### test_get_text_header 

| Description            | Test getting the text and headers from an Wikipedia article |                                             |
| ---------------------- | ----------------------------------------------------------- | ------------------------------------------- |
| **Initial conditions** | None                                                        |                                             |
| **Test step**          | **Description**                                             | **Expected result**                         |
| 1                      | Send a request for the needed article                       | A `Content` object is created in the memory |
| 2                      | Verify that the content is split correctly                  | The content is split correctly              |
| 3                      | Verify that the content type is correct                     | The content type is correct                 |
| 4                      | Verify that the content is accurate                         | The content is accurate                                          |

##### test_get_text_header 

| Description            | Test getting the text, headers and image from an Wikipedia article |                                             |
| ---------------------- | ----------------------------------------------------------- | ------------------------------------------- |
| **Initial conditions** | None                                                        |                                             |
| **Test step**          | **Description**                                             | **Expected result**                         |
| 1                      | Send a request for the needed article                       | A `Content` object is created in the memory |
| 2                      | Verify that the content is split correctly                  | The content is split correctly              |
| 3                      | Verify that the content type is correct                     | The content type is correct                 |
| 4                      | Verify that the content is accurate                         | The content is accurate                     |

### test_xml_generator

#### test_1element

| Description            | Test generating an XML tree based on a DTD file        |                                                      |
| ---------------------- | ------------------------------------------------------ | ---------------------------------------------------- |
| **Initial conditions** | None                                                   |                                                      |
| **Test step**          | **Description**                                        | **Expected result**                                  |
| 1                      | Create DTD parser object                               | A new DTD parser object is created                   |
| 2                      | Read the file 1element.dt                              | The file 1element.dtd is read into the object memory |
| 3                      | Create XML generator object                            | An XML generator object is created                   |
| 4                      | Generate xml                                           | Generates an XML file based on the DTD parser object |
| 5                      | Verify that the XML converted to string is as expected | The XML string is equal to `<note />`                |
| 6                      | Verify that the root tag of the XML is 'note'          | The root tag of the XML is 'note'                    |
#### test_2nested_elements

| Description            | Test generating an XML tree based on a DTD file        |                                                              |
| ---------------------- | ------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                   |                                                              |
| **Test step**          | **Description**                                        | **Expected result**                                          |
| 1                      | Create DTD parser object                               | A new DTD parser object is created                           |
| 2                      | Read the file 2nested_elements.dtd                     | The file 2nested_elements.dtd is read into the object memory |
| 3                      | Create XML generator object                            | An XML generator object is created                           |
| 4                      | Generate xml                                           | Generates an XML file based on the DTD parser object         |
| 5                      | Verify that the XML converted to string is as expected | The XML string is equal to `<note><heading /></note>`        |

#### test_1element_1attribute

| Description            | Test generating an XML tree based on a DTD file        |                                                              |
| ---------------------- | ------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                   |                                                              |
| **Test step**          | **Description**                                        | **Expected result**                                          |
| 1                      | Create DTD parser object                               | A new DTD parser object is created                           |
| 2                      | Read the file 1element_1attribute.dtd                  | The file 1element_1attribute.dtd is read into the object memory |
| 3                      | Create XML generator object                            | An XML generator object is created                           |
| 4                      | Generate xml                                           | Generates an XML file based on the DTD parser object         |
| 5                      | Verify that the XML converted to string is as expected | The XML string is equal to `<square width="0" />`            |

#### test_5nested_elements

| Description            | Test generating an XML tree based on a DTD file        |                                                              |
| ---------------------- | ------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                   |                                                              |
| **Test step**          | **Description**                                        | **Expected result**                                          |
| 1                      | Create DTD parser object                               | A new DTD parser object is created                           |
| 2                      | Read the file 5nested_elements.dtd                     | The file 5nested_elements.dtd is read into the object memory |
| 3                      | Create XML generator object                            | An XML generator object is created                           |
| 4                      | Generate xml                                           | Generates an XML file based on the DTD parser object         |
| 5                      | Verify that the XML converted to string is as expected | The XML string is equal to `<note><to /><from /><heading /><body /></note>` |

#### test_1element_6attributes

| Description            | Test generating an XML tree based on a DTD file        |                                                              |
| ---------------------- | ------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                   |                                                              |
| **Test step**          | **Description**                                        | **Expected result**                                          |
| 1                      | Create DTD parser object                               | A new DTD parser object is created                           |
| 2                      | Read the file 1element_6attributes.dtd                 | The file 1element_6attributes.dtd is read into the object memory |
| 3                      | Create XML generator object                            | An XML generator object is created                           |
| 4                      | Generate xml                                           | Generates an XML file based on the DTD parser object         |
| 5                      | Verify that the XML converted to string is as expected | The XML string is equal to `<square width="0" number="" fax="" company="Microsoft" type="cash"title="Mr or Mrs" />` |

#### test_11elements_6attributes

| Description            | Test generating an XML tree based on a DTD file        |                                                              |
| ---------------------- | ------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                   |                                                              |
| **Test step**          | **Description**                                        | **Expected result**                                          |
| 1                      | Create DTD parser object                               | A new DTD parser object is created                           |
| 2                      | Read the file 11elements_6attributes.dtd               | The file 11elements_6attributes.dtd is read into the object memory |
| 3                      | Create XML generator object                            | An XML generator object is created                           |
| 4                      | Generate xml                                           | Generates an XML file based on the DTD parser object         |
| 5                      | Verify that the XML converted to string is as expected | The XML string is equal to `<Course_Catalog Year="2017-2018"><Department Code=""><Title '/><Course Number=""><Title /><Description><Courseref Number=""/></Description></Course><Lecturer InstrID=""><First_Name/><Middle_Initial /><Last_Name/></Lecturer></Department></Course_Catalog>` |

#### test_9elements_3attributes

| Description            | Test generating an XML tree based on a DTD file        |                                                              |
| ---------------------- | ------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                   |                                                              |
| **Test step**          | **Description**                                        | **Expected result**                                          |
| 1                      | Create DTD parser object                               | A new DTD parser object is created                           |
| 2                      | Read the file 9elements_3attributes.dtd                | The file 9elements_3attributes.dtd is read into the object memory |
| 3                      | Create XML generator object                            | An XML generator object is created                           |
| 4                      | Generate xml                                           | Generates an XML file based on the DTD parser object         |
| 5                      | Verify that the XML converted to string is as expected | The XML string is equal to `<games><game score=""><home-team /><ex-team /><scores><score time="" type=""><player /></score></scores><yellows><player/></yellows><reds><player /></reds></game></games>` |

#### test_14elements_2attributes

| Description            | Test generating an XML tree based on a DTD file        |                                                              |
| ---------------------- | ------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                   |                                                              |
| **Test step**          | **Description**                                        | **Expected result**                                          |
| 1                      | Create DTD parser object                               | A new DTD parser object is created                           |
| 2                      | Read the file 14elements_2attributes.dtd               | The file 14elements_2attributes.dtd is read into the object memory |
| 3                      | Create XML generator object                            | An XML generator object is created                           |
| 4                      | Generate xml                                           | Generates an XML file based on the DTD parser object         |
| 5                      | Verify that the XML converted to string is as expected | The XML string is equal to `<Course_Catalog><Department Code=""><Title '<br/>                                                '/><Chair><Professor><First_Name /><Middle_Initial /><Last_Name '<br/>                                                '/></Professor></Chair><Course CourseNumber=""><Title /><Description '<br/>                                                '/><Instructors><Lecturer><First_Name /><Middle_Initial /><Last_Name '<br/>                                                '/></Lecturer><Professor><First_Name /><Middle_Initial /><Last_Name '<br/>                                                '/></Professor></Instructors><Prerequisites><Prereq '<br/>                                                '/></Prerequisites></Course></Department></Course_Catalog>` |

#### test_nested_child_elements

| Description            | Test generating an XML tree based on a DTD file        |                                                              |
| ---------------------- | ------------------------------------------------------ | ------------------------------------------------------------ |
| **Initial conditions** | None                                                   |                                                              |
| **Test step**          | **Description**                                        | **Expected result**                                          |
| 1                      | Create DTD parser object                               | A new DTD parser object is created                           |
| 2                      | Read the file nested_child_elements.dtd                | The file nested_child_elements.dtd is read into the object memory |
| 3                      | Create XML generator object                            | An XML generator object is created                           |
| 4                      | Generate xml                                           | Generates an XML file based on the DTD parser object         |
| 5                      | Verify that the XML converted to string is as expected | The XML string is equal to `<D><A /><B /><C /></D>`          |