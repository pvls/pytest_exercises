from pet import *

def test_pet_change_name():
    dog2 = Pet('Jorgin')
    assert dog2.change_name('Marcin') == 'Marcin'