def binary_search(collection: list, target: str) -> bool:

    left = 0
    right = len(collection) - 1

    while left <= right:
        mid = (left + right)//2
        
        if collection[mid] == target:
            return True

        elif collection[mid] < target:
            left = mid + 1

        else:
            right = mid + 1
    
    return False

ls = [i for i in range(0,100)]
print()
print(binary_search(ls,101))