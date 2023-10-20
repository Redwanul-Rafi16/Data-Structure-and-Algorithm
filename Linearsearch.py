def linearsearch(arr, n, search_number):
    for i in range(n):
        if arr[i] == search_number:
            return 1
    return 0

if __name__ == "__main__":
    arr = list(map(int, input("Enter Array: ").split()))
    N = len(arr)
    b = int(input("What integer do you want to search for: "))  
    k = linearsearch(arr, N, b)
    if k == 1:
        print("YES")
    else:
        print("NO")
