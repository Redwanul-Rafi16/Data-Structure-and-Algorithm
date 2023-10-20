def binary_search(arr, n, x):
    left=0 
    right = n - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == x:
            return True  # Element found
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return False  # Element not found

if __name__ == "__main__":
    arr = list(map(int, input("Enter the elements in sorted order: ").split()))
    x = int(input("What integer do you want to search for: "))
    n= len(arr)
    found = binary_search(arr, n, x)
    if found:
        print("YES")
    else:
        print("NO")
