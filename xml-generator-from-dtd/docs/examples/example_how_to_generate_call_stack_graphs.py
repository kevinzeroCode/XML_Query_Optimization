import os
import unittest
from src.dtd_parser.dtd_parser import DTDParser
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
from pycallgraph import PyCallGraph, Config, GlobbingFilter
from pycallgraph.output import GraphvizOutput


class TestDTDParserParseString(unittest.TestCase):
    def test_1element(self):
        parser = DTDParser()
        parser.parse_string('<!ELEMENT note (#PCDATA)>')
        self.assertEqual(len(parser._tokens), 1)


config = Config(groups=True)
config.trace_filter = GlobbingFilter(include=['src.*', 'Test*'])

with PyCallGraph(config=config, output=GraphvizOutput(output_file='graph.png')):
    x = TestDTDParserParseString()
    x.setUp()
    x.test_1element()

