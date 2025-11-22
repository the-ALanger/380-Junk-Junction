import csv
from UserInfo import UserInfo
from UpdateCSVs import UpdateCSVs

class UserDatabase:
    """
    UserDatabase.py
    11/06/2025
    Anthony Langer, Ian Flack

    This class loads user data from a CSV file into UserInfo objects and
    provides methods to access and update this data.
    Uses UserInfo.py to define the user data structure.
    Uses UpdateCSVs.py to write changes back to the CSV file.
    """

    userList = []
    with open('CSV/JJUserDatabase.csv', newline='') as f:
        
        '''On class load, read the CSV and populate userList with UserInfo objects.
        '''
        reader = csv.reader(f)
        for row in csv.reader(f):
            user = UserInfo(
                userID=row[0],
                name=row[1],
                email=row[2], 
                password=row[3]
            )
            userList.append(user)

    def get_user_with_id(self, userID):
        '''Gets a user by their userID.
        Returns the UserInfo object if found, else returns None.
        '''
        for user in UserDatabase.userList:
            if user.userID == str(userID):
                return user
        return None
    
    def update_csv():
        '''Updates the user CSV file with the current userList data.'''
        filename = "CSV/JJUserDatabase.csv"
        UpdateCSVs.update_user_csv(filename, UserDatabase.userList)
        
    def create_account(name, email, password):
        user = UserInfo(
            userID=str(int(UserDatabase.curID)+1),
            name=name,
            email=email,
            password=password
        )
        UserDatabase.userList.append(user)
        UserDatabase.curID = str(int(UserDatabase.curID)+1)
        UserDatabase.update_csv()
        return user
