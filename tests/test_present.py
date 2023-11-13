import pytest
from lib.present import *

def test_wrap():
    gift = Present()
    with pytest.raises(Exception) as e:
        gift.wrap('Football')
        error_message = str(e.value)
        assert error_message == "A contents has already been wrapped."
