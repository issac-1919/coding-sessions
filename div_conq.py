def divide_and_conquer():
    # inp = map(int, input().split())
    # inp = [2, 4, 6, 7, 1, 9]
    inp = sorted([2, 4, 6, 7, 1, 9])

    div = divide(inp)
    cq = conquer(div)
    res = combine(cq)

    return res

def divide(li):
    pass
def conquer(div):
    pass
def combine(cq):
    pass

def binary_search(l, target, beg, end):
    """
    Binary Search:
    Recursive binary search to find an element in a sorted list
    Parameters:
    l: sorted list
    target: element to search
    beg: first index of the list
    end: length of the list
    """
    mid = (beg + end)//2
    if target == l[mid]:
        return print(f"element {target} found at index-{mid}")
    elif target < l[mid]:
        return binary_search(l, target, beg, mid)
    elif target > l[mid]:
        return binary_search(l, target, mid, end)
    

def tester_1():
    l = [1, 4, 6, 22, 78, 91, 92, 102]
    try:
        binary_search(l, 101, 0, len(l))
    except RecursionError:
        return ("Element not present in the list")