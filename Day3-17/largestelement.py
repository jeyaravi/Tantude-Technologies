arr = [5, 2, 8, 1, 9, 3]
largest = arr[0]
for i in range(1, len(arr)):
    if arr[i] > largest:
        largest = arr[i]
print("The largest element is:", largest)