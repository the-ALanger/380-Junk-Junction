from UserDatabase import UserDatabase
 
class UserCurrent:
    '''
    UserCurrent.py
    11/06/2025
    Anthony Langer, Ian Flack
    This class manages the current user session.
    It includes methods to check if a user exists by email and password.
    '''
    current_user = None  # Initialize as None instead of dummy user

    def __init__(self, userID, name, email, password):
        '''Initializes a UserCurrent object with user details.'''
        self.userID = userID
        self.name = name
        self.email = email
        self.password = password

    
    @staticmethod
    def check_if_user_exists(email, password):
        ''' Checks if a user exists with the given email and password.
        Returns a UserCurrent object if found, else returns None.
        '''
        for user in UserDatabase.userList:
            if user.email == email and user.password == password:
                return user
        return None
    
    @staticmethod
    def check_if_user_exists_by_email(email):
        '''Checks if there is a user with the given email.
        Returns a UserCurrent object if found, else returns None.
        '''
        for user in UserDatabase.userList:
            if user.email == email:
                return user
        return None
            
    @staticmethod
    def set_current_user(user):
        '''Sets the current user session to the provided UserCurrent object.'''
        UserCurrent.current_user = user
        
    @staticmethod
    def get_current_user_id():
        '''Returns the userID of the current user session.'''
        if UserCurrent.current_user:
            return UserCurrent.current_user.userID
        return 00000


