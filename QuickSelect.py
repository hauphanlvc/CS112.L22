import io,os,sys
 # input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
sys.stdin = open("QuickSelect.txt","r")

def partition(arr, l, r):
     
    x = arr[r]
    i = l
    for j in range(l, r):
         
        if arr[j] >= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
             
    arr[i], arr[r] = arr[r], arr[i]
    return i
 
# finds the kth position (of the sorted array)
# in a given unsorted array i.e this function
# can be used to find both kth largest and
# kth smallest element in the array.
# ASSUMPTION: all elements in arr[] are distinct
def kthSmallest(arr, l, r, k):
 
    # if k is smaller than number of
    # elements in array
    if (k > 0 and k <= r - l + 1):
 
        # Partition the array around last
        # element and get position of pivot
        # element in sorted array
        index = partition(arr, l, r)
 
        # if position is same as k
        if (index - l == k - 1):
            return arr[index]
 
        # If position is more, recur
        # for left subarray
        if (index - l > k - 1):
            return kthSmallest(arr, l, index - 1, k)
 
        # Else recur for right subarray
        return kthSmallest(arr, index + 1, r,
                            k - index + l - 1)
    
n, k = map(int,input().split())
a = []
for i in range(n):
    a.append(int(input()))
# a.sort()
# print(a[-k])
print(kthSmallest(a,0,n-1,k))
# Source Code : https://www.geeksforgeeks.org/quickselect-algorithm/