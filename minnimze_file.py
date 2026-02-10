#Given an array arr[] denoting heights of n towers and a positive integer k.

class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        if n == 1:
            return 0
        arr.sort()
        ans = arr[n-1] - arr[0]
        smallest = arr[0] + k
        largest = arr[n-1] - k
        for i in range(1, n):
            min_height = min(smallest, arr[i] - k)
            max_height = max(largest, arr[i-1] + k)
            if min_height < 0:
                continue
            ans = min(ans, max_height - min_height)
        return ans
