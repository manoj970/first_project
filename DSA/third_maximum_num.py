
def third_maximum(arr):
    arr=list(set(arr))
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j] > arr[min_index]:
                min_index=j

        arr[i],arr[min_index]=arr[min_index],arr[i]

    if len(arr) >= 3:
      return arr[2]
    else:
      return arr[0]
arr=[2,5,3,1,4]
print(third_maximum(arr))