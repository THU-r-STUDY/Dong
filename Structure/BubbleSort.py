def bubbleSort(arr):
    if not isinstance(arr, list):
        return None
    if len(arr) == 0:
        return 0
    if arr is None:
        return None
    
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[i] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr