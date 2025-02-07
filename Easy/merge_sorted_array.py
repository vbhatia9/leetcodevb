def merge_sorted_arrays(arr1, arr2):
    n, m = len(arr1), len(arr2)

    for i in range(n):
        if arr1[i] > arr2[0]:
            # Swap elements
            arr1[i], arr2[0] = arr2[0], arr1[i]
            arr2.sort()  # Sort the second array after each swap

# Example

if __name__ == "__main__": 
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    merge_sorted_arrays(arr1, arr2)
    print(arr1)  # Output: [1, 2, 3]
    print(arr2)  # Output: [4, 5, 6]
