import csv
from ItemInfo import ItemInfo
#THIS IS A TEST FILE FOR READING CSV DATA
class InventoryDatabase:
    
    # 2D and only has values 
    # row 0 is the labels
    with open('JJInventoryDatabase.csv', newline='') as f:
        reader = csv.reader(f)
        data_values_2D = list(reader)

    # And then printing the list of dictionaries
    # print(" Print dictionary list:")  
    # print(csv_data)

        
    # Creating ItemInfo objects for each row in the CSV
    itemList = []
    with open('JJInventoryDatabase.csv', newline='') as f:
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
                itemStatus=row[7]
            )
            itemList.append(Item)

    # change the method signature to include self
    def get_item_with_id(self, itemID):
        for item in InventoryDatabase.itemList:
            if item.itemID == str(itemID):
                return item
        return None
