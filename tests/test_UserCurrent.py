from UserCurrent import UserCurrent
from UserDatabase import UserDatabase


def test_check_if_user_exists():
    result = UserCurrent.check_if_user_exists("ian.flack.694@my.csun.edu", "password")
    assert result == UserDatabase.get_user_with_id(77777)
    
def test_check_if_user_exists_by_email():
    result = UserCurrent.check_if_user_exists_by_email("ian.flack.694@my.csun.edu")
    assert result == UserDatabase.get_user_with_id(77777)

def test_get_current_user_id():
    UserCurrent.set_current_user(UserDatabase.get_user_with_id(77778))
    result = UserCurrent.get_current_user_id()
    assert result == UserDatabase.get_user_with_id(77778).userID
