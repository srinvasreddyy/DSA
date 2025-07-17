"""
Rotate Array
Difficulty: MediumAccuracy: 37.06%Submissions: 537K+Points: 4Average Time: 20m
Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.

Note: Consider the array as circular.

Examples :

Input: arr[] = [1, 2, 3, 4, 5], d = 2
Output: [3, 4, 5, 1, 2]
Explanation: when rotated by 2 elements, it becomes 3 4 5 1 2.
Input: arr[] = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], d = 3
Output: [8, 10, 12, 14, 16, 18, 20, 2, 4, 6]
Explanation: when rotated by 3 elements, it becomes 8 10 12 14 16 18 20 2 4 6.
Input: arr[] = [7, 3, 9, 1], d = 9
Output: [3, 9, 1, 7]
Explanation: when we rotate 9 times, we'll get 3 9 1 7 as resultant array.
Constraints:
1 <= arr.size(), d <= 105
0 <= arr[i] <= 105

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""

# def rotateArray(d,arr):
#     return arr[d:]+arr[:d]  here arr[:d] creates a new list and + operator copies then complexities willbe O(n),O(n)

def rotateArray(d,arr):
    newArr=[0]*len(arr)
    j=0
    for i in range(len(arr)):
        if(i<len(arr)-d):
            newArr[i]=arr[i+d]
        else:
            newArr[i]=arr[j]
            j+=1
    return newArr

print(rotateArray(2,[1,2,3,4,5]))