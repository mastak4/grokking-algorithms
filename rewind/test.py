items = [2,4,6]
def sum(array):
    if len(array) == 0:
        return 0
    else:
        return array[0] + sum(array[1:])
    
print(sum(items))