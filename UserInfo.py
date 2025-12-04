
class UserInfo:
    '''
    UserInfo.py
    11/06/2025
    Anthony Langer, Ian Flack

    A UserInfo object holds details about a user including userID, name, email, and password.
    Realistically, passwords should be hashed for security, but for simplicity, they are stored in plain text here.
    It should also be integrated with UserDatabase as this is just a data class.
    '''
    def __init__(self,userID,name,email,password):
        
        '''Initializes a UserInfo object with user details.'''
        self.userID = userID
        self.name = name
        self.email = email
        self.password = password
