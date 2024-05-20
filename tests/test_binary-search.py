from rewind.re_binary_search import binary_search
import array

def test_existing_items_found():
    items = array.array('i', range(10))
    assert binary_search(items, 0) == 0
    assert binary_search(items, 1) == 1
    assert binary_search(items, 9) == 9
    assert binary_search(items, 5) == 5

def test_non_existing_items():
    items = array.array('i', range(10))
    assert binary_search(items, -1) == None
    assert binary_search(items, -11) == None
    assert binary_search(items, 10) == None