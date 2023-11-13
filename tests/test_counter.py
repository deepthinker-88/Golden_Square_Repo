from lib.counter import *

def test_add():
    count = Counter()
    count_total = count.add(4)
    assert count_total == 4


def test_report():
    count = Counter()
    total_count = count.report()
    assert total_count == f"{total_count}"