
def fibo_recursive(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibo_recursive(n-1) + fibo_recursive(n-2)

def fibo_dynamic(n):
    l = [0, 1]
    for i in range(2, n+1):
        l.append(l[i-1] + l[i-2])
    return l

def tester_1():
    # fibo_top_down(10)
    print(fibo_dynamic(899))