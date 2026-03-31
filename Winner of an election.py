class Solution:
    def winner(self, arr):
        from collections import Counter
        
        freq = Counter(arr)
        
        max_votes = max(freq.values())
        
        # collect all candidates with max votes
        candidates = [name for name in freq if freq[name] == max_votes]
        
        # pick lexicographically smallest
        winner = min(candidates)
        
        return [winner, str(max_votes)]
