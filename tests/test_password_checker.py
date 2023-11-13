from lib.password_checker import *
import pytest

def test_check():
    check_password= PasswordChecker()
    check_password.check('makers12345')
    with pytest.raises(Exception) as e:
        if len(check_password)>=8:
            return True
        error_message = str(e.value)
        assert error_message == "Invalid password, must be 8+ characters."