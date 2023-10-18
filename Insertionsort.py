def insertionsort(arr):
  n=len(arr)
  i=1
  for i in range(n):
     item=arr[i]
     j=i-1
     while j>=0 and arr[j]>item:
        arr[j+1]=arr[j]
        j=j-1
        arr[j+1]=item

if __name__=="__main__":
 arr=[99,97,21,12,2,1]
 insertionsort(arr)
print(*arr)
#for i in range(len(arr)):
    #print("%d "%arr[i],end='')
