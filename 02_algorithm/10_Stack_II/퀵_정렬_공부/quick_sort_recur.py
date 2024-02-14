def quick_sort(lst):
    if len(lst) <= 1:  # 분할 불가능 할 때까지 분할
        return lst
    else:
        pvt = lst[0]
        less_than_pivot = [x for x in lst[1:] if x <= pvt]
        more_than_pivot = [x for x in lst[1:] if x > pvt]
        return quick_sort(less_than_pivot) + [pvt] + quick_sort(more_than_pivot)


arr = [5, 1, 8, 9, 4, 1, 6, 2, 7]
result = quick_sort(arr)

print(result)