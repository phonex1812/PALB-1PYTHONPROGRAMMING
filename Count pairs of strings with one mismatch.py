class Solution:
    def countPairs(self, arr):
        from collections import defaultdict
        
        count = 0
        mp = defaultdict(int)
        
        for s in arr:
            for i in range(len(s)):
                # create pattern by replacing ith char
                pattern = s[:i] + '_' + s[i+1:]
                
                count += mp[pattern]
                mp[pattern] += 1
        
        return count
