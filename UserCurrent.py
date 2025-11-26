from UserDatabase import UserDatabase
class UserCurrent:
    
    
    def __init__(self, userID, name, email, password):
        self.userID = userID
        self.name = name
        self.email = email
        self.password = password

    def check_if_user_exists(email, password):
        for user in UserDatabase.userList:
            if user.email == email and user.password == password:
                return UserCurrent(
                    userID=user.userID,
                    name=user.name,
                    email=user.email,
                    password=user.password
                )
        return None
    
    def check_if_user_exists_by_email(email):
        for user in UserDatabase.userList:
            if user.email == email:
                return UserCurrent(
                    userID=user.userID,
                    name=user.name,
                    email=user.email,
                    password=user.password
                )
        return None
    
    users_items = {}
    
    current_user = None
    def set_current_user(user):
        UserCurrent.current_user = user
        
        users_items = UserDatabase.get_user_items(UserCurrent.current_user.user_id)
