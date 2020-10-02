from .problem2 import array_product

def test_problem2():
    assert array_product([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert array_product([3, 2, 1]) == [2, 3, 6]