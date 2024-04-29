def linear_search(collection:list, target:str)->bool:

    for i in collection:
        if collection[i] == target:
            return True
    
    return False

ls = [i for i in range(0,100)]
print(linear_search(ls,42))