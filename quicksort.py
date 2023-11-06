def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    return j

def quicksort(arr, low, high):
    if low < high:
        loc = partition(arr, low, high)
        quicksort(arr, low, loc - 1)
        quicksort(arr, loc + 1, high)

if __name__ == '__main__':
    arr = list(map(int, input("Enter array: ").split()))
    n = len(arr)
    low = 0
    high = n - 1

    quicksort(arr, low, high)

    print("Sorted array:")
    print(*arr)
