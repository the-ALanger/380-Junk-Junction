class ItemInfo:
    '''
    ItemInfo.py
    10/020/2025
    Anthony Langer, Ian Flack

    An ItemInfo object holds details about an item including itemID, userID, name, description, condition, category, price, status, and comments.
    It should be integrated with ItemDatabase as this is just a data class.
    '''
    def __init__(self, itemID, userID, itemName, itemDescription, itemCondition, itemCategory, itemPrice, itemStatus, itemComments):
        '''Initializes an ItemInfo object with item details.'''

        self.itemID = itemID
        self.userID = userID
        self.itemName = itemName
        self.itemDescription = itemDescription
        self.itemCondition = itemCondition
        self.itemCategory = itemCategory
        self.itemPrice = itemPrice
        self.itemStatus = itemStatus
        self.itemComments = itemComments  # Initialize with provided item comments path

    
    

