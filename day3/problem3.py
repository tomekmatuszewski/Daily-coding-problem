#This problem was asked by Stripe.

#Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.

#For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#You can modify the input array in-place

def find_smallest_positive_integer(arr):
    if max(arr) <= 0 or arr == []:
        return 1
    sorted_arr = [x for x in sorted(arr) if x>0]
    for i in range(len(sorted_arr)-1):
        if sorted_arr[i] + 1 == sorted_arr[i+1] and sorted_arr[i] > 0:
            continue
        else:
            return sorted_arr[i]+1
    return max(sorted_arr)+1



