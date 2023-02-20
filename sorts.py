def merge_sort(data):
        print(f"List before sort:{data}")
        if len(data) > 1:
            mid = len(data)//2
            left_ = data[:mid]
            right_ = data[mid:]
            merge_sort(left_)
            merge_sort(right_)
            flag1 = flag2 = flag3 = 0
            
            while flag1<len(left_) and flag2<len(right_):
                if left_[flag1] <= right_[flag2]:
                    data[flag3] = flag1
                    flag1 += 1
                else:
                    data[flag3] = flag2
                    flag2 += 1
                flag3 += 1
            
            while flag1<len(left_):
                data[flag3] = left_[flag1]
                flag1 += 1
                flag3 += 1
            while flag2<len(right_):
                data[flag3] = left_[flag2]
                flag2 += 1
                flag3 += 1

def tester():
    data = [221, 101, 1, 5, 2, 4, 8, 7, 16, 11, 10, 100]
    merge_sort(data)
    for i in range(len(data)):
        print(data[i], end=',')