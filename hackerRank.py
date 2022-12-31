def maximum_subArray(arr):
    res=[0 for i in range(len(arr))]
    for i in range(1, len(arr)):
        res=[arr[i-i]]
    print(res) ** 2

arr=[1, -1, 1, -1, 1]
print(maximum_subArray(arr))
