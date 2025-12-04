from UserCurrent import UserCurrent

def test_check_of_user_exists():
    result = UserCurrent.check_if_user_exists()
    assert result == None
    