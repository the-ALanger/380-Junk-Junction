import csv
from UserInfo import UserInfo
from UpdateCSVs import UpdateCSVs
#THIS IS A TEST FILE FOR READING CSV DATA
class UserDatabase:
    
    
    # 2D and only has values 
    # row 0 is the labels
    with open('CSV/JJUserDatabase.csv', newline='') as f:
        reader = csv.reader(f)
        data_values_2D = list(reader)
        

        # Creating ItemInfo objects for each row in the CSV
    userList = [] 
    curID = 0
    with open('CSV/JJUserDatabase.csv', newline='') as f:
        reader = csv.reader(f)
        for row in csv.reader(f):
            user = UserInfo(
                userID=row[0],
                name=row[1],
                email=row[2], 
                password=row[3]
            )
            userList.append(user)
        curID=userList[-1].userID
        
    # change the method signature to include self
    def get_user_with_id(self, userID):
        for user in UserDatabase.userList:
            if user.userID == str(userID):
                return user
        return None
    
    def update_csv():
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
