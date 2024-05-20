from rewind.re_quicksort import sort

def test_sort_ok():
    assert sort([3,2,1]) == [1,2,3]
    assert sort([3,4,2,5,1]) == [1,2,3,4,5]
    assert sort([234, 23, 56, 123]) == [23,56,123,234]