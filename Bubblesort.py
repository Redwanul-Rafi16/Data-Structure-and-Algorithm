
#function for bubblesort
def bubblesort(arr):
 n=len(arr)

 for i in range(n):
    for j in range( n-i-1):
        if arr[j]>arr[j+1]:
             temp=arr[j]
             arr[j]=arr[j+1]
             arr[j+1]=temp
#main function             
if __name__=="__main__":
  arr=list(map(int,input("Enter array:").split()))
  bubblesort(arr)
  for i in range(len(arr)):
    print("%d "%arr[i],end='')
    #print(*arr)