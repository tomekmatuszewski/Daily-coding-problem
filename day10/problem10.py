#Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

from collections import Counter


def find_k_distinct_characters(string, k):
    chars = sorted(dict(Counter(string)).items(), key=lambda x: x[1], reverse=True)[:k]
    sel_chars = [x[0] for x in chars]
    new_str = ""
    for char in string:
        if char in sel_chars:
            new_str+= char
    return new_str



print(find_k_distinct_characters("abcbabba", 2))
print(find_k_distinct_characters("abcba", 2))