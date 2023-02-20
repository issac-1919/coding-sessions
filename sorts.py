class divide_conquer:
    def merge_sort(self, l):
        print(f"List before sort:{l}")
        if len(l) > 1:
            mid = len(l)//2
            left_ = l[:mid]
            right_ = l[mid:]
            self.merge_sort(left_)
            self.merge_sort(right_)
            flag1 = flag2 = flag3 = 0
            while flag1<len(left_) and flag2<len(right_):
                if left_[flag1] < right_[flag1]:
                    l[flag3] = left_[flag1]
                    flag1 += 1
                else:
                    l[flag3] = right_[flag2]
            while flag1<len(left_):
                l[flag3] = left_[flag1]
                flag1 += 1
                flag3 += 1
            while flag2<len(right_):
                l[flag3] = right_[flag2]
                flag2 += 1
                flag3 += 1
        return print(f"sorted list: {l}")
    
    def heap_sort(self):
        return


def tester():
    data = [221, 101, 1, 5, 2, 4, 8, 7, 16, 11, 10, 100]
    dc = divide_conquer()
    dc.merge_sort(data)