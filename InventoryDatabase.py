import csv
#THIS IS A TEST FILE FOR READING CSV DATA
class InventoryDatabase:
        
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
    with open('JJInventoryDatabase.csv', newline='') as f:
        reader = csv.reader(f)
        data_values_2D = list(reader)
        
    
    
    

    
    

    # And then printing the list of dictionaries
    # print("         Print dictionary list:")  
    # print(csv_data)