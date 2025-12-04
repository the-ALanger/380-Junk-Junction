
from InventoryDatabase import InventoryDatabase
from UserDatabase import UserDatabase 
from UserCurrent import UserCurrent


def test_get_item_with_id():
    result = InventoryDatabase.get_item_with_id(1004)
    assert result.itemName == "Smartphone"
    
   
def test_get_items_with_user():
    user = UserDatabase.get_user_with_id(77778)
    result = InventoryDatabase.get_items_with_user(user)
    assert len(result) == 4
    assert result[0].itemName == "Smartphone"
    assert result[1].itemName == "Bookshelf"
    assert result[2].itemName == "Tennis Racket"
    assert result[3].itemName == "Coffee Table"
    

def test_get_items_with_user_id():
    result = InventoryDatabase.get_items_with_user_id(1001)
    assert result == [1]
    

def test_get_items_with_user_id():
    result = InventoryDatabase.get_items_with_user_id(77777)
    assert len(result) == 2
    assert result[0].itemName == "Laptop"
    assert result[1].itemName == "Desk Chair"
    
def test_create_new_item():
    UserCurrent.set_current_user(UserDatabase.get_user_with_id(77777))
    result = InventoryDatabase.create_new_item("dogBones", "Bones for dogs", "New", "Pet Supplies", "15.00")
    assert result.itemName == "dogBones"
    assert result.itemDescription == "Bones for dogs"
    assert result.itemCondition == "New"
    assert result.itemCategory == "Pet Supplies"
    assert result.itemPrice == "15.00"
