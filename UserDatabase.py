import csv
from UserInfo import UserInfo
#THIS IS A TEST FILE FOR READING CSV DATA
class UserDatabase:
        
    
    
    # 2D and only has values 
    # row 0 is the labels
    with open('JJUserDatabase.csv', newline='') as f:
        reader = csv.reader(f)
        data_values_2D = list(reader)
        

        # Creating ItemInfo objects for each row in the CSV
    userList = []
    with open('JJUserDatabase.csv', newline='') as f:
        reader = csv.reader(f)
        for row in csv.reader(f):
            Item = UserInfo(
                userID=row[0],
                name=row[1],
                email=row[2], 
                password=row[3]
            )
            userList.append(Item)

    # change the method signature to include self
    def get_user_with_id(self, userID):
        for user in UserDatabase.userList:
            if user.userID == str(userID):
                return user
        return None