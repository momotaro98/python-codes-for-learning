def quick_sort(arr):
    left = []
    right = []
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    arr = arr[1:]
    for ele in arr:
        if ele <= pivot:
            left.append(ele) # 手続きしてる
        elif ele > pivot:
            right.append(ele)
    left = quick_sort(left)
    right = quick_sort(right)
    return left + [pivot] + right
