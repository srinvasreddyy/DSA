"""
given an array it might be same eles , and eles greater than 2 number of eles
should return 2nd largest
"""

arr=[10,10,10]

def secLargest(arr):
    highest=float('-inf')
    secondHighest=float('-inf')
    for i in range(len(arr)):
        if(arr[i]>highest):
            secondHighest = highest
            highest = arr[i]

    return -1 if secondHighest == float('-inf') else secondHighest

print(secLargest(arr))
        
