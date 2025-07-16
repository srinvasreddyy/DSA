"""
given an sorted array need to square each element and again sort them 
its may be empty array, single element , negative also
"""

arr=[]

def squared(arr):
    newArr = [0]*len(arr)
    start=0
    end=len(arr)-1
    for k in reversed(range(len(arr))):
        if(arr[start]**2 > arr[end]**2):
            newArr[k]=arr[start]**2
            start+=1
        else:
            newArr[k]=arr[end]**2
            end-=1
    return newArr

print(squared(arr))
