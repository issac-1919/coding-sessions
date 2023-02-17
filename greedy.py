""" 
GREEDY APPROACH

> Simple approach which gives you optimal solution most of the times.
> This is used in optimization problems like finding MAX or MIN of something.

STEPS
- Choose a value which is immediately closer to the desired result.
- Break down the problem into similar sub problems based on the value chosen
- Repeat this step till the globally optimal solution is arrived
"""

def coin_change_problem():
    denominations = [1, 2, 5, 10]
    # inp = int(input())
    inp = 20
    l1=[]
    if inp in denominations:
        return print("You don't need change for:$", inp)
    for x in sorted(denominations, reverse=True):
        if x < inp:
            l1.append(x)
            inp = inp-x
    return print("Change :", l1)


def coin_change_problem_2():
    denominations = [1, 2, 5, 10]
    # inp = int(input()) 
    inp = 14
    x = inp
    l1 = {}

    for denom in denominations[::-1]:
        if x != 0:
            # 15//10 = 1
            # 15%10 = 5
            l1[denom] = x//denom
            x = x%denom
    
    return ("\nChange for {}: {}\n".format(inp, l1))

coin_change_problem_2()