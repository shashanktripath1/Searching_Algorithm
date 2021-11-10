#iterative approach binary search
l=list(map(float,input("Input Elemnts In List \t").split()))
target=float(input("Enter The Target Element \t"))
def binary_search_iterative(l,target):
    beg=0
    end=len(l)-1
    mid=0
    while(beg<=end):
        mid=(beg+end)//2
        if l[mid]==target:
            return mid
        elif l[mid]>target:
            end=mid-1
        elif l[mid]<target:
            beg=mid+1
        else:
            return mid
    return -1
result=binary_search_iterative(l,target)
if result!=-1:
    print("target element ",target," is found at index ",result)
else:
    print("element not present in the list")

#recursive approach binary search
l=list(map(float,input("Input Elements in Array").split()))
target=float(input("enter the target element"))
def binary_search_recursive(l,beg,end,target):
    mid=0
    while(beg<=end):
        mid=(beg+end)//2
        if l[mid]==target:
            return mid
        elif l[mid]>target:
            return binary_search_recursive(l,beg,mid-1,target)
        elif l[mid]<target:
            return binary_search_recursive(l,mid+1,end,target)
        else:
            return mid
    return -1
res=binary_search_recursive(l,0,len(l)-1,target)
if res!=-1:
    print("target element ",target,"is found at index ",res)
else:
    print("target element ",target," is not present in the list")
    
        
