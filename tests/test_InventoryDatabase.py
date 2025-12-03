
from InventoryDatabase import InventoryDatabase
from UserCurrent import UserCurrent


def test_get_item_with_id():
    result = InventoryDatabase.get_item_with_id(1004)
    assert result.itemName == "Smartphone"
    
   
# def test_get_items_with_user():
#     result = InventoryDatabase.get_items_with_user(77778)
#     assert len(result) == 4
#     assert result[0].itemName == "Smartphone"
#     assert result[1].itemName == "Bookshelf"
#     assert result[2].itemName == "Tennis Racket"
#     assert result[3].itemName == "Coffee Table"
    

def test_get_items_with_user_id():
    result = InventoryDatabase.get_items_with_user_id(1001)
    assert result == [1]
    

def test_get_items_with_user_id():
    result = InventoryDatabase.get_items_with_user_id(77777)
    assert len(result) == 2
    assert result[0].itemName == "Laptop"
    assert result[1].itemName == "Desk Chair"