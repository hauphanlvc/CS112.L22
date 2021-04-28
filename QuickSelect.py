import io,os,sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

def partition(arr, low, high) : 
  
    pivot = arr[high] 
    i = (low - 1) 
    for j in range(low, high) : 
        if arr[j] >= pivot : 
            i += 1
            arr[i], arr[j] = arr[j], arr[i] 
          
    arr[i + 1], arr[high] = arr[high], arr[i + 1] 
    return (i + 1) 
  
# Implementation of QuickSelect 
def kthSmallest(a, left, right, k) : 
  
    while left <= right : 
  
        # Partition a[left..right] around a pivot 
        # and find the position of the pivot 
        pivotIndex = partition(a, left, right) 
  
        # If pivot itself is the k-th smallest element 
        if pivotIndex == k - 1 : 
            return a[pivotIndex] 
  
        # If there are more than k-1 elements on 
        # left of pivot, then k-th smallest must be 
        # on left side. 
        elif pivotIndex > k - 1 :
            right = pivotIndex - 1
  
        # Else k-th smallest is on right side. 
        else :
            left = pivotIndex + 1
      
    
    
n, k = map(int,input().split())
a = []
for i in range(n):
    a.append(int(input()))
# a.sort()
# print(a[-k])
print(kthSmallest(a,0,n-1,k))
# Source Code : hhttps://www.geeksforgeeks.org/quickselect-a-simple-iterative-implementation/