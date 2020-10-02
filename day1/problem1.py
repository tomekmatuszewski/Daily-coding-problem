# Given a list of numbers, return whether any two sums to k. For example,
# given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.


def check_given_array(arr, k):
    new_lst = set()
    for element in arr:
        if element in new_lst:
            return True
        new_lst.add(k - element)

    return False

