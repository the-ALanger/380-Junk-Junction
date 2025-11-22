
class ItemComments:
    '''
    ItemComments.py
    11/20/2025
    Anthony Langer, Ian Flack

    Class to hold comments log for a specific item.'''
    def __init__(self, itemID, comments):
        '''Initializes an ItemComments object with itemID and comments.'''
        self.itemID = itemID
        self.comments = comments