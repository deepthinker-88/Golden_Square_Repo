from lib.gratitudes import *

def test_add():
    appreciation = Gratitudes()
    appreciation.add("You're Welcome!")
    assert appreciation.format() == "Be grateful for: You're Welcome!"
