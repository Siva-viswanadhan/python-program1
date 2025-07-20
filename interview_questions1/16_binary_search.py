#Write a Python code to implement a binary search algorithm

def binary_search(lst,target):
    lst.sort()
    low = 0
    high = len(lst) - 1
    flag = False

    while low<= high:
        mid = (low + high) // 2
        if target > lst[mid]:
            low = mid + 1
        elif target < lst[mid]:
            high = mid - 1
        elif lst[mid] == target:
            flag = True
            break

    if flag:
        print('element found')
    else:
        print('element not found')

binary_search([1,2,4,5,3,8,9],0)
