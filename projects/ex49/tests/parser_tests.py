from nose.tools import *
from nose.tools import assert_raises
from ex49 import parser
from ex49.parser import ParserError

def test_parser():
    result = parser.parse_sentence(
                [('stop', 'the'), ('noun', 'bear'),
                ('verb', 'run'), ('direction', 'south')]
                )
    assert_equal(result.subject, 'bear')
    assert_equal(result.verb, 'run')
    assert_equal(result.object, 'south')

def add(x, y):
    result = parser.parse_sentence(
                [(x, y), (x, y),
                (x, y), (x, y)]
                )
    result.verb

assert_raises(ParserError, add, "noun", "bear")
