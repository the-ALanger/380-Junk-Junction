import csv
from ItemInfo import ItemInfo
from UpdateCSVs import UpdateCSVs
from UserCurrent import UserCurrent

#THIS IS A TEST FILE FOR READING CSV DATA
class InventoryDatabase:
    
    # 2D and only has values 
    # row 0 is the labels
    with open('CSV/JJInventoryDatabase.csv', newline='') as f:
        reader = csv.reader(f)
        data_values_2D = list(reader)

    # And then printing the list of dictionaries
    # print(" Print dictionary list:")  
    # print(csv_data)

        
    # Creating ItemInfo objects for each row in the CSV
    curID=0
    itemList = []
    with open('CSV/JJInventoryDatabase.csv', newline='') as f:
        reader = csv.reader(f)
        for row in csv.reader(f):
            Item = ItemInfo(
                itemID=row[0],
                userID=row[1],
                itemName=row[2],
                itemDescription=row[3],
                itemCondition=row[4],
                itemCategory=row[5],
                itemPrice=row[6],
                itemStatus=row[7],
                itemComments=row[8],
            )
            itemList.append(Item)
        curID=itemList[-1].itemID

    # change the method signature to include self
    def get_item_with_id(self, itemID):
        for item in InventoryDatabase.itemList:
            if item.itemID == str(itemID):
                return item
        return None
    
    def get_items_with_user_id(self, userID):
        user_items = []
        for item in InventoryDatabase.itemList:
            if item.userID == str(userID):
                user_items.append(item)
        return user_items




 # 2D and only has values 
    # row 0 is the labels
    with open('CSV/JJLogInventory.csv', newline='') as f:
        reader = csv.reader(f)
        data_values_2D = list(reader)

    # And then printing the list of dictionaries
    # print(" Print dictionary list:")  
    # print(csv_data)

        
    # Creating ItemInfo objects for each row in the CSV
    logItemList = []
    with open('CSV/JJLogInventory.csv', newline='') as f:
        reader = csv.reader(f)
        for row in csv.reader(f):
            logItem = ItemInfo(
                itemID=row[0],
                userID=row[1],
                itemName=row[2],
                itemDescription=row[3],
                itemCondition=row[4],
                itemCategory=row[5],
                itemPrice=row[6],
                itemStatus=row[7],
                itemComments=row[8],
            )
            logItemList.append(logItem)
            
    ''' Marks an item as sold by updating its status and moving it to the log list.
        Takes an ItemInfo object as input, and returns nothing.
    '''
    def make_sold(item):
        item.itemStatus = "Sold"
        for logItem in InventoryDatabase.logItemList:
            if logItem.itemID == str(item.itemID):
                return  # Item already logged as sold
        InventoryDatabase.logItemList.append(item)
        InventoryDatabase.itemList.remove(item)
        
    ''' Creates a new item and adds it to the item list.
        Takes all item name, description, condition, category, and price as input. Generates a default itemID 
        and userID from the current user. Returns the created ItemInfo object.
    '''  
    def create_new_item(itemName, itemDescription, itemCondition, itemCategory, itemPrice):
        newItem = ItemInfo(
            itemID=str(int(InventoryDatabase.curItemID) + 1),
            userID=UserCurrent.current_user.userID,
            itemName=itemName,
            itemDescription=itemDescription,
            itemCondition=itemCondition,
            itemCategory=itemCategory,
            itemPrice=itemPrice,
            itemStatus="Available",
            itemComments="",
        )
        InventoryDatabase.itemList.append(newItem)
        return newItem
        
    ''' Updates the CSV files with the current item lists 
        Calls UpdateCSVs using the itemList and logItemList.
    '''
    def update_csv():
        filename = "CSV/JJInventoryDatabase.csv"
        UpdateCSVs.update_item_csv(filename, InventoryDatabase.itemList)

        logFilename = "CSV/JJLogInventory.csv"
        UpdateCSVs.update_item_csv(logFilename, InventoryDatabase.logItemList)
        
    
        
