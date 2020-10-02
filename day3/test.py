from .problem3 import find_smallest_positive_integer

def test_find_smallest_positive_int():
    assert find_smallest_positive_integer([3, 4, -1, 1]) == 2
    assert find_smallest_positive_integer([1, 2, 0]) == 3
    assert find_smallest_positive_integer([0, 1, 2, 3, 5]) == 4
    assert find_smallest_positive_integer([-3, -2, -1, 0, 1]) == 2
    assert find_smallest_positive_integer([-3, -2, -1, 0 ]) == 1