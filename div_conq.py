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

divide_and_conquer()