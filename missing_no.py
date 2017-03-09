def find_missing(array1, array2):

    # we Set longer array to list1, shorter to list2 else vice-versa
    if len(array1)> len(array2):
        list1 = array1
        list2 = array2
    else:
        list1 = array2
        list2 = array1

    # Go through elements in longer list
    for element in list1:
        if element not in list2:
            return element
print(find_missing([1,2,3], [1,2,3,4]))
print(find_missing([4,66,7], [66,77,7,4]))