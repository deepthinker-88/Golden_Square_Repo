from lib.string_builder import *

def test_add_two_strings():
    string = StringBuilder()
    result = string.add('James-Leigh')
    assert result == 'James-Leigh'


def test_size_of_str():
    string = StringBuilder()
    length_of_string = string.size('Makers')
    assert length_of_string == 6


def test_output_string():
    string = StringBuilder()
    output_string = string.output("CODING BOOTCAMP")
    assert output_string == output_string.upper()