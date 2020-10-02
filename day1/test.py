from .problem1 import check_given_array

def test_problem1():
    assert check_given_array([10, 15, 3, 7], 17)
    assert not check_given_array([], 17)
    assert not check_given_array([10, 15, 3, 4], 17)