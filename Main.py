from InventoryDatabase import InventoryDatabase

class Main:
    InvData = InventoryDatabase()
    print(InvData.csv_w_label[2:4])
    print("\n")
    print(InvData.csv_w_label[2])
    
    print("\n")

   
        
    print(InvData.data_values_2D[0][0])
    print(InvData.data_values_2D[1][2])
    print("\n")
    