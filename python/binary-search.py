# from math import floor
import math

elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(elements)
print(len(elements))

for x in range(5): 
    print(x)

def my_binary_search(list, number):
    '''
    Test docstring
    
    list -- argument 1

    number -- argument 2
    
    returns: String with index position'''
    result = None
    
    lo = 0
    hi = len(elements) - 1

    while lo <= hi:
        mid = math.floor((lo + hi) / 2)

        if list[mid] == number:
            return mid
        elif list[mid] > number:
            hi = mid - 1
        else:
            lo = mid + 1


print('found index {0} for 0'.format(my_binary_search(elements, 0)))
print('found index {0} for 3'.format(my_binary_search(elements, 3)))
print('found index {0} for 4'.format(my_binary_search(elements, 4)))
print('found index {0} for 5'.format(my_binary_search(elements, 5)))
print('found index {0} for 6'.format(my_binary_search(elements, 6)))
print('found index {0} for 7'.format(my_binary_search(elements, 7)))
print('found index {0} for 9'.format(my_binary_search(elements, 9)))
print('found index {0} for 10'.format(my_binary_search(elements, 10)))



# def binary_search(list, item):
#     low = 0
#     high = len(list) - 1
#     while low <= high:
#         mid = (low + high) / 2
#         guess = list[mid]
#         if guess == item:
#             return mid
#         if guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None

# my_list = [1, 3, 5, 7, 9]

# print (binary_search(my_list, 3))

# print('found index {0} for 0'.format(binary_search(elements, 0)))
# print('found index {0} for 5'.format(binary_search(elements, 5)))
# print('found index {0} for 6'.format(binary_search(elements, 6)))
# print('found index {0} for 7'.format(binary_search(elements, 7)))
# print('found index {0} for 9'.format(binary_search(elements, 9)))
# print('found index {0} for 10'.format(binary_search(elements, 10)))

# print(len(elements))