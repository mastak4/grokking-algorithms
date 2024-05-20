def sort(arr):
    if len(arr) < 2: # base case, we don't need to sort arr of zero or one element
        return arr
    pivot = arr[0] # we take a random number and compare all other numbers to it, sorting lesser and bigger numbers into separate arrs and sort them afterwards
    less = [i for i in arr[1:] if i <= pivot] # we ignore first element as it's a pivot
    greater = [i for i in arr[1:] if i > pivot]
    return sort(less) + [pivot] + sort(greater) # sort first less part, add pivot to the center or after all sorted numbers that are lower, and after that add all sorted numbers that are bigger