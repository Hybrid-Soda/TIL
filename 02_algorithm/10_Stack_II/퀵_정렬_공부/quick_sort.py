def partition(arr, low, high):
    pvt = (low + high)//2

    while low < high:
        while low < high and arr[low] < arr[pvt]: low += 1
        while low < high and arr[high] >= arr[pvt]: high -= 1

        if low < high:
            if low == pvt: pvt = high
            arr[low], arr[high] = arr[high], arr[low]

    arr[pvt], arr[high] = arr[high], arr[pvt]

    return high


def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)


arr = [5, 3, 8, 9, 4, 1, 6, 2, 7]
N = len(arr)
quick_sort(arr, 0, N-1)
print(arr)