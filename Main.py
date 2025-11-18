from InventoryDatabase import InventoryDatabase
from UserDatabase import UserDatabase

def main():
    InvData = InventoryDatabase()
    UData = UserDatabase()
    
    InventoryDatabase.update_csv()
    UserDatabase.update_csv()
 #Prints the column name and then the associated values in that row: 'itemID, 1003' as an Array
########################################## INVENTORY DATABASE TESTING ###########################################

    #Prints the first header of the CSV file
    print(InvData.data_values_2D[0][0])
    print("\n")
    
    #Prints the first item under the first column
    print(InvData.data_values_2D[1][0])
    print("\n")
    
    #Prints the second header of the CSV file
    print(InvData.data_values_2D[0][1])
    print("\n")

########################################## USER DATABASE TESTING ###########################################
    print("Test For Users")
    print("\n")
    
    #Prints the header of the CSV: "name"
    print(UData.data_values_2D[0][0])
    print("\n")
    
    #Prints the first name under the name column in the CSV: "Anthony Langer"
    print(UData.data_values_2D[1][0])
    print("\n")
    
    
    #We can probably condense all of these different databases to one method that 
    # calls based on CSV file name
    item = InvData.get_item_with_id(1002)
    if item:
        print(item.itemName)
        print(item.itemDescription)
        print(item.itemPrice)
    else:
        print("Item 1002 not found")

    user = UData.get_user_with_id(69420)
    if user:
        print(user.name)
    else:
        print("User 69420 not found")
        
    user_items = InvData.get_items_with_user_id(77777)
    if user_items:
        for item in user_items:
            print(item.itemName)
    else:
        print("No items found for user 77777")

if __name__ == "__main__":
    main()

 