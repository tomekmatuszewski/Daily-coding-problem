#Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
# return all strings in the set that have s as a prefix.

#For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].


#Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.


def find_strings(arr, prefix):
    result = []
    for element in arr:
        if element.startswith(prefix):
            result.append(element)
    return result


print(find_strings(['dog', 'deer', 'deal'], 'de'))