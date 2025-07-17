"""
You are given an array of integers arr[]. Your task is to reverse the given array.

Note: Modify the array in place.

Examples:

Input: arr = [1, 4, 3, 2, 6, 5]
Output: [5, 6, 2, 3, 4, 1]
Explanation: The elements of the array are 1 4 3 2 6 5. After reversing the array, the first element goes to the last position, the second element goes to the second last position and so on. Hence, the answer is 5 6 2 3 4 1.
Input: arr = [4, 5, 2]
Output: [2, 5, 4]
Explanation: The elements of the array are 4 5 2. The reversed array will be 2 5 4.
Input: arr = [1]
Output: [1]
Explanation: The array has only single element, hence the reversed array is same as the original.
Constraints:
1<=arr.size()<=105
0<=arr[i]<=105

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""

def reverseArray(arr):
    j=-1
    mid=(len(arr)/2)-1
    if(len(arr)==1):
            return arr
    for i in range(0,int(mid)):
        arr[i],arr[j]= arr[j],arr[i]
        j-=1
    return arr
arr=[1.2,6,3,7,3,5,43,6,3]
print(reverseArray(arr))