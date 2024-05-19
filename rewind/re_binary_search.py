import math
import array

items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def binary_search(array, number):
    
    lo = 0
    hi = len(array) - 1
    iter = 0
    while lo <= hi:
        if iter > 10:
            break
        else:
            iter += 1
        print('hi = ', hi, ' lo = ', lo, ' iter = ', iter)
        mid = math.floor(((hi - lo)/2) + lo)
        print('mid = ', mid)
        value = array[mid]
        if number == value:
            return mid
        elif value < number:
            lo = mid + 1
        else:
            hi = mid - 1

print(binary_search(items, 0))

print(items)

print(array.array('i', range(10)))