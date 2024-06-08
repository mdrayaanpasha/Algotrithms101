#hello world! the following are codes for linear search and binary search in python
def linearSearch(arr,ele):
    found=-1
    
    for i in range(len(arr)):
        if arr[i]==ele:
            found=i
            break;
        
    if found != -1:
        print("found at index: ",found)
    else:
        print("not found!")

def binarySearch(arr,ele):
    low=0
    high = len(arr)
    
    got=-1
    while low<=high:
        mid=int((low+high)/2)
        if arr[mid] == ele:
            got=mid
            break
        elif arr[mid] < ele:
            low=mid+1
        else:
            high=low-1
            
    if got != -1:
        print("found at index: ",got)
    else:
        print("not found!")
        
        
        
arr=[0,1,8,9]
linearSearch(arr,2)
binarySearch(arr,2)
            
