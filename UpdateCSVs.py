import csv
    

class UpdateCSVs:
    '''
    UpdateCSVs.py
    11/18/2025
    Anthony Langer, Ian Flack

    This class is responsible for updating CSV files for items and users.
    Each method takes a filename and an array of data objects to write to the CSV file.
    The CSV files are created or overwritten with the provided data.
    '''

    def update_item_csv(filename, data):

        '''Updates the item CSV file with the provided array data.'''
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
                item.itemComments,
                item.itemImage
            ])
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows) # Writes all rows at once
            # Alternatively, to write row by row:
            # for row in data:
            #     writer.writerow(row)

        print(f"CSV file '{filename}' created successfully.")
        
    def update_user_csv(filename, data):
        
        '''Updates the user CSV file with the provided array data.'''
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
