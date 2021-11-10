#linear search
def linear_search(l,target):
    for i in range(len(l)):
        if target==l[i]:
            return i
    return -1
l=list(map(float,input("Input Elements In List ").split()))
target=float(input("enter the target element "))
print("list after elements are input = ",l)
a=linear_search(l,target)
if a!=-1:
    print("the target element ",target," is found at ",a," index")
else:
    print("target element",target," is not present in list")
 
    
    
