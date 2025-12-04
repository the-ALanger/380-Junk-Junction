import csv
from ItemInfo import ItemInfo
from UpdateCSVs import UpdateCSVs
from UserCurrent import UserCurrent

#THIS IS A TEST FILE FOR READING CSV DATA
class InventoryDatabase:
    """
    InventoryDatabase.py
    10/20/2025
    Anthony Langer, Ian Flack

    This class manages the inventory database by reading item data from a CSV file.
    It creates ItemInfo objects for each item and stores them in a itemlist[].
    provides methods to access and manipulate the inventory data.
    """
        
    # Creating ItemInfo objects for each row in the CSV
    curItemID = 0
    itemList = []
    with open('CSV/JJInventoryDatabase.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            item = ItemInfo(
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
            itemList.append(item)
    if itemList:
        try:
            curItemID = int(itemList[-1].itemID)
        except Exception:
            curItemID = 0

    @staticmethod
    def get_item_with_id(itemID):
        '''Gets an item by its itemID.
        Returns the ItemInfo object if found, else returns None.
        '''
        for item in InventoryDatabase.itemList:
            if item.itemID == str(itemID):
                return item
        return None
        
    # Reading CSV file row by row
    # with open('JJInventoryDatabase.csv', 'r') as file:
    #     reader = csv.reader(file)  # For comma-separated values
    #         # For tab-separated values, use: reader = csv.reader(file, delimiter='\t')

    #     print("         Print CSV row by row:")  
    #     for row in reader:
    #         print(row)

    # Function to read CSV into a list of dictionaries
    def read_item_dicts(filepath):              
        """
        Reads a CSV file into a list of dictionaries.
        """
        data = []
        with open(filepath, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data
    
    # Using the 'def read_item_dicts(filepath)' function to read the CSV file
    # 1D and has labels with the values
    # row 0 is first item
    csv_w_label = read_item_dicts('JJInventoryDatabase.csv')
    
    # 2D and only has values 
    # row 0 is the labels
    with open('CSV/JJInventoryDatabase.csv', newline='') as f:
        reader = csv.reader(f)
        data_values_2D = list(reader)
        
    
    
    
    @staticmethod
    def get_items_with_user_id(userID):
        '''Gets ALL items associated with a specific userID.
        Returns a list of ItemInfo objects.
        '''
        user_items = []
        for item in InventoryDatabase.itemList:
            if item.userID == str(userID):
                user_items.append(item)
        return user_items
    
    @staticmethod
    def get_items_with_user(user):
        '''Gets ALL items associated with a specific UserCurrent object.
        Returns a list of ItemInfo objects.
        '''
        user_items = []
        for item in InventoryDatabase.itemList:
            if item.userID == str(user.userID):
                user_items.append(item)
        return user_items

    # log list read
    logItemList = []
    with open('CSV/JJLogInventory.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
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
            
    @staticmethod
    def make_sold(item):
        ''' Marks an item as sold by updating its status and moving it to the log list.
        Takes an ItemInfo object as input, and returns nothing.
        '''
        item.itemStatus = "Sold"
        for logItem in InventoryDatabase.logItemList:
            if logItem.itemID == str(item.itemID):
                return
        InventoryDatabase.logItemList.append(item)
        try:
            InventoryDatabase.itemList.remove(item)
        except ValueError:
            pass
    
    @staticmethod
    def create_new_item(itemName, itemDescription, itemCondition, itemCategory, itemPrice):
        ''' Creates a new item and adds it to the item list.
        Takes all item name, description, condition, category, and price as input. Generates a default itemID 
        and userID from the current user. Returns the created ItemInfo object.
        '''  
        new_id = str(InventoryDatabase.curItemID + 1)
        newItem = ItemInfo(
            itemID=new_id,
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
        InventoryDatabase.curItemID += 1
        return newItem
        
    @staticmethod
    def update_csv():
        ''' Updates the CSV files with the current item lists 
        Calls UpdateCSVs using the itemList and logItemList.
        '''
        filename = "CSV/JJInventoryDatabase.csv"
        UpdateCSVs.update_item_csv(filename, InventoryDatabase.itemList)

        logFilename = "CSV/JJLogInventory.csv"
        UpdateCSVs.update_item_csv(logFilename, InventoryDatabase.logItemList)



