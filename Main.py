from InventoryDatabase import InventoryDatabase
from UserDatabase import UserDatabase
from ItemInfo import ItemInfo

def main():
    InvData = InventoryDatabase()
    UData = UserDatabase()
 #Prints the column name and then the associated values in that row: 'itemID, 1003' as an Array
    print(InvData.csv_w_label[2:4])
    print("\n")
    
    #Prints the same things as before but as a String
    print(InvData.csv_w_label[2])
    print("\n")

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
    else:
        print("Item 1002 not found")

if __name__ == "__main__":
    main()

