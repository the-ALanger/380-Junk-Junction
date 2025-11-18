import csv
class UpdateCSVs:
    
    
    '''A class to handle updating CSV files.
    Takes a file and an array and to write a new csv into that name.
    '''
    def update_item_csv(filename, data):
        rows = []
        for item in data:
            rows.append([
                item.itemID,
                item.userID,
                item.itemName,
                item.itemDescription,
                item.itemCondition,
                item.itemCategory,
                item.itemPrice,
                item.itemStatus,
                item.itemComments
            ])
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows) # Writes all rows at once
            # Alternatively, to write row by row:
            # for row in data:
            #     writer.writerow(row)

        print(f"CSV file '{filename}' created successfully.")
        
    def update_user_csv(filename, data):
        rows = []
        for user in data:
            rows.append([
                user.userID,
                user.name,
                user.email,
                user.password
            ])
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows) # Writes all rows at once
            # Alternatively, to write row by row:
            # for row in data:
            #     writer.writerow(row)

        print(f"CSV file '{filename}' created successfully.")
