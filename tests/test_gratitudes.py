from lib.gratitudes import *

def test_add():
    appreciation = Gratitudes()
    result = Gratitudes.add("You're Welcome!")
    result = self.gratitudes.append("You're Welcome!")
    assert result == "You're Welcome!"
