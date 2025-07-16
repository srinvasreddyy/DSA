"""
Check if array is strictly increaing or decareasing if yes it is monotonic 
empty array also monotonic
single element also monotonic
return True if monotonic else False
"""

arr=[1,2,3,4,3]

def monotonic(arr):
    if(len(arr)>0):
        if(arr[0]>arr[len(arr)-1]):
            for i in range(len(arr)):
                if(i==(len(arr)-1)):
                    return True
                else:
                    if(arr[i]>arr[i+1]):
                        continue
                    else:
                        return False
        if(arr[0]<arr[len(arr)-1]):
            for i in range(len(arr)):
                if(i==(len(arr)-1)):
                    return True
                else:
                    if(arr[i]<arr[i+1]):
                        continue
                    else:
                        return False
        if(arr[0]==arr[len(arr)-1]):
            for i in range(len(arr)):
                if(i==(len(arr)-1)):
                    return True
                else:
                    if(arr[i]==arr[i+1]):
                        continue
                    else:
                        return False
                    
print(monotonic(arr))