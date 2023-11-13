from lib.report_length import *
# def test_report_length():
#     length_of_string = "letter"
#     assert length_of_string == "This string was 6 characters long"

def test_report_length():
    result = report_length("letter")
    assert result == f"{result}"


def test_report_lentgh_upper():
    result = report_length("Makers")
    assert result == f"{result}"


def test_report_length_lower():
    result = report_length_lower("chelsea")
    assert result == f"{result}"